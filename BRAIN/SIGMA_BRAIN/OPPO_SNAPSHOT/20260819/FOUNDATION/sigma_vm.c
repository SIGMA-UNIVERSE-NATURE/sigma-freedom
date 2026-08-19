/*
SIGMA Genesis-4 Native C VM
Loads and executes SIGMA-BYTECODE-BINARY ABI v1.0 (.sigmab).
*/
#define _POSIX_C_SOURCE 200112L
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <math.h>
#include <dirent.h>
#include <sys/stat.h>
#include <unistd.h>
#include <errno.h>
#include <time.h>
#include <ctype.h>

#ifdef SIGMA_EXTENDED_STDLIB
#include <curl/curl.h>
#include <openssl/evp.h>
#include <openssl/rand.h>
#include <netdb.h>
#include <arpa/inet.h>
#include <sys/socket.h>
#endif

#ifdef SIGMA_EMBED_COMPILER
int sigma_compile_file(const char *input_path,const char *output_path);
#endif

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

typedef enum { V_NULL, V_BOOL, V_INT, V_FLOAT, V_STR } ValueType;

typedef struct {
    ValueType type;
    union {
        int boolean;
        int64_t integer;
        double floating;
        char *string;
    } as;
} Value;

typedef struct {
    uint8_t op;
    uint32_t a;
    uint16_t b;
} Instruction;

typedef struct {
    uint32_t name_sym;
    uint16_t param_count;
    uint32_t *params;
    uint32_t code_count;
    Instruction *code;
} Function;

typedef struct {
    uint32_t count;
    uint32_t cap;
    uint32_t *sym;
    Value *val;
} Env;

typedef struct {
    Value *constants;
    uint32_t constant_count;
    char **symbols;
    uint32_t symbol_count;
    Function *functions;
    uint32_t function_count;
    Instruction *main_code;
    uint32_t main_count;
    Env globals;
    uint64_t steps;
    uint64_t max_steps;
} VM;

typedef struct {
    FILE *f;
    int error;
} Reader;

static uint8_t r8(Reader *r) {
    uint8_t x=0;
    if (fread(&x,1,1,r->f)!=1) r->error=1;
    return x;
}
static uint16_t r16(Reader *r) {
    uint8_t b[2]={0};
    if (fread(b,1,2,r->f)!=2) r->error=1;
    return (uint16_t)b[0] | ((uint16_t)b[1]<<8);
}
static uint32_t r32(Reader *r) {
    uint8_t b[4]={0};
    if (fread(b,1,4,r->f)!=4) r->error=1;
    return (uint32_t)b[0] | ((uint32_t)b[1]<<8) | ((uint32_t)b[2]<<16) | ((uint32_t)b[3]<<24);
}
static uint64_t r64u(Reader *r) {
    uint8_t b[8]={0};
    if (fread(b,1,8,r->f)!=8) r->error=1;
    uint64_t x=0;
    for(int i=0;i<8;i++) x |= ((uint64_t)b[i]) << (8*i);
    return x;
}
static int64_t r64i(Reader *r) {
    uint64_t u = r64u(r);
    int64_t s;
    memcpy(&s,&u,8);
    return s;
}
static double r64f(Reader *r) {
    uint64_t u = r64u(r);
    double d;
    memcpy(&d,&u,8);
    return d;
}

static Value v_null(void){ Value v; v.type=V_NULL; return v; }
static Value v_bool(int x){ Value v; v.type=V_BOOL; v.as.boolean=!!x; return v; }
static Value v_int(int64_t x){ Value v; v.type=V_INT; v.as.integer=x; return v; }
static Value v_float(double x){ Value v; v.type=V_FLOAT; v.as.floating=x; return v; }
static Value v_str(char *s){ Value v; v.type=V_STR; v.as.string=s; return v; }
static double as_double(Value v);

/* SIGMA_GENERIC_HOSTLIB_V1
   Generic substrate primitives only: containers, byte buffers, strings, files.
   No SIGMA lexer/parser/compiler logic lives here. */
typedef enum { O_LIST, O_MAP, O_BYTES } ObjType;

typedef struct {
    Value *items;
    uint32_t count;
    uint32_t cap;
} HList;

typedef struct {
    char **keys;
    Value *values;
    uint32_t count;
    uint32_t cap;
} HMap;

typedef struct {
    uint8_t *data;
    uint32_t count;
    uint32_t cap;
} HBytes;

typedef struct {
    ObjType type;
    union {
        HList list;
        HMap map;
        HBytes bytes;
    } as;
} HObject;

static HObject **g_objects = NULL;
static uint32_t g_object_count = 0;
static uint32_t g_object_cap = 0;

static void *h_alloc(size_t n) {
    void *p = malloc(n ? n : 1);
    if(!p) { fprintf(stderr,"SIGMA host: OOM\n"); exit(20); }
    return p;
}
static void *h_realloc(void *p,size_t n) {
    void *q = realloc(p,n ? n : 1);
    if(!q) { fprintf(stderr,"SIGMA host: OOM\n"); exit(20); }
    return q;
}
static char *h_strdup_n(const char *s,size_t n) {
    char *p=(char*)h_alloc(n+1);
    memcpy(p,s,n); p[n]='\0'; return p;
}
static char *h_strdup(const char *s) { return h_strdup_n(s,strlen(s)); }

static int64_t h_new_object(ObjType type) {
    if(g_object_count==g_object_cap) {
        uint32_t nc=g_object_cap ? g_object_cap*2 : 64;
        g_objects=(HObject**)h_realloc(g_objects,nc*sizeof(HObject*));
        g_object_cap=nc;
    }
    HObject *o=(HObject*)calloc(1,sizeof(HObject));
    if(!o) { fprintf(stderr,"SIGMA host: OOM\n"); exit(20); }
    o->type=type;
    g_objects[g_object_count]=o;
    g_object_count++;
    return (int64_t)g_object_count; /* handle = index + 1 */
}
static HObject *h_obj(Value v,ObjType type) {
    if(v.type!=V_INT || v.as.integer<=0 || (uint64_t)v.as.integer>g_object_count) {
        fprintf(stderr,"SIGMA host: invalid object handle\n"); exit(21);
    }
    HObject *o=g_objects[(uint32_t)v.as.integer-1];
    if(!o || o->type!=type) { fprintf(stderr,"SIGMA host: object type mismatch\n"); exit(21); }
    return o;
}
static int64_t h_int(Value v) {
    if(v.type==V_INT) return v.as.integer;
    if(v.type==V_BOOL) return v.as.boolean;
    if(v.type==V_FLOAT) return (int64_t)v.as.floating;
    fprintf(stderr,"SIGMA host: integer required\n"); exit(22);
}
static const char *h_string(Value v) {
    if(v.type!=V_STR) { fprintf(stderr,"SIGMA host: string required\n"); exit(22); }
    return v.as.string;
}
static void h_list_push(HList *l,Value v) {
    if(l->count==l->cap) {
        uint32_t nc=l->cap?l->cap*2:16;
        l->items=(Value*)h_realloc(l->items,nc*sizeof(Value)); l->cap=nc;
    }
    l->items[l->count++]=v;
}
static int h_map_find(HMap *m,const char *key) {
    for(uint32_t i=0;i<m->count;i++) if(strcmp(m->keys[i],key)==0) return (int)i;
    return -1;
}
static void h_map_set(HMap *m,const char *key,Value v) {
    int i=h_map_find(m,key);
    if(i>=0) { m->values[i]=v; return; }
    if(m->count==m->cap) {
        uint32_t nc=m->cap?m->cap*2:16;
        m->keys=(char**)h_realloc(m->keys,nc*sizeof(char*));
        m->values=(Value*)h_realloc(m->values,nc*sizeof(Value));
        m->cap=nc;
    }
    m->keys[m->count]=h_strdup(key); m->values[m->count]=v; m->count++;
}
static void h_bytes_reserve(HBytes *b,uint32_t add) {
    uint64_t need=(uint64_t)b->count+add;
    if(need>UINT32_MAX) { fprintf(stderr,"SIGMA host: byte buffer too large\n"); exit(23); }
    if(need>b->cap) {
        uint32_t nc=b->cap?b->cap:64;
        while(nc<need) nc*=2;
        b->data=(uint8_t*)h_realloc(b->data,nc); b->cap=nc;
    }
}
static void h_bytes_raw(HBytes *b,const void *p,uint32_t n) {
    h_bytes_reserve(b,n); memcpy(b->data+b->count,p,n); b->count+=n;
}
static void h_bytes_u8(HBytes *b,uint8_t x) { h_bytes_raw(b,&x,1); }
static void h_bytes_u16(HBytes *b,uint16_t x) {
    uint8_t q[2]={(uint8_t)x,(uint8_t)(x>>8)}; h_bytes_raw(b,q,2);
}
static void h_bytes_u32(HBytes *b,uint32_t x) {
    uint8_t q[4]={(uint8_t)x,(uint8_t)(x>>8),(uint8_t)(x>>16),(uint8_t)(x>>24)}; h_bytes_raw(b,q,4);
}
static void h_bytes_u64(HBytes *b,uint64_t x) {
    uint8_t q[8]; for(int i=0;i<8;i++) q[i]=(uint8_t)(x>>(8*i)); h_bytes_raw(b,q,8);
}


