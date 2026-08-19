/*
SIGMA Genesis-5 Native Compiler
Compiles the Genesis core subset directly:
    .sigma source -> SIGMA Bytecode ABI v1.0 (.sigmab)

No Python is required at runtime or compile time for this native path.
*/
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <ctype.h>
#include <errno.h>

/* ABI */
#define OP_PUSH_CONST 0x01
#define OP_POP 0x02
#define OP_LOAD 0x10
#define OP_STORE 0x11
#define OP_UNARY 0x20
#define OP_BINARY 0x21
#define OP_CALL 0x30
#define OP_RETURN 0x31
#define OP_JUMP 0x40
#define OP_JUMP_IF_FALSE 0x41
#define OP_HALT 0xFF

#define U_NOT 0x01
#define U_NEG 0x02
#define U_POS 0x03

#define B_ADD 0x01
#define B_SUB 0x02
#define B_MUL 0x03
#define B_DIV 0x04
#define B_FLOORDIV 0x05
#define B_MOD 0x06
#define B_POW 0x07
#define B_EQ 0x10
#define B_NE 0x11
#define B_LT 0x12
#define B_GT 0x13
#define B_LE 0x14
#define B_GE 0x15
#define B_AND 0x20
#define B_OR 0x21

#define TAG_NULL 0x00
#define TAG_BOOL 0x01
#define TAG_INT 0x02
#define TAG_FLOAT 0x03
#define TAG_STR 0x04

typedef enum {
    TK_EOF=0, TK_IDENT, TK_NUMBER, TK_STRING, TK_OP,
    TK_LPAREN, TK_RPAREN, TK_LBRACE, TK_RBRACE,
    TK_LBRACKET, TK_RBRACKET, TK_COLON, TK_SEMI, TK_COMMA, TK_DOT,
    TK_COMMAND, TK_SIGMA, TK_DYNAMIC, TK_STATIC
} TokenKind;

typedef struct {
    TokenKind kind;
    char *text;
    int line;
    int col;
} Token;

typedef struct {
    const char *src;
    size_t len, pos;
    int line, col;
    Token tok;
} Lexer;

typedef enum { C_NULL, C_BOOL, C_INT, C_FLOAT, C_STR } ConstType;
typedef struct {
    ConstType type;
    int boolean;
    int64_t integer;
    double floating;
    char *string;
} Constant;

typedef struct {
    uint8_t op;
    uint32_t a;
    uint16_t b;
} Instruction;

typedef struct {
    Instruction *v;
    uint32_t n, cap;
} Code;

typedef struct {
    uint32_t name_sym;
    uint32_t *params;
    uint16_t param_count;
    Code code;
} Function;

typedef struct {
    char **symbols;
    uint32_t symbol_count, symbol_cap;

    Constant *constants;
    uint32_t constant_count, constant_cap;

    Function *functions;
    uint32_t function_count, function_cap;

    Code main_code;
} Module;

typedef struct {
    Lexer lx;
    Module mod;
    int failed;
    char error[512];
} Parser;

static void die_oom(void){ fprintf(stderr,"sigmac: out of memory\n"); exit(2); }
static void *xmalloc(size_t n){ void *p=malloc(n?n:1); if(!p)die_oom(); return p; }
static void *xrealloc(void *p,size_t n){ void *q=realloc(p,n?n:1); if(!q)die_oom(); return q; }
static char *xstrndup(const char *s,size_t n){ char *p=(char*)xmalloc(n+1); memcpy(p,s,n); p[n]=0; return p; }
static char *xstrdup(const char *s){ return xstrndup(s,strlen(s)); }

static int starts(const char *s,size_t n,const char *lit){
    size_t m=strlen(lit); return n>=m && memcmp(s,lit,m)==0;
}

static void token_free(Token *t){ free(t->text); t->text=NULL; }

static void lexer_init(Lexer *l,const char *src){
    memset(l,0,sizeof(*l)); l->src=src; l->len=strlen(src); l->line=2; l->col=1;
}

static void bump(Lexer *l,size_t n){
    for(size_t i=0;i<n;i++){
        char c=l->src[l->pos++];
        if(c=='\n'){ l->line++; l->col=1; } else l->col++;
    }
}