#ifdef SIGMA_EXTENDED_STDLIB
typedef struct { char *data; size_t size; } SigmaCurlBuf;

static size_t sigma_curl_write(void *contents,size_t size,size_t nmemb,void *userp) {
    size_t total=size*nmemb;
    SigmaCurlBuf *b=(SigmaCurlBuf*)userp;
    char *p=(char*)realloc(b->data,b->size+total+1);
    if(!p) return 0;
    b->data=p;
    memcpy(b->data+b->size,contents,total);
    b->size+=total;
    b->data[b->size]='\0';
    return total;
}

static char hex_digit(unsigned x) {
    return (char)(x<10?'0'+x:'a'+(x-10));
}

static char *hex_encode(const unsigned char *data,size_t n) {
    char *out=(char*)h_alloc(n*2+1);
    for(size_t i=0;i<n;i++) {
        out[i*2]=hex_digit(data[i]>>4);
        out[i*2+1]=hex_digit(data[i]&15);
    }
    out[n*2]='\0';
    return out;
}

static char *json_escape_string(const char *s) {
    size_t cap=strlen(s)*6+3;
    char *out=(char*)h_alloc(cap);
    size_t j=0;
    out[j++]='"';
    for(size_t i=0;s[i];i++) {
        unsigned char c=(unsigned char)s[i];
        if(c=='"' || c=='\\') {
            out[j++]='\\';
            out[j++]=(char)c;
        } else if(c=='\n') {
            out[j++]='\\'; out[j++]='n';
        } else if(c=='\r') {
            out[j++]='\\'; out[j++]='r';
        } else if(c=='\t') {
            out[j++]='\\'; out[j++]='t';
        } else if(c<32) {
            snprintf(out+j,7,"\\u%04x",(unsigned)c);
            j+=6;
        } else {
            out[j++]=(char)c;
        }
    }
    out[j++]='"';
    out[j]='\0';
    return out;
}

static Value json_encode_scalar(Value v) {
    if(v.type==V_NULL) return v_str(h_strdup("null"));
    if(v.type==V_BOOL) return v_str(h_strdup(v.as.boolean?"true":"false"));
    if(v.type==V_INT) {
        char buf[64]; snprintf(buf,sizeof(buf),"%lld",(long long)v.as.integer);
        return v_str(h_strdup(buf));
    }
    if(v.type==V_FLOAT) {
        char buf[96]; snprintf(buf,sizeof(buf),"%.17g",v.as.floating);
        return v_str(h_strdup(buf));
    }
    if(v.type==V_STR) return v_str(json_escape_string(v.as.string));
    return v_null();
}

static Value json_decode_scalar_text(const char *s) {
    while(*s && isspace((unsigned char)*s)) s++;
    if(strcmp(s,"null")==0) return v_null();
    if(strcmp(s,"true")==0) return v_bool(1);
    if(strcmp(s,"false")==0) return v_bool(0);
    if(*s=='"') {
        size_t n=strlen(s);
        if(n<2 || s[n-1]!='"') return v_null();
        char *out=(char*)h_alloc(n);
        size_t j=0;
        for(size_t i=1;i+1<n;i++) {
            if(s[i]=='\\' && i+1<n-1) {
                i++;
                if(s[i]=='n') out[j++]='\n';
                else if(s[i]=='r') out[j++]='\r';
                else if(s[i]=='t') out[j++]='\t';
                else out[j++]=s[i];
            } else out[j++]=s[i];
        }
        out[j]='\0';
        return v_str(out);
    }
    char *end=NULL;
    double d=strtod(s,&end);
    if(end && *end=='\0') {
        if(strchr(s,'.') || strchr(s,'e') || strchr(s,'E')) return v_float(d);
        return v_int(strtoll(s,NULL,10));
    }
    return v_null();
}
#endif