static int is_ident_start(unsigned char c){ return isalpha(c)||c=='_'; }
static int is_ident_cont(unsigned char c){ return isalnum(c)||c=='_'; }

static char *unescape_string(const char *s,size_t n){
    char *out=(char*)xmalloc(n+1); size_t j=0;
    for(size_t i=0;i<n;i++){
        if(s[i]=='\\' && i+1<n){
            i++;
            switch(s[i]){
                case 'n': out[j++]='\n'; break;
                case 'r': out[j++]='\r'; break;
                case 't': out[j++]='\t'; break;
                case '\\': out[j++]='\\'; break;
                case '"': out[j++]='"'; break;
                case '\'': out[j++]='\''; break;
                default: out[j++]=s[i]; break;
            }
        } else out[j++]=s[i];
    }
    out[j]=0; return out;
}

static Token lex_next(Lexer *l){
    token_free(&l->tok);
    while(l->pos<l->len){
        const char *p=l->src+l->pos; size_t rem=l->len-l->pos;
        if(*p==' '||*p=='\t'||*p=='\r'||*p=='\n'){ bump(l,1); continue; }
        if(starts(p,rem,"//")){
            int line_prefix_ws=1;
            size_t j=l->pos;

            while(j>0){
                char prev=l->src[j-1];

                if(prev=='\n') break;

                if(prev!=' ' && prev!='\t' && prev!='\r'){
                    line_prefix_ws=0;
                    break;
                }

                j--;
            }

            if(line_prefix_ws){
                while(l->pos<l->len && l->src[l->pos]!='\n')
                    bump(l,1);

                continue;
            }
        }

        int line=l->line,col=l->col;
        Token t={0}; t.line=line; t.col=col;

        /* UTF-8 SIGMA sigils */
        if(starts(p,rem,"\xE2\x9F\xA1")){ t.kind=TK_COMMAND; t.text=xstrdup("⟡"); bump(l,3); l->tok=t; return t; }
        if(starts(p,rem,"\xCE\xA3")){ t.kind=TK_SIGMA; t.text=xstrdup("Σ"); bump(l,2); l->tok=t; return t; }
        if(starts(p,rem,"\xE2\x9A\xA1")){ t.kind=TK_DYNAMIC; t.text=xstrdup("⚡"); bump(l,3); l->tok=t; return t; }
        if(starts(p,rem,"\xE2\x8B\x88")){ t.kind=TK_STATIC; t.text=xstrdup("⋈"); bump(l,3); l->tok=t; return t; }

        if(is_ident_start((unsigned char)*p)){
            size_t s=l->pos; bump(l,1);
            while(l->pos<l->len && is_ident_cont((unsigned char)l->src[l->pos])) bump(l,1);
            t.kind=TK_IDENT; t.text=xstrndup(l->src+s,l->pos-s); l->tok=t; return t;
        }

        if(isdigit((unsigned char)*p)){
            size_t s=l->pos; int dot=0; bump(l,1);
            while(l->pos<l->len){
                char c=l->src[l->pos];
                if(isdigit((unsigned char)c)){ bump(l,1); continue; }
                if(c=='.'&&!dot){ dot=1; bump(l,1); continue; }
                break;
            }
            t.kind=TK_NUMBER; t.text=xstrndup(l->src+s,l->pos-s); l->tok=t; return t;
        }

        if(*p=='"' || *p=='\''){
            char q=*p; bump(l,1); size_t s=l->pos; int esc=0;
            while(l->pos<l->len){
                char c=l->src[l->pos];
                if(!esc && c==q) break;
                if(!esc && c=='\\') esc=1; else esc=0;
                bump(l,1);
            }
            if(l->pos>=l->len){ t.kind=TK_EOF; t.text=xstrdup("<unterminated-string>"); l->tok=t; return t; }
            size_t e=l->pos; bump(l,1);
            t.kind=TK_STRING; t.text=unescape_string(l->src+s,e-s); l->tok=t; return t;
        }

        #define ONE(ch,k) if(*p==(ch)){ t.kind=(k); t.text=xstrndup(p,1); bump(l,1); l->tok=t; return t; }
        ONE('(',TK_LPAREN) ONE(')',TK_RPAREN) ONE('{',TK_LBRACE) ONE('}',TK_RBRACE)
        ONE('[',TK_LBRACKET) ONE(']',TK_RBRACKET) ONE(':',TK_COLON) ONE(';',TK_SEMI)
        ONE(',',TK_COMMA) ONE('.',TK_DOT)
        #undef ONE

        /* operators longest first */
        const char *ops[]={"**","//","==","!=","<=",">=","&&","||","+","-","*","/","%","<",">","=","!"};
        for(size_t i=0;i<sizeof(ops)/sizeof(ops[0]);i++){
            size_t m=strlen(ops[i]);
            if(starts(p,rem,ops[i])){ t.kind=TK_OP; t.text=xstrdup(ops[i]); bump(l,m); l->tok=t; return t; }
        }

        t.kind=TK_EOF; t.text=xstrndup(p,1); bump(l,1); l->tok=t; return t;
    }
    Token t={TK_EOF,xstrdup(""),l->line,l->col}; l->tok=t; return t;
}

static void parser_error(Parser *p,const char *msg){
    if(p->failed) return;
    p->failed=1;
    snprintf(p->error,sizeof(p->error),"line %d col %d: %s (token=%s)",
             p->lx.tok.line,p->lx.tok.col,msg,p->lx.tok.text?p->lx.tok.text:"");
}
static void next(Parser *p){ if(!p->failed) lex_next(&p->lx); }
static int tok_is(Parser *p,TokenKind k){ return p->lx.tok.kind==k; }
static int text_is(Parser *p,const char *s){ return p->lx.tok.text && strcmp(p->lx.tok.text,s)==0; }
static void expect_kind(Parser *p,TokenKind k,const char *what){
    if(p->failed)return;
    if(!tok_is(p,k)){ parser_error(p,what); return; }
    next(p);
}
static char *take_ident(Parser *p){
    if(p->failed)return xstrdup("");
    if(!tok_is(p,TK_IDENT)){ parser_error(p,"expected identifier"); return xstrdup(""); }
    char *s=xstrdup(p->lx.tok.text); next(p); return s;
}

static uint32_t sym(Module *m,const char *s){
    for(uint32_t i=0;i<m->symbol_count;i++) if(strcmp(m->symbols[i],s)==0) return i;
    if(m->symbol_count==m->symbol_cap){
        m->symbol_cap=m->symbol_cap?m->symbol_cap*2:32;
        m->symbols=(char**)xrealloc(m->symbols,m->symbol_cap*sizeof(char*));
    }
    m->symbols[m->symbol_count]=xstrdup(s);
    return m->symbol_count++;
}
static int const_eq(Constant *c,Constant *d){
    if(c->type!=d->type)return 0;
    switch(c->type){
        case C_NULL:return 1;
        case C_BOOL:return c->boolean==d->boolean;
        case C_INT:return c->integer==d->integer;
        case C_FLOAT:return memcmp(&c->floating,&d->floating,sizeof(double))==0;
        case C_STR:return strcmp(c->string,d->string)==0;
    } return 0;
}
static uint32_t add_const(Module *m,Constant c){
    for(uint32_t i=0;i<m->constant_count;i++) {
        if(const_eq(&m->constants[i],&c)) {
            if(c.type==C_STR) {
                free(c.string);
            }
            return i;
        }
    }
    if(m->constant_count==m->constant_cap){
        m->constant_cap=m->constant_cap?m->constant_cap*2:32;
        m->constants=(Constant*)xrealloc(m->constants,m->constant_cap*sizeof(Constant));
    }
    m->constants[m->constant_count]=c;
    return m->constant_count++;
}
static uint32_t c_null(Module *m){ Constant c={0}; c.type=C_NULL; return add_const(m,c); }
static uint32_t c_bool(Module *m,int v){ Constant c={0}; c.type=C_BOOL;c.boolean=!!v;return add_const(m,c); }
static uint32_t c_int(Module *m,int64_t v){ Constant c={0};c.type=C_INT;c.integer=v;return add_const(m,c); }
static uint32_t c_float(Module *m,double v){ Constant c={0};c.type=C_FLOAT;c.floating=v;return add_const(m,c); }
static uint32_t c_str(Module *m,const char *s){ Constant c={0};c.type=C_STR;c.string=xstrdup(s);return add_const(m,c); }