static Value sigma_host_call(Value *args,uint16_t argc) {
    if(argc<1 || args[0].type!=V_STR) {
        fprintf(stderr,"SIGMA host: host(op,...) requires operation string\n"); exit(24);
    }
    const char *op=args[0].as.string;
    Value a=argc>1?args[1]:v_null();
    Value b=argc>2?args[2]:v_null();
    Value c=argc>3?args[3]:v_null();

    if(strcmp(op,"value_type")==0) {
        if(argc<2) {
            fprintf(stderr,"SIGMA host: value_type expects one argument\n");
            exit(24);
        }
        return v_int((int64_t)a.type);
    }
    if(strcmp(op,"numeric_to_int")==0) {
        if(argc<2) {
            fprintf(stderr,"SIGMA host: numeric_to_int expects one argument\n");
            exit(24);
        }
        return v_int(h_int(a));
    }

    if(strcmp(op,"list_new")==0) return v_int(h_new_object(O_LIST));
    if(strcmp(op,"list_len")==0) return v_int(h_obj(a,O_LIST)->as.list.count);
    if(strcmp(op,"list_push")==0) { h_list_push(&h_obj(a,O_LIST)->as.list,b); return v_null(); }
    if(strcmp(op,"list_get")==0) {
        HList *l=&h_obj(a,O_LIST)->as.list; int64_t i=h_int(b);
        if(i<0 || (uint64_t)i>=l->count) return v_null();
        return l->items[i];
    }
    if(strcmp(op,"list_set")==0) {
        HList *l=&h_obj(a,O_LIST)->as.list; int64_t i=h_int(b);
        if(i<0 || (uint64_t)i>=l->count) { fprintf(stderr,"SIGMA host: list_set index\n"); exit(25); }
        l->items[i]=c; return v_null();
    }

    if(strcmp(op,"map_new")==0) return v_int(h_new_object(O_MAP));
    if(strcmp(op,"map_set")==0) { h_map_set(&h_obj(a,O_MAP)->as.map,h_string(b),c); return v_null(); }
    if(strcmp(op,"map_get")==0) {
        HMap *m=&h_obj(a,O_MAP)->as.map; int i=h_map_find(m,h_string(b));
        return i<0?v_null():m->values[i];
    }
    if(strcmp(op,"map_has")==0) {
        HMap *m=&h_obj(a,O_MAP)->as.map; return v_bool(h_map_find(m,h_string(b))>=0);
    }

    if(strcmp(op,"bytes_new")==0) return v_int(h_new_object(O_BYTES));
    if(strcmp(op,"bytes_len")==0) return v_int(h_obj(a,O_BYTES)->as.bytes.count);

    if(strcmp(op,"bytes_get")==0) {
        HBytes *bb=&h_obj(a,O_BYTES)->as.bytes;
        int64_t i=h_int(b);
        if(i<0 || (uint64_t)i>=bb->count) return v_int(-1);
        return v_int((int64_t)bb->data[i]);
    }

    if(strcmp(op,"read_bytes")==0) {
        const char *path=h_string(a);
        FILE *f=fopen(path,"rb");
        if(!f) return v_null();

        int64_t handle=h_new_object(O_BYTES);
        HBytes *bb=&h_obj(v_int(handle),O_BYTES)->as.bytes;

        uint8_t buf[4096];
        size_t got;
        while((got=fread(buf,1,sizeof(buf),f))>0) {
            h_bytes_raw(bb,buf,(uint32_t)got);
        }

        if(ferror(f)) {
            fclose(f);
            return v_null();
        }

        fclose(f);
        return v_int(handle);
    }
    if(strcmp(op,"bytes_slice_string")==0) {
        HBytes *bb=&h_obj(a,O_BYTES)->as.bytes;
        int64_t pos=h_int(b);
        int64_t len=h_int(c);

        if(pos<0 || len<0) return v_null();
        if((uint64_t)pos>bb->count) return v_null();
        if((uint64_t)len>((uint64_t)bb->count-(uint64_t)pos)) return v_null();

        if(len==0) return v_str(h_strdup_n("",0));

        return v_str(
            h_strdup_n(
                (const char*)bb->data + (size_t)pos,
                (size_t)len
            )
        );
    }
    if(strcmp(op,"bytes_u8")==0) { h_bytes_u8(&h_obj(a,O_BYTES)->as.bytes,(uint8_t)h_int(b)); return v_null(); }
    if(strcmp(op,"bytes_u16")==0) { h_bytes_u16(&h_obj(a,O_BYTES)->as.bytes,(uint16_t)h_int(b)); return v_null(); }
    if(strcmp(op,"bytes_u32")==0) { h_bytes_u32(&h_obj(a,O_BYTES)->as.bytes,(uint32_t)h_int(b)); return v_null(); }
    if(strcmp(op,"bytes_i64")==0) {
        int64_t x=h_int(b); uint64_t u; memcpy(&u,&x,8); h_bytes_u64(&h_obj(a,O_BYTES)->as.bytes,u); return v_null();
    }
    if(strcmp(op,"bytes_f64")==0) {
        double x=(b.type==V_FLOAT)?b.as.floating:(double)h_int(b); uint64_t u; memcpy(&u,&x,8);
        h_bytes_u64(&h_obj(a,O_BYTES)->as.bytes,u); return v_null();
    }
    if(strcmp(op,"bytes_get_f64")==0) {
        HBytes *bb=&h_obj(a,O_BYTES)->as.bytes;
        int64_t pos=h_int(b);

        if(pos<0) return v_null();
        if((uint64_t)pos>bb->count) return v_null();
        if(((uint64_t)bb->count-(uint64_t)pos)<8) return v_null();

        uint64_t u=0;
        for(int i=0;i<8;i++) {
            u |= ((uint64_t)bb->data[(uint64_t)pos+(uint64_t)i]) << (8*i);
        }

        double d;
        memcpy(&d,&u,8);
        return v_float(d);
    }
    if(strcmp(op,"bytes_raw_utf8")==0) {
        const char *s=h_string(b); h_bytes_raw(&h_obj(a,O_BYTES)->as.bytes,s,(uint32_t)strlen(s)); return v_null();
    }
    if(strcmp(op,"bytes_write")==0) {
        HBytes *bb=&h_obj(a,O_BYTES)->as.bytes; const char *path=h_string(b);
        FILE *f=fopen(path,"wb"); if(!f) return v_int(1);
        size_t wrote=fwrite(bb->data,1,bb->count,f); fclose(f);
        return v_int(wrote==bb->count?0:2);
    }

    if(strcmp(op,"read_text")==0) {
        const char *path=h_string(a); FILE *f=fopen(path,"rb"); if(!f) return v_null();
        fseek(f,0,SEEK_END); long n=ftell(f); rewind(f);
        char *s=(char*)h_alloc((size_t)n+1);
        size_t got=fread(s,1,(size_t)n,f); fclose(f); s[got]='\0'; return v_str(s);
    }
    if(strcmp(op,"str_len")==0) return v_int((int64_t)strlen(h_string(a)));
    if(strcmp(op,"str_byte")==0) {
        const char *s=h_string(a); int64_t i=h_int(b); size_t n=strlen(s);
        if(i<0 || (uint64_t)i>=n) return v_int(-1);
        return v_int((unsigned char)s[i]);
    }
    if(strcmp(op,"str_starts")==0) {
        const char *s=h_string(a); int64_t pos=h_int(b); const char *needle=h_string(c);
        size_t n=strlen(s), m=strlen(needle);
        if(pos<0 || (uint64_t)pos>n || (uint64_t)pos+m>n) return v_bool(0);
        return v_bool(memcmp(s+pos,needle,m)==0);
    }
    if(strcmp(op,"str_slice")==0) {
        const char *s=h_string(a); int64_t pos=h_int(b), len=h_int(c); size_t n=strlen(s);
        if(pos<0) {
            pos=0;
        }
        if(len<0) {
            len=0;
        }
        if((uint64_t)pos>n) pos=(int64_t)n;
        if((uint64_t)pos+(uint64_t)len>n) len=(int64_t)n-pos;
        return v_str(h_strdup_n(s+pos,(size_t)len));
    }
    if(strcmp(op,"str_find")==0) {
        const char *s=h_string(a), *needle=h_string(b); const char *p=strstr(s,needle);
        return v_int(p?(int64_t)(p-s):-1);
    }
    if(strcmp(op,"is_alpha")==0) {
        int64_t x=h_int(a); return v_bool((x>='A'&&x<='Z')||(x>='a'&&x<='z')||x=='_');
    }
    if(strcmp(op,"is_digit")==0) {
        int64_t x=h_int(a); return v_bool(x>='0'&&x<='9');
    }
    if(strcmp(op,"to_int")==0) return v_int(strtoll(h_string(a),NULL,10));
    if(strcmp(op,"to_float")==0) return v_float(strtod(h_string(a),NULL));

    if(strcmp(op,"math_sqrt")==0) {
        double x=(a.type==V_FLOAT)?a.as.floating:(double)h_int(a);
        return v_float(sqrt(x));
    }
    if(strcmp(op,"math_exp")==0) {
        double x=(a.type==V_FLOAT)?a.as.floating:(double)h_int(a);
        return v_float(exp(x));
    }
    if(strcmp(op,"math_abs")==0) {
        double x=(a.type==V_FLOAT)?a.as.floating:(double)h_int(a);
        return v_float(fabs(x));
    }

    if(strcmp(op,"pwd")==0) {
        size_t size=256;
        while(size < 65536) {
            char *buf=(char*)h_alloc(size);
            if(getcwd(buf,size)) return v_str(buf);
            free(buf);
            if(errno!=ERANGE) return v_null();
            size*=2;
        }
        return v_null();
    }
    if(strcmp(op,"file_exists")==0) {
        struct stat st;
        return v_bool(stat(h_string(a),&st)==0);
    }
    if(strcmp(op,"mkdir")==0) {
        const char *path=h_string(a);
        if(mkdir(path,0777)==0 || errno==EEXIST) return v_int(0);
        return v_int(errno?errno:1);
    }
    if(strcmp(op,"write_text")==0) {
        const char *path=h_string(a), *txt=h_string(b);
        FILE *f=fopen(path,"wb"); if(!f) return v_int(errno?errno:1);
        size_t n=strlen(txt), w=fwrite(txt,1,n,f); fclose(f);
        return v_int(w==n?0:2);
    }
    if(strcmp(op,"append_text")==0) {
        const char *path=h_string(a), *txt=h_string(b);
        FILE *f=fopen(path,"ab"); if(!f) return v_int(errno?errno:1);
        size_t n=strlen(txt), w=fwrite(txt,1,n,f); fclose(f);
        return v_int(w==n?0:2);
    }
    if(strcmp(op,"listdir")==0) {
        const char *path=h_string(a);
        DIR *d=opendir(path); if(!d) return v_null();
        int64_t handle=h_new_object(O_LIST);
        HList *l=&g_objects[(uint32_t)handle-1]->as.list;
        struct dirent *ent;
        while((ent=readdir(d))!=NULL) {
            if(strcmp(ent->d_name,".")==0 || strcmp(ent->d_name,"..")==0) continue;
            h_list_push(l,v_str(h_strdup(ent->d_name)));
        }
        closedir(d);
        return v_int(handle);
    }
    if(strcmp(op,"getenv")==0) {
        const char *x=getenv(h_string(a));
        return x?v_str(h_strdup(x)):v_null();
    }

    /* Standard Library v0.1 generic operations */

    if(strcmp(op,"math_pow")==0) {
        double x=(a.type==V_FLOAT)?a.as.floating:(double)h_int(a);
        double y=(b.type==V_FLOAT)?b.as.floating:(double)h_int(b);
        return v_float(pow(x,y));
    }
    if(strcmp(op,"math_log")==0) {
        double x=(a.type==V_FLOAT)?a.as.floating:(double)h_int(a);
        return v_float(log(x));
    }
    if(strcmp(op,"math_sin")==0) {
        double x=(a.type==V_FLOAT)?a.as.floating:(double)h_int(a);
        return v_float(sin(x));
    }
    if(strcmp(op,"math_cos")==0) {
        double x=(a.type==V_FLOAT)?a.as.floating:(double)h_int(a);
        return v_float(cos(x));
    }
    if(strcmp(op,"math_tan")==0) {
        double x=(a.type==V_FLOAT)?a.as.floating:(double)h_int(a);
        return v_float(tan(x));
    }
    if(strcmp(op,"math_floor")==0) {
        double x=(a.type==V_FLOAT)?a.as.floating:(double)h_int(a);
        return v_float(floor(x));
    }
    if(strcmp(op,"math_ceil")==0) {
        double x=(a.type==V_FLOAT)?a.as.floating:(double)h_int(a);
        return v_float(ceil(x));
    }
    if(strcmp(op,"math_round")==0) {
        double x=(a.type==V_FLOAT)?a.as.floating:(double)h_int(a);
        return v_float(round(x));
    }

    if(strcmp(op,"str_upper")==0 || strcmp(op,"str_lower")==0) {
        const char *src=h_string(a);
        char *out=h_strdup(src);
        for(size_t i=0;out[i];i++) {
            unsigned char ch=(unsigned char)out[i];
            if(strcmp(op,"str_upper")==0) out[i]=(char)toupper(ch);
            else out[i]=(char)tolower(ch);
        }
        return v_str(out);
    }
    if(strcmp(op,"str_strip")==0) {
        const char *src=h_string(a);
        size_t n=strlen(src),lo=0,hi=n;
        while(lo<hi && isspace((unsigned char)src[lo])) lo++;
        while(hi>lo && isspace((unsigned char)src[hi-1])) hi--;
        return v_str(h_strdup_n(src+lo,hi-lo));
    }
    if(strcmp(op,"str_capitalize")==0) {
        char *out=h_strdup(h_string(a));
        if(out[0]) out[0]=(char)toupper((unsigned char)out[0]);
        for(size_t i=1;out[i];i++) out[i]=(char)tolower((unsigned char)out[i]);
        return v_str(out);
    }
    if(strcmp(op,"str_title")==0) {
        char *out=h_strdup(h_string(a));
        int start_word=1;
        for(size_t i=0;out[i];i++) {
            unsigned char ch=(unsigned char)out[i];
            if(isspace(ch)) {
                start_word=1;
            } else {
                out[i]=(char)(start_word?toupper(ch):tolower(ch));
                start_word=0;
            }
        }
        return v_str(out);
    }
    if(strcmp(op,"str_contains")==0) return v_bool(strstr(h_string(a),h_string(b))!=NULL);
    if(strcmp(op,"str_ends")==0) {
        const char *s=h_string(a), *suffix=h_string(b);
        size_t n=strlen(s),m=strlen(suffix);
        return v_bool(m<=n && memcmp(s+n-m,suffix,m)==0);
    }
    if(strcmp(op,"str_replace")==0) {
        const char *src=h_string(a), *old=h_string(b), *rep=h_string(c);
        size_t oldn=strlen(old),repn=strlen(rep);
        if(oldn==0) return v_str(h_strdup(src));
        size_t count=0;
        const char *p=src;
        while((p=strstr(p,old))!=NULL) {
            count++;
            p+=oldn;
        }
        size_t srcn=strlen(src);
        size_t outn=srcn + count*(repn-oldn);
        char *out=(char*)h_alloc(outn+1);
        char *w=out;
        p=src;
        const char *q=NULL;
        while((q=strstr(p,old))!=NULL) {
            size_t k=(size_t)(q-p);
            memcpy(w,p,k);
            w+=k;
            memcpy(w,rep,repn);
            w+=repn;
            p=q+oldn;
        }
        strcpy(w,p);
        return v_str(out);
    }
    if(strcmp(op,"str_split")==0) {
        const char *src=h_string(a), *sep=h_string(b);
        size_t sepn=strlen(sep);
        int64_t handle=h_new_object(O_LIST);
        HList *l=&g_objects[(uint32_t)handle-1]->as.list;
        if(sepn==0) {
            for(size_t i=0;src[i];i++) h_list_push(l,v_str(h_strdup_n(src+i,1)));
            return v_int(handle);
        }
        const char *p=src,*q=NULL;
        while((q=strstr(p,sep))!=NULL) {
            h_list_push(l,v_str(h_strdup_n(p,(size_t)(q-p))));
            p=q+sepn;
        }
        h_list_push(l,v_str(h_strdup(p)));
        return v_int(handle);
    }
    if(strcmp(op,"str_join")==0) {
        HList *l=&h_obj(a,O_LIST)->as.list;
        const char *sep=h_string(b);
        size_t sepn=strlen(sep),total=1;
        for(uint32_t i=0;i<l->count;i++) {
            total+=strlen(h_string(l->items[i]));
            if(i) total+=sepn;
        }
        char *out=(char*)h_alloc(total);
        out[0]='\0';
        for(uint32_t i=0;i<l->count;i++) {
            if(i) strcat(out,sep);
            strcat(out,h_string(l->items[i]));
        }
        return v_str(out);
    }

    if(strcmp(op,"list_pop")==0) {
        HList *l=&h_obj(a,O_LIST)->as.list;
        if(!l->count) return v_null();
        return l->items[--l->count];
    }
    if(strcmp(op,"list_shift")==0) {
        HList *l=&h_obj(a,O_LIST)->as.list;
        if(!l->count) return v_null();
        Value out=l->items[0];
        if(l->count>1) memmove(l->items,l->items+1,(l->count-1)*sizeof(Value));
        l->count--;
        return out;
    }
    if(strcmp(op,"list_unshift")==0) {
        HList *l=&h_obj(a,O_LIST)->as.list;
        h_list_push(l,b);
        if(l->count>1) memmove(l->items+1,l->items,(l->count-1)*sizeof(Value));
        l->items[0]=b;
        return v_null();
    }
    if(strcmp(op,"list_reverse")==0) {
        HList *l=&h_obj(a,O_LIST)->as.list;
        for(uint32_t i=0;i<l->count/2;i++) {
            Value t=l->items[i];
            l->items[i]=l->items[l->count-1-i];
            l->items[l->count-1-i]=t;
        }
        return a;
    }
    if(strcmp(op,"list_slice")==0) {
        HList *l=&h_obj(a,O_LIST)->as.list;
        int64_t start=h_int(b),count=h_int(c);
        if(start<0) start=0;
        if(count<0) count=0;
        if((uint64_t)start>l->count) start=(int64_t)l->count;
        if((uint64_t)start+(uint64_t)count>l->count) count=(int64_t)l->count-start;
        int64_t handle=h_new_object(O_LIST);
        HList *o=&g_objects[(uint32_t)handle-1]->as.list;
        for(int64_t i=0;i<count;i++) h_list_push(o,l->items[start+i]);
        return v_int(handle);
    }
    if(strcmp(op,"list_sort")==0) {
        HList *l=&h_obj(a,O_LIST)->as.list;
        for(uint32_t i=0;i<l->count;i++) {
            for(uint32_t j=i+1;j<l->count;j++) {
                int do_swap=0;
                if(l->items[i].type==V_STR && l->items[j].type==V_STR)
                    do_swap=strcmp(l->items[i].as.string,l->items[j].as.string)>0;
                else
                    do_swap=as_double(l->items[i])>as_double(l->items[j]);
                if(do_swap) {
                    Value t=l->items[i];
                    l->items[i]=l->items[j];
                    l->items[j]=t;
                }
            }
        }
        return a;
    }
    if(strcmp(op,"map_delete")==0) {
        HMap *m=&h_obj(a,O_MAP)->as.map;
        int i=h_map_find(m,h_string(b));
        if(i<0) return v_bool(0);
        free(m->keys[i]);
        for(uint32_t j=(uint32_t)i+1;j<m->count;j++) {
            m->keys[j-1]=m->keys[j];
            m->values[j-1]=m->values[j];
        }
        m->count--;
        return v_bool(1);
    }
    if(strcmp(op,"map_keys")==0 || strcmp(op,"map_values")==0 || strcmp(op,"map_items")==0) {
        HMap *m=&h_obj(a,O_MAP)->as.map;
        int64_t handle=h_new_object(O_LIST);
        HList *l=&g_objects[(uint32_t)handle-1]->as.list;
        for(uint32_t i=0;i<m->count;i++) {
            if(strcmp(op,"map_keys")==0) {
                h_list_push(l,v_str(h_strdup(m->keys[i])));
            } else if(strcmp(op,"map_values")==0) {
                h_list_push(l,m->values[i]);
            } else {
                int64_t ph=h_new_object(O_LIST);
                HList *pair=&g_objects[(uint32_t)ph-1]->as.list;
                h_list_push(pair,v_str(h_strdup(m->keys[i])));
                h_list_push(pair,m->values[i]);
                h_list_push(l,v_int(ph));
            }
        }
        return v_int(handle);
    }

    if(strcmp(op,"rmdir")==0) {
        if(rmdir(h_string(a))==0) return v_int(0);
        return v_int(errno?errno:1);
    }
    if(strcmp(op,"input")==0) {
        const char *prompt=(a.type==V_STR)?a.as.string:"";
        if(prompt[0]) {
            fputs(prompt,stdout);
            fflush(stdout);
        }
        char buf[4096];
        if(!fgets(buf,sizeof(buf),stdin)) return v_null();
        size_t n=strlen(buf);
        while(n && (buf[n-1]=='\n' || buf[n-1]=='\r')) buf[--n]='\0';
        return v_str(h_strdup(buf));
    }
    if(strcmp(op,"time_now")==0) return v_int((int64_t)time(NULL));
    if(strcmp(op,"time_sleep")==0) {
        int64_t sec=h_int(a);
        if(sec<0) sec=0;
        sleep((unsigned int)sec);
        return v_null();
    }
    if(strcmp(op,"time_strftime")==0) {
        time_t t=(time_t)h_int(a);
        const char *fmt=h_string(b);
        struct tm *tmp=gmtime(&t);
        if(!tmp) return v_null();
        char buf[256];
        if(!strftime(buf,sizeof(buf),fmt,tmp)) return v_null();
        return v_str(h_strdup(buf));
    }
    if(strcmp(op,"random_int")==0) {
        static int seeded=0;
        if(!seeded) {
            srand((unsigned)time(NULL));
            seeded=1;
        }
        int64_t lo=h_int(a),hi=h_int(b);
        if(hi<lo) {
            int64_t t=lo;
            lo=hi;
            hi=t;
        }
        uint64_t span=(uint64_t)(hi-lo)+1;
        return v_int(lo+(int64_t)((uint64_t)rand()%span));
    }
    if(strcmp(op,"random_float")==0) {
        static int seeded=0;
        if(!seeded) {
            srand((unsigned)time(NULL));
            seeded=1;
        }
        return v_float((double)rand()/(double)RAND_MAX);
    }
    if(strcmp(op,"random_choice")==0) {
        HList *l=&h_obj(a,O_LIST)->as.list;
        if(!l->count) return v_null();
        return l->items[(uint32_t)rand()%l->count];
    }
    if(strcmp(op,"random_shuffle")==0) {
        HList *l=&h_obj(a,O_LIST)->as.list;
        for(uint32_t i=l->count;i>1;i--) {
            uint32_t j=(uint32_t)rand()%i;
            Value t=l->items[i-1];
            l->items[i-1]=l->items[j];
            l->items[j]=t;
        }
        return a;
    }


#ifdef SIGMA_EXTENDED_STDLIB
    if(strcmp(op,"json_encode")==0) {
        return json_encode_scalar(a);
    }
    if(strcmp(op,"json_decode")==0) {
        return json_decode_scalar_text(h_string(a));
    }
    if(strcmp(op,"json_dump")==0) {
        Value encoded=json_encode_scalar(b);
        if(encoded.type!=V_STR) return v_int(2);
        FILE *f=fopen(h_string(a),"wb");
        if(!f) return v_int(errno?errno:1);
        size_t n=strlen(encoded.as.string);
        size_t wrote=fwrite(encoded.as.string,1,n,f);
        fclose(f);
        return v_int(wrote==n?0:3);
    }
    if(strcmp(op,"json_load")==0) {
        const char *path=h_string(a);
        FILE *f=fopen(path,"rb");
        if(!f) return v_null();
        fseek(f,0,SEEK_END);
        long n=ftell(f);
        rewind(f);
        char *buf=(char*)h_alloc((size_t)n+1);
        size_t got=fread(buf,1,(size_t)n,f);
        fclose(f);
        buf[got]='\0';
        return json_decode_scalar_text(buf);
    }

    if(strcmp(op,"net_fetch")==0) {
        CURL *curl=curl_easy_init();
        if(!curl) return v_null();
        SigmaCurlBuf buf={0};
        buf.data=(char*)h_alloc(1);
        buf.data[0]='\0';
        curl_easy_setopt(curl,CURLOPT_URL,h_string(a));
        curl_easy_setopt(curl,CURLOPT_NOPROXY,"*");
        curl_easy_setopt(curl,CURLOPT_FOLLOWLOCATION,1L);
        curl_easy_setopt(curl,CURLOPT_TIMEOUT_MS,5000L);
        curl_easy_setopt(curl,CURLOPT_WRITEFUNCTION,sigma_curl_write);
        curl_easy_setopt(curl,CURLOPT_WRITEDATA,&buf);
        CURLcode rc=curl_easy_perform(curl);
        curl_easy_cleanup(curl);
        if(rc!=CURLE_OK) {
            free(buf.data);
            return v_null();
        }
        return v_str(buf.data);
    }
    if(strcmp(op,"dns_lookup")==0) {
        const char *host=h_string(a);
        struct addrinfo hints;
        memset(&hints,0,sizeof(hints));
        hints.ai_family=AF_UNSPEC;
        hints.ai_socktype=SOCK_STREAM;
        struct addrinfo *res=NULL;
        if(getaddrinfo(host,NULL,&hints,&res)!=0 || !res) return v_null();
        char out[INET6_ADDRSTRLEN];
        void *addr=NULL;
        if(res->ai_family==AF_INET) addr=&((struct sockaddr_in*)res->ai_addr)->sin_addr;
        else if(res->ai_family==AF_INET6) addr=&((struct sockaddr_in6*)res->ai_addr)->sin6_addr;
        if(!addr) {
            freeaddrinfo(res);
            return v_null();
        }
        const char *ok=inet_ntop(res->ai_family,addr,out,sizeof(out));
        freeaddrinfo(res);
        return ok?v_str(h_strdup(out)):v_null();
    }
    if(strcmp(op,"net_ping")==0) {
        const char *target=h_string(a);
        char url[2048];
        if(strstr(target,"://")) snprintf(url,sizeof(url),"%s",target);
        else snprintf(url,sizeof(url),"https://%s",target);
        CURL *curl=curl_easy_init();
        if(!curl) return v_bool(0);
        curl_easy_setopt(curl,CURLOPT_URL,url);
        curl_easy_setopt(curl,CURLOPT_NOPROXY,"*");
        curl_easy_setopt(curl,CURLOPT_NOBODY,1L);
        curl_easy_setopt(curl,CURLOPT_CONNECTTIMEOUT_MS,2500L);
        curl_easy_setopt(curl,CURLOPT_TIMEOUT_MS,4000L);
        curl_easy_setopt(curl,CURLOPT_FOLLOWLOCATION,1L);
        CURLcode rc=curl_easy_perform(curl);
        curl_easy_cleanup(curl);
        return v_bool(rc==CURLE_OK);
    }

    if(strcmp(op,"crypto_digest")==0) {
        const char *alg=h_string(a), *text=h_string(b);
        const EVP_MD *md=EVP_get_digestbyname(alg);
        if(!md) return v_null();
        EVP_MD_CTX *ctx=EVP_MD_CTX_new();
        if(!ctx) return v_null();
        unsigned char out[EVP_MAX_MD_SIZE];
        unsigned int outn=0;
        int ok=EVP_DigestInit_ex(ctx,md,NULL)==1 &&
               EVP_DigestUpdate(ctx,text,strlen(text))==1 &&
               EVP_DigestFinal_ex(ctx,out,&outn)==1;
        EVP_MD_CTX_free(ctx);
        return ok?v_str(hex_encode(out,outn)):v_null();
    }
    if(strcmp(op,"base64_encode")==0) {
        const unsigned char *src=(const unsigned char*)h_string(a);
        int n=(int)strlen((const char*)src);
        int outn=4*((n+2)/3);
        unsigned char *out=(unsigned char*)h_alloc((size_t)outn+1);
        int got=EVP_EncodeBlock(out,src,n);
        if(got<0) return v_null();
        out[got]='\0';
        return v_str((char*)out);
    }
    if(strcmp(op,"base64_decode")==0) {
        const unsigned char *src=(const unsigned char*)h_string(a);
        int n=(int)strlen((const char*)src);
        unsigned char *out=(unsigned char*)h_alloc((size_t)n+1);
        int got=EVP_DecodeBlock(out,src,n);
        if(got<0) return v_null();
        while(n>0 && src[n-1]=='=') { got--; n--; }
        out[got]='\0';
        return v_str((char*)out);
    }
    if(strcmp(op,"random_bytes")==0) {
        int64_t n=h_int(a);
        if(n<0 || n>1048576) return v_null();
        unsigned char *buf=(unsigned char*)h_alloc((size_t)n);
        if(RAND_bytes(buf,(int)n)!=1) {
            free(buf);
            return v_null();
        }
        char *hex=hex_encode(buf,(size_t)n);
        free(buf);
        return v_str(hex);
    }
    if(strcmp(op,"random_uuid")==0) {
        unsigned char b16[16];
        if(RAND_bytes(b16,16)!=1) return v_null();
        b16[6]=(unsigned char)((b16[6]&0x0f)|0x40);
        b16[8]=(unsigned char)((b16[8]&0x3f)|0x80);
        char *out=(char*)h_alloc(37);
        snprintf(out,37,
            "%02x%02x%02x%02x-%02x%02x-%02x%02x-%02x%02x-%02x%02x%02x%02x%02x%02x",
            b16[0],b16[1],b16[2],b16[3],b16[4],b16[5],b16[6],b16[7],
            b16[8],b16[9],b16[10],b16[11],b16[12],b16[13],b16[14],b16[15]);
        return v_str(out);
    }
#endif

    fprintf(stderr,"SIGMA host: unknown operation %s\\n",op);
    exit(26);
}

static int truthy(Value v) {
    switch(v.type) {
        case V_NULL: return 0;
        case V_BOOL: return v.as.boolean;
        case V_INT: return v.as.integer != 0;
        case V_FLOAT: return v.as.floating != 0.0;
        case V_STR: return v.as.string && v.as.string[0] != '\0';
    }
    return 0;
}

static double as_double(Value v) {
    if(v.type==V_INT) return (double)v.as.integer;
    if(v.type==V_FLOAT) return v.as.floating;
    if(v.type==V_BOOL) return (double)v.as.boolean;
    fprintf(stderr,"SIGMA C VM: numeric value required\n");
    exit(3);
}

static int value_equal(Value a, Value b) {
    if(a.type==V_STR && b.type==V_STR) return strcmp(a.as.string,b.as.string)==0;
    if((a.type==V_INT||a.type==V_FLOAT||a.type==V_BOOL) &&
       (b.type==V_INT||b.type==V_FLOAT||b.type==V_BOOL))
        return as_double(a)==as_double(b);
    if(a.type!=b.type) return 0;
    if(a.type==V_NULL) return 1;
    if(a.type==V_BOOL) return a.as.boolean==b.as.boolean;
    if(a.type==V_INT) return a.as.integer==b.as.integer;
    if(a.type==V_FLOAT) return a.as.floating==b.as.floating;
    return 0;
}