static uint32_t emit(Code *c,uint8_t op,uint32_t a,uint16_t b){
    if(c->n==c->cap){ c->cap=c->cap?c->cap*2:32; c->v=(Instruction*)xrealloc(c->v,c->cap*sizeof(Instruction)); }
    c->v[c->n]=(Instruction){op,a,b}; return c->n++;
}
static void patch(Code *c,uint32_t at,uint32_t target){ if(at<c->n)c->v[at].a=target; }

static int precedence(const char *op){
    if(strcmp(op,"||")==0)return 1;
    if(strcmp(op,"&&")==0)return 2;
    if(strcmp(op,"==")==0||strcmp(op,"!=")==0)return 3;
    if(strcmp(op,"<")==0||strcmp(op,">")==0||strcmp(op,"<=")==0||strcmp(op,">=")==0)return 4;
    if(strcmp(op,"+")==0||strcmp(op,"-")==0)return 5;
    if(strcmp(op,"*")==0||strcmp(op,"/")==0||strcmp(op,"//")==0||strcmp(op,"%")==0)return 6;
    if(strcmp(op,"**")==0)return 7;
    return 0;
}
static uint32_t binary_sub(const char *op){
    if(strcmp(op,"+")==0) return B_ADD;
    if(strcmp(op,"-")==0) return B_SUB;
    if(strcmp(op,"*")==0) return B_MUL;
    if(strcmp(op,"/")==0) return B_DIV;
    if(strcmp(op,"//")==0) return B_FLOORDIV;
    if(strcmp(op,"%")==0) return B_MOD;
    if(strcmp(op,"**")==0) return B_POW;
    if(strcmp(op,"==")==0) return B_EQ;
    if(strcmp(op,"!=")==0) return B_NE;
    if(strcmp(op,"<")==0) return B_LT;
    if(strcmp(op,">")==0) return B_GT;
    if(strcmp(op,"<=")==0) return B_LE;
    if(strcmp(op,">=")==0) return B_GE;
    if(strcmp(op,"&&")==0) return B_AND;
    if(strcmp(op,"||")==0) return B_OR;
    return 0;
}

static void parse_expr(Parser *p,Code *code,int min_prec);

static void parse_call_after_name(Parser *p,Code *code,const char *name){
    expect_kind(p,TK_LPAREN,"expected '('");
    uint16_t argc=0;
    if(!tok_is(p,TK_RPAREN)){
        while(!p->failed){
            parse_expr(p,code,0); argc++;
            if(tok_is(p,TK_COMMA)){ next(p); continue; }
            break;
        }
    }
    expect_kind(p,TK_RPAREN,"expected ')'");
    emit(code,OP_CALL,sym(&p->mod,name),argc);
}

static void parse_primary(Parser *p,Code *code){
    if(p->failed)return;
    if(tok_is(p,TK_NUMBER)){
        char *s=xstrdup(p->lx.tok.text); next(p);
        if(strchr(s,'.')) emit(code,OP_PUSH_CONST,c_float(&p->mod,strtod(s,NULL)),0);
        else emit(code,OP_PUSH_CONST,c_int(&p->mod,strtoll(s,NULL,10)),0);
        free(s); return;
    }
    if(tok_is(p,TK_STRING)){
        char *s=xstrdup(p->lx.tok.text); next(p);
        emit(code,OP_PUSH_CONST,c_str(&p->mod,s),0); free(s); return;
    }
    if(tok_is(p,TK_IDENT)){
        char *name=take_ident(p);
        if(strcmp(name,"TRUE")==0){ emit(code,OP_PUSH_CONST,c_bool(&p->mod,1),0); free(name); return; }
        if(strcmp(name,"FALSE")==0){ emit(code,OP_PUSH_CONST,c_bool(&p->mod,0),0); free(name); return; }
        if(strcmp(name,"NULL")==0){ emit(code,OP_PUSH_CONST,c_null(&p->mod),0); free(name); return; }
        if(tok_is(p,TK_LPAREN)) parse_call_after_name(p,code,name);
        else emit(code,OP_LOAD,sym(&p->mod,name),0);
        free(name); return;
    }
    if(tok_is(p,TK_LPAREN)){
        next(p); parse_expr(p,code,0); expect_kind(p,TK_RPAREN,"expected ')'"); return;
    }
    parser_error(p,"expected expression");
}