static void print_value(Value v) {
    switch(v.type) {
        case V_NULL: printf("NULL"); break;
        case V_BOOL: printf(v.as.boolean ? "TRUE" : "FALSE"); break;
        case V_INT: printf("%lld",(long long)v.as.integer); break;
        case V_FLOAT:
            if(floor(v.as.floating)==v.as.floating) printf("%.0f",v.as.floating);
            else printf("%.15g",v.as.floating);
            break;
        case V_STR: printf("%s",v.as.string); break;
    }
}

static void env_init(Env *e) { memset(e,0,sizeof(*e)); }
static int env_find(Env *e, uint32_t sym) {
    for(uint32_t i=0;i<e->count;i++) if(e->sym[i]==sym) return (int)i;
    return -1;
}
static void env_set(Env *e, uint32_t sym, Value v) {
    int i=env_find(e,sym);
    if(i>=0){ e->val[i]=v; return; }
    if(e->count==e->cap){
        uint32_t nc=e->cap?e->cap*2:16;
        e->sym=(uint32_t*)realloc(e->sym,nc*sizeof(uint32_t));
        e->val=(Value*)realloc(e->val,nc*sizeof(Value));
        if(!e->sym||!e->val){ fprintf(stderr,"OOM\n"); exit(2); }
        e->cap=nc;
    }
    e->sym[e->count]=sym; e->val[e->count]=v; e->count++;
}
static int env_get(Env *e, uint32_t sym, Value *out) {
    int i=env_find(e,sym);
    if(i<0) return 0;
    *out=e->val[i]; return 1;
}

static Instruction *read_code(Reader *r, uint32_t *count) {
    *count=r32(r);
    Instruction *code=(Instruction*)calloc(*count,sizeof(Instruction));
    if(!code && *count){ fprintf(stderr,"OOM\n"); exit(2); }
    for(uint32_t i=0;i<*count;i++){
        uint8_t op=r8(r); code[i].op=op;
        if(op==OP_PUSH_CONST||op==OP_LOAD||op==OP_STORE||op==OP_JUMP||op==OP_JUMP_IF_FALSE){
            code[i].a=r32(r);
        } else if(op==OP_UNARY||op==OP_BINARY){
            code[i].a=r8(r);
        } else if(op==OP_CALL){
            code[i].a=r32(r); code[i].b=r16(r);
        } else if(op==OP_POP||op==OP_RETURN||op==OP_HALT){
        } else {
            fprintf(stderr,"SIGMA C VM: unknown opcode 0x%02x in file\n",op); exit(4);
        }
    }
    return code;
}

static Function *find_function(VM *vm, uint32_t sym) {
    for(uint32_t i=0;i<vm->function_count;i++)
        if(vm->functions[i].name_sym==sym) return &vm->functions[i];
    return NULL;
}

typedef struct {
    Value *v;
    uint32_t n, cap;
} Stack;