static void parse_unary(Parser *p,Code *code){
    if(tok_is(p,TK_OP) && (text_is(p,"!")||text_is(p,"-")||text_is(p,"+"))){
        char *op=xstrdup(p->lx.tok.text); next(p); parse_unary(p,code);
        uint32_t sub=strcmp(op,"!")==0?U_NOT:(strcmp(op,"-")==0?U_NEG:U_POS);
        emit(code,OP_UNARY,sub,0); free(op); return;
    }
    parse_primary(p,code);
}

static void parse_expr(Parser *p,Code *code,int min_prec){
    parse_unary(p,code);
    while(!p->failed && tok_is(p,TK_OP)){
        int prec=precedence(p->lx.tok.text);
        if(!prec || prec<min_prec)break;
        char *op=xstrdup(p->lx.tok.text); next(p);
        int next_min=(strcmp(op,"**")==0)?prec:prec+1;
        parse_expr(p,code,next_min);
        uint32_t sub=binary_sub(op);
        if(!sub){ free(op); parser_error(p,"unknown binary operator"); return; }
        emit(code,OP_BINARY,sub,0); free(op);
    }
}

static void parse_block(Parser *p,Code *code);

static void parse_statement(Parser *p,Code *code){
    if(p->failed)return;

    if(tok_is(p,TK_DYNAMIC)){
        next(p);
        char *name=take_ident(p);
        if(tok_is(p,TK_COLON)){
            next(p); parse_expr(p,code,0); expect_kind(p,TK_SEMI,"expected ';'");
            emit(code,OP_STORE,sym(&p->mod,name),0);
        } else if(tok_is(p,TK_LPAREN)){
            parse_call_after_name(p,code,name); expect_kind(p,TK_SEMI,"expected ';'");
            emit(code,OP_POP,0,0);
        } else parser_error(p,"expected ':' or '(' after dynamic name");
        free(name); return;
    }

    if(tok_is(p,TK_STATIC)){
        next(p); char *name=take_ident(p); free(name);
        parse_block(p,code); return;
    }

    if(tok_is(p,TK_IDENT) && text_is(p,"IF")){
        next(p); expect_kind(p,TK_LPAREN,"expected '(' after IF");
        parse_expr(p,code,0); expect_kind(p,TK_RPAREN,"expected ')' after IF condition");
        uint32_t jf=emit(code,OP_JUMP_IF_FALSE,0,0);
        parse_block(p,code);
        uint32_t je=emit(code,OP_JUMP,0,0);
        patch(code,jf,code->n);
        if(tok_is(p,TK_IDENT)&&text_is(p,"ELSE")){ next(p); parse_block(p,code); }
        patch(code,je,code->n); return;
    }

    if(tok_is(p,TK_IDENT) && text_is(p,"WHILE")){
        next(p); uint32_t start=code->n;
        expect_kind(p,TK_LPAREN,"expected '(' after WHILE");
        parse_expr(p,code,0); expect_kind(p,TK_RPAREN,"expected ')' after WHILE condition");
        uint32_t jf=emit(code,OP_JUMP_IF_FALSE,0,0);
        parse_block(p,code); emit(code,OP_JUMP,start,0); patch(code,jf,code->n); return;
    }

    if(tok_is(p,TK_IDENT) && text_is(p,"RETURN")){
        next(p); parse_expr(p,code,0); expect_kind(p,TK_SEMI,"expected ';' after RETURN");
        emit(code,OP_RETURN,0,0); return;
    }

    if(tok_is(p,TK_IDENT)){
        char *name=take_ident(p);
        if(tok_is(p,TK_LPAREN)){
            parse_call_after_name(p,code,name); expect_kind(p,TK_SEMI,"expected ';'");
            emit(code,OP_POP,0,0); free(name); return;
        }
        free(name);
    }
    parser_error(p,"unsupported statement");
}

static void parse_block(Parser *p,Code *code){
    expect_kind(p,TK_LBRACE,"expected '{'");
    while(!p->failed && !tok_is(p,TK_RBRACE) && !tok_is(p,TK_EOF)) parse_statement(p,code);
    expect_kind(p,TK_RBRACE,"expected '}'");
}

static void add_function(Module *m,Function fn){
    if(m->function_count==m->function_cap){
        m->function_cap=m->function_cap?m->function_cap*2:16;
        m->functions=(Function*)xrealloc(m->functions,m->function_cap*sizeof(Function));
    }
    m->functions[m->function_count++]=fn;
}

static void parse_def(Parser *p){
    next(p); /* consume DEF */
    char *name=take_ident(p);
    Function fn={0}; fn.name_sym=sym(&p->mod,name); free(name);
    expect_kind(p,TK_LPAREN,"expected '(' after function name");
    if(!tok_is(p,TK_RPAREN)){
        while(!p->failed){
            char *param=take_ident(p);
            fn.params=(uint32_t*)xrealloc(fn.params,(fn.param_count+1)*sizeof(uint32_t));
            fn.params[fn.param_count++]=sym(&p->mod,param); free(param);
            if(tok_is(p,TK_COMMA)){next(p);continue;} break;
        }
    }
    expect_kind(p,TK_RPAREN,"expected ')' after params");
    parse_block(p,&fn.code);
    if(fn.code.n==0 || fn.code.v[fn.code.n-1].op!=OP_RETURN){
        emit(&fn.code,OP_PUSH_CONST,c_null(&p->mod),0);
        emit(&fn.code,OP_RETURN,0,0);
    }
    add_function(&p->mod,fn);
}

static void parse_command(Parser *p){
    next(p); /* ⟡ */
    expect_kind(p,TK_LPAREN,"expected '(' after ⟡");
    expect_kind(p,TK_SIGMA,"expected Σ");
    expect_kind(p,TK_DOT,"expected '.'");
    char *name=take_ident(p); free(name);
    expect_kind(p,TK_RPAREN,"expected ')' after command name");
    parse_block(p,&p->mod.main_code);
}

static int parse_module(Parser *p,const char *body){
    memset(p,0,sizeof(*p)); lexer_init(&p->lx,body); lex_next(&p->lx);
    while(!p->failed && !tok_is(p,TK_EOF)){
        if(tok_is(p,TK_IDENT)&&text_is(p,"DEF")) parse_def(p);
        else if(tok_is(p,TK_COMMAND)) parse_command(p);
        else parser_error(p,"top-level item must be DEF or ⟡ command");
    }
    if(!p->failed) emit(&p->mod.main_code,OP_HALT,0,0);
    return p->failed?1:0;
}

static void w8(FILE*f,uint8_t x){ fwrite(&x,1,1,f); }
static void w16(FILE*f,uint16_t x){ uint8_t b[2]={x&255,(x>>8)&255};fwrite(b,1,2,f); }
static void w32(FILE*f,uint32_t x){ uint8_t b[4]={x&255,(x>>8)&255,(x>>16)&255,(x>>24)&255};fwrite(b,1,4,f); }
static void w64(FILE*f,uint64_t x){ uint8_t b[8];for(int i=0;i<8;i++)b[i]=(x>>(8*i))&255;fwrite(b,1,8,f); }

static void write_code(FILE*f,Code*c){
    w32(f,c->n);
    for(uint32_t i=0;i<c->n;i++){
        Instruction in=c->v[i]; w8(f,in.op);
        if(in.op==OP_PUSH_CONST||in.op==OP_LOAD||in.op==OP_STORE||in.op==OP_JUMP||in.op==OP_JUMP_IF_FALSE) w32(f,in.a);
        else if(in.op==OP_UNARY||in.op==OP_BINARY) w8(f,(uint8_t)in.a);
        else if(in.op==OP_CALL){w32(f,in.a);w16(f,in.b);}
    }
}