static void stack_push(Stack *s, Value v){
    if(s->n==s->cap){
        uint32_t nc=s->cap?s->cap*2:32;
        s->v=(Value*)realloc(s->v,nc*sizeof(Value));
        if(!s->v){ fprintf(stderr,"OOM\n"); exit(2); }
        s->cap=nc;
    }
    s->v[s->n++]=v;
}
static Value stack_pop(Stack *s){
    if(!s->n){ fprintf(stderr,"SIGMA C VM: stack underflow\n"); exit(5); }
    return s->v[--s->n];
}

static Value binary_eval(uint32_t sub, Value a, Value b) {
    int numeric = (a.type==V_INT||a.type==V_FLOAT||a.type==V_BOOL) &&
                  (b.type==V_INT||b.type==V_FLOAT||b.type==V_BOOL);
    if(sub==B_ADD && a.type==V_STR && b.type==V_STR) {
        size_t na=strlen(a.as.string), nb=strlen(b.as.string);
        char *s=(char*)malloc(na+nb+1); if(!s){fprintf(stderr,"OOM\n");exit(2);}
        memcpy(s,a.as.string,na); memcpy(s+na,b.as.string,nb+1);
        return v_str(s);
    }
    if(sub==B_EQ) return v_bool(value_equal(a,b));
    if(sub==B_NE) return v_bool(!value_equal(a,b));
    if(sub==B_AND) return v_bool(truthy(a)&&truthy(b));
    if(sub==B_OR) return v_bool(truthy(a)||truthy(b));
    if(!numeric){ fprintf(stderr,"SIGMA C VM: incompatible binary operands\n"); exit(6); }

    double x=as_double(a), y=as_double(b);
    int both_int=(a.type==V_INT && b.type==V_INT);

    switch(sub){
        case B_ADD: return both_int?v_int(a.as.integer+b.as.integer):v_float(x+y);
        case B_SUB: return both_int?v_int(a.as.integer-b.as.integer):v_float(x-y);
        case B_MUL: return both_int?v_int(a.as.integer*b.as.integer):v_float(x*y);
        case B_DIV: return v_float(x/y);
        case B_FLOORDIV:
            if(both_int) return v_int((int64_t)floor((double)a.as.integer/(double)b.as.integer));
            return v_float(floor(x/y));
        case B_MOD:
            if(both_int) return v_int(a.as.integer % b.as.integer);
            return v_float(fmod(x,y));
        case B_POW:
            if(both_int && b.as.integer>=0) {
                int64_t r=1, base=a.as.integer, e=b.as.integer;
                while(e){ if(e&1)r*=base; base*=base; e>>=1; }
                return v_int(r);
            }
            return v_float(pow(x,y));
        case B_LT: return v_bool(x<y);
        case B_GT: return v_bool(x>y);
        case B_LE: return v_bool(x<=y);
        case B_GE: return v_bool(x>=y);
    }
    fprintf(stderr,"SIGMA C VM: bad binary subop 0x%x\n",sub); exit(7);
}

static Value execute(VM *vm, Instruction *code, uint32_t count, Env *locals, int is_main);

static Value call_fn(VM *vm, uint32_t sym, Value *args, uint16_t argc) {
    const char *name = sym < vm->symbol_count ? vm->symbols[sym] : "";

#ifdef SIGMA_EMBED_COMPILER
    if(strcmp(name,"compile_file")==0){
        if(argc!=2 || args[0].type!=V_STR || args[1].type!=V_STR){
            fprintf(stderr,"SIGMA selfhost: compile_file expects two strings\n");
            exit(15);
        }
        int rc=sigma_compile_file(args[0].as.string,args[1].as.string);
        return v_int(rc);
    }
#endif

    if(strcmp(name,"host")==0){
        return sigma_host_call(args,argc);
    }

    if(strcmp(name,"print")==0){
        for(uint16_t i=0;i<argc;i++){
            if(i) printf(" ");
            print_value(args[i]);
        }
        printf("\n");
        return v_null();
    }
    Function *fn=find_function(vm,sym);
    if(!fn){ fprintf(stderr,"SIGMA C VM: undefined function %s\n",name); exit(8); }
    if(fn->param_count!=argc){ fprintf(stderr,"SIGMA C VM: arg mismatch for %s\n",name); exit(8); }
    Env local; env_init(&local);
    for(uint16_t i=0;i<argc;i++) env_set(&local,fn->params[i],args[i]);
    Value ret=execute(vm,fn->code,fn->code_count,&local,0);
    free(local.sym); free(local.val);
    return ret;
}

static Value execute(VM *vm, Instruction *code, uint32_t count, Env *locals, int is_main) {
    Stack st={0};
    uint32_t ip=0;
    while(ip<count){
        if(++vm->steps>vm->max_steps){ fprintf(stderr,"SIGMA C VM: step limit\n"); exit(9); }
        Instruction in=code[ip];
        switch(in.op){
            case OP_PUSH_CONST:
                if(in.a>=vm->constant_count){fprintf(stderr,"bad const index\n");exit(10);}
                stack_push(&st,vm->constants[in.a]); break;
            case OP_POP:
                if(st.n) {
                    (void)stack_pop(&st);
                }
                break;
            case OP_LOAD: {
                Value v;
                if(env_get(locals,in.a,&v) || env_get(&vm->globals,in.a,&v)) stack_push(&st,v);
                else {fprintf(stderr,"SIGMA C VM: undefined symbol %u\n",in.a);exit(11);}
                break;
            }
            case OP_STORE: {
                Value v=stack_pop(&st);
                if(is_main) env_set(&vm->globals,in.a,v); else env_set(locals,in.a,v);
                break;
            }
            case OP_UNARY: {
                Value v=stack_pop(&st);
                if(in.a==U_NOT) stack_push(&st,v_bool(!truthy(v)));
                else if(in.a==U_NEG){
                    if(v.type==V_INT) stack_push(&st,v_int(-v.as.integer));
                    else stack_push(&st,v_float(-as_double(v)));
                } else if(in.a==U_POS) stack_push(&st,v);
                else {fprintf(stderr,"bad unary subop\n");exit(12);}
                break;
            }
            case OP_BINARY: {
                Value b=stack_pop(&st), a=stack_pop(&st);
                stack_push(&st,binary_eval(in.a,a,b)); break;
            }
            case OP_CALL: {
                uint16_t argc=in.b;
                Value *args=(Value*)calloc(argc?argc:1,sizeof(Value));
                for(int i=(int)argc-1;i>=0;i--) args[i]=stack_pop(&st);
                Value ret=call_fn(vm,in.a,args,argc);
                free(args); stack_push(&st,ret); break;
            }
            case OP_JUMP:
                if(in.a>=count){fprintf(stderr,"bad jump\n");exit(13);}
                ip=in.a; continue;
            case OP_JUMP_IF_FALSE: {
                Value c=stack_pop(&st);
                if(!truthy(c)){ if(in.a>=count){fprintf(stderr,"bad jump\n");exit(13);} ip=in.a; continue; }
                break;
            }
            case OP_RETURN: {
                Value ret=st.n?stack_pop(&st):v_null();
                free(st.v); return ret;
            }
            case OP_HALT:
                free(st.v); return v_null();
            default:
                fprintf(stderr,"unknown opcode runtime\n"); exit(14);
        }
        ip++;
    }
    free(st.v); return v_null();
}

static void free_vm(VM *vm) {
    for(uint32_t i=0;i<vm->constant_count;i++) if(vm->constants[i].type==V_STR) free(vm->constants[i].as.string);
    for(uint32_t i=0;i<vm->symbol_count;i++) free(vm->symbols[i]);
    for(uint32_t i=0;i<vm->function_count;i++){ free(vm->functions[i].params); free(vm->functions[i].code); }
    free(vm->constants); free(vm->symbols); free(vm->functions); free(vm->main_code);
    free(vm->globals.sym); free(vm->globals.val);
}

static int load_vm(const char *path, VM *vm) {
    memset(vm,0,sizeof(*vm));
    env_init(&vm->globals);
    vm->max_steps=1000000;
    {
        const char *limit=getenv("SIGMA_MAX_STEPS");
        if(limit && *limit) {
            unsigned long long parsed=strtoull(limit,NULL,10);
            if(parsed>0) {
                vm->max_steps=(uint64_t)parsed;
            }
        }
    }
    FILE *f=fopen(path,"rb");
    if(!f){ perror(path); return 1; }
    Reader r={f,0};
    char magic[8];
    if(fread(magic,1,8,f)!=8 || memcmp(magic,"SIGMBC01",8)!=0){ fprintf(stderr,"SIGMA C VM: bad magic\n"); fclose(f); return 2; }
    uint16_t major=r16(&r), minor=r16(&r);
    if(major!=1 || minor>0){ fprintf(stderr,"SIGMA C VM: unsupported ABI %u.%u\n",major,minor); fclose(f); return 3; }

    vm->constant_count=r32(&r);
    vm->constants=(Value*)calloc(vm->constant_count,sizeof(Value));
    for(uint32_t i=0;i<vm->constant_count;i++){
        uint8_t tag=r8(&r);
        if(tag==TAG_NULL) vm->constants[i]=v_null();
        else if(tag==TAG_BOOL) vm->constants[i]=v_bool(r8(&r));
        else if(tag==TAG_INT) vm->constants[i]=v_int(r64i(&r));
        else if(tag==TAG_FLOAT) vm->constants[i]=v_float(r64f(&r));
        else if(tag==TAG_STR){
            uint32_t n=r32(&r); char *s=(char*)malloc(n+1);
            if(fread(s,1,n,f)!=n){r.error=1;} s[n]='\0'; vm->constants[i]=v_str(s);
        } else {fprintf(stderr,"bad constant tag\n");fclose(f);return 4;}
    }

    vm->symbol_count=r32(&r);
    vm->symbols=(char**)calloc(vm->symbol_count,sizeof(char*));
    for(uint32_t i=0;i<vm->symbol_count;i++){
        uint32_t n=r32(&r); vm->symbols[i]=(char*)malloc(n+1);
        if(fread(vm->symbols[i],1,n,f)!=n){r.error=1;} vm->symbols[i][n]='\0';
    }

    vm->function_count=r32(&r);
    vm->functions=(Function*)calloc(vm->function_count,sizeof(Function));
    for(uint32_t i=0;i<vm->function_count;i++){
        Function *fn=&vm->functions[i];
        fn->name_sym=r32(&r); fn->param_count=r16(&r);
        fn->params=(uint32_t*)calloc(fn->param_count,sizeof(uint32_t));
        for(uint16_t j=0;j<fn->param_count;j++) fn->params[j]=r32(&r);
        fn->code=read_code(&r,&fn->code_count);
    }

    vm->main_code=read_code(&r,&vm->main_count);
    fclose(f);
    if(r.error){ fprintf(stderr,"SIGMA C VM: truncated file\n"); return 5; }
    return 0;
}

int main(int argc, char **argv) {
    if(argc<2){
        printf("SIGMA Genesis-4 C VM — ABI 1.0\nUsage: %s program.sigmab\n",argv[0]);
        return 0;
    }
    VM vm;
    int rc=load_vm(argv[1],&vm);
    if(rc) return rc;
    Env empty; env_init(&empty);
    execute(&vm,vm.main_code,vm.main_count,&empty,1);
    free(empty.sym); free(empty.val);
    free_vm(&vm);
    return 0;
}