static int write_module(const char *path,Module*m){
    FILE*f=fopen(path,"wb"); if(!f){perror(path);return 1;}
    fwrite("SIGMBC01",1,8,f);w16(f,1);w16(f,0);
    w32(f,m->constant_count);
    for(uint32_t i=0;i<m->constant_count;i++){
        Constant*c=&m->constants[i];
        if(c->type==C_NULL)w8(f,TAG_NULL);
        else if(c->type==C_BOOL){w8(f,TAG_BOOL);w8(f,c->boolean);}
        else if(c->type==C_INT){w8(f,TAG_INT);uint64_t u;memcpy(&u,&c->integer,8);w64(f,u);}
        else if(c->type==C_FLOAT){w8(f,TAG_FLOAT);uint64_t u;memcpy(&u,&c->floating,8);w64(f,u);}
        else if(c->type==C_STR){w8(f,TAG_STR);uint32_t n=(uint32_t)strlen(c->string);w32(f,n);fwrite(c->string,1,n,f);}
    }
    w32(f,m->symbol_count);
    for(uint32_t i=0;i<m->symbol_count;i++){uint32_t n=(uint32_t)strlen(m->symbols[i]);w32(f,n);fwrite(m->symbols[i],1,n,f);}
    w32(f,m->function_count);
    for(uint32_t i=0;i<m->function_count;i++){
        Function*fn=&m->functions[i];w32(f,fn->name_sym);w16(f,fn->param_count);
        for(uint16_t j=0;j<fn->param_count;j++)w32(f,fn->params[j]);
        write_code(f,&fn->code);
    }
    write_code(f,&m->main_code);
    fclose(f);return 0;
}

static char *read_all(const char*path,size_t*outn){
    FILE*f=fopen(path,"rb");if(!f){perror(path);return NULL;}
    fseek(f,0,SEEK_END);long n=ftell(f);rewind(f);
    char*s=(char*)xmalloc((size_t)n+1);if(fread(s,1,(size_t)n,f)!=(size_t)n){fclose(f);free(s);return NULL;}
    s[n]=0;fclose(f);if(outn)*outn=(size_t)n;return s;
}

static const char *after_header(char *src){
    char *nl=strchr(src,'\n'); if(!nl)return NULL;
    *nl=0;
    if(strncmp(src,"#SIGMAUNIVERSE_LANGUAGE[DOMAIN=",31)!=0)return NULL;
    if(!strstr(src,"][VERSION=")||src[strlen(src)-1]!=']')return NULL;
    *nl='\n'; return nl+1;
}

static void free_module(Module*m){
    for(uint32_t i=0;i<m->symbol_count;i++) {
        free(m->symbols[i]);
    }
    free(m->symbols);

    for(uint32_t i=0;i<m->constant_count;i++) {
        if(m->constants[i].type==C_STR) {
            free(m->constants[i].string);
        }
    }
    free(m->constants);

    for(uint32_t i=0;i<m->function_count;i++) {
        free(m->functions[i].params);
        free(m->functions[i].code.v);
    }
    free(m->functions);
    free(m->main_code.v);
}

int sigma_compile_file(const char *input_path,const char *output_path){
    size_t n=0;
    char*src=read_all(input_path,&n);
    (void)n;
    if(!src) return 2;

    const char*body=after_header(src);
    if(!body){
        fprintf(stderr,"sigmac: invalid/missing SIGMA header\n");
        free(src);
        return 3;
    }

    Parser p;
    if(parse_module(&p,body)){
        fprintf(stderr,"sigmac: %s\n",p.error);
        free_module(&p.mod);
        token_free(&p.lx.tok);
        free(src);
        return 4;
    }

    int rc=write_module(output_path,&p.mod);
    if(!rc) {
        printf("COMPILED %s -> %s\n",input_path,output_path);
    }

    free_module(&p.mod);
    token_free(&p.lx.tok);
    free(src);
    return rc;
}

#ifndef SIGMAC_NO_MAIN
int main(int argc,char**argv){
    if(argc<3){
        printf("SIGMA Genesis-5 native compiler\nUsage: %s input.sigma output.sigmab\n",argv[0]);
        return 0;
    }
    return sigma_compile_file(argv[1],argv[2]);
}
#endif
