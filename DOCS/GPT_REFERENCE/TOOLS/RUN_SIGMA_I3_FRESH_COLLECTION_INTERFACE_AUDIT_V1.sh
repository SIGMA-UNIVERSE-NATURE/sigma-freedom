#!/data/data/com.termux/files/usr/bin/bash
set -u
set -o pipefail
umask 077

P=/data/data/com.termux/files/usr
ROOT="$HOME/SIGMA/sigma_genesis1/.sigma_exec/HH_AUTO_INTERNET_LESSONS"

SOURCE_ASSESSMENT="$ROOT/assessments/20260903T104621Z_6069_19041"
SOURCE_COLLECTION="$ROOT/runs/20260903T104006Z_18344_20745"
I2R1_RUN="$ROOT/collection_more_evidence_to_fresh_web_i2r1_runs/20260903T122751Z_18360_19557"
FRESH_COLLECTION="$ROOT/runs/20260903T122823Z_19134_21003"
CURRENT_I2R1_POINTER="$ROOT/current_collection_more_evidence_to_fresh_web_i2r1.path"

GENESIS="$HOME/SIGMA/sigma_genesis1"
SIGMAC="$GENESIS/native/sigmac"
VM="$GENESIS/native/sigma-vm.v09_candidate"

EXPECTED_SIGMAC_SHA256="65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71"
EXPECTED_VM_SHA256="029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99"

hash1() {
    "$P/bin/sha256sum" "$1" | "$P/bin/awk" '{print $1}'
}

size1() {
    "$P/bin/stat" -c '%s' "$1"
}

print_path_gate() {
    label="$1"
    path="$2"
    if [ -e "$path" ]; then
        printf '%s_EXISTS=YES\n' "$label"
        printf '%s_PATH=%s\n' "$label" "$path"
    else
        printf '%s_EXISTS=NO\n' "$label"
        printf '%s_PATH=%s\n' "$label" "$path"
    fi
}

# Content may be printed only for small control-plane files.
# Human-language/query/topic/lesson/source/payload/content artifacts are NEVER catted.
content_allowed() {
    rel="$1"
    base="${rel##*/}"

    case "$rel" in
        *lesson*|*LESSON*|*experience*|*EXPERIENCE*|*topic*|*TOPIC*|*query*|*QUERY*|\
        *reader*|*READER*|*search*|*SEARCH*|*keep*|*KEEP*|*source*|*SOURCE*|\
        *payload*|*PAYLOAD*|*content*|*CONTENT*|*text*|*TEXT*|*raw*|*RAW*|\
        *knowledge*|*KNOWLEDGE*|*candidate*|*CANDIDATE*|*extract*|*EXTRACT*|\
        *paragraph*|*PARAGRAPH*|*document*|*DOCUMENT*|*html*|*HTML*|*xml*|*XML*|\
        *json*|*JSON*|*body*|*BODY*|*title*|*TITLE*|*summary*|*SUMMARY*|\
        *answer*|*ANSWER*)
            return 1
            ;;
    esac

    case "$base" in
        *.state|*.metrics|*.metric|*.count|*.rc|*.status|*.path|*.pointer|\
        *.sha256|*.hash|state|metrics|metric|count|rc|status|pointer)
            return 0
            ;;
    esac

    return 1
}

audit_dir() {
    label="$1"
    dir="$2"

    printf '\n=== %s ===\n' "$label"

    if [ ! -d "$dir" ]; then
        printf '%s_AUDIT=HOLD_DIRECTORY_MISSING\n' "$label"
        return 1
    fi

    printf '%s_AUDIT=BEGIN\n' "$label"

    # Exact directory listing only. No file content is used to choose what SIGMA should do.
    "$P/bin/find" "$dir" -maxdepth 2 -type d -print \
      | "$P/bin/sort" \
      | while IFS= read -r d; do
            rel="${d#"$dir"}"
            [ -n "$rel" ] || rel="/"
            printf 'DIR=%s\n' "$rel"
        done

    "$P/bin/find" "$dir" -maxdepth 2 -type f -print \
      | "$P/bin/sort" \
      | while IFS= read -r f; do
            rel="${f#"$dir"/}"
            sz=$(size1 "$f")
            sha=$(hash1 "$f")
            printf 'FILE=%s\tBYTES=%s\tSHA256=%s\n' "$rel" "$sz" "$sha"

            if [ "$sz" -le 4096 ] && content_allowed "$rel"; then
                printf 'CONTROL_FILE_CONTENT_BEGIN=%s\n' "$rel"
                "$P/bin/cat" "$f"
                printf '\nCONTROL_FILE_CONTENT_END=%s\n' "$rel"
            fi
        done

    printf '%s_AUDIT=END\n' "$label"
    return 0
}

printf 'REPORT=SIGMA_I3_FRESH_COLLECTION_INTERFACE_AUDIT_V1\n'
printf 'PURPOSE=MECHANICAL_INTERFACE_DISCOVERY_ONLY\n'
printf 'SIGMA_VM_EXECUTED=NO\n'
printf 'LIVE_INTERNET_REQUEST_EXECUTED=NO\n'
printf 'HOST_SEMANTIC_OUTCOME_CLASSIFICATION=NO\n'
printf 'HOST_SEMANTIC_EVIDENCE_SELECTION=NO\n'
printf 'LESSON_TEXT_READ_BY_AUDIT=NO\n'
printf 'QUERY_OR_TOPIC_TEXT_READ_BY_AUDIT=NO\n'
printf 'FRESH_COLLECTION_OUTCOME_DECISION_MADE_BY_AUDIT=NO\n'
printf 'I3_NATIVE_DECISION_IMPLEMENTED_BY_AUDIT=NO\n'

if [ -x "$SIGMAC" ]; then
    SIGMAC_SHA256=$(hash1 "$SIGMAC")
    printf 'SIGMAC_SHA256=%s\n' "$SIGMAC_SHA256"
    if [ "$SIGMAC_SHA256" = "$EXPECTED_SIGMAC_SHA256" ]; then
        printf 'SIGMAC_IDENTITY=PASS\n'
    else
        printf 'SIGMAC_IDENTITY=HOLD_MISMATCH\n'
    fi
else
    printf 'SIGMAC_IDENTITY=HOLD_MISSING\n'
fi

if [ -x "$VM" ]; then
    VM_SHA256=$(hash1 "$VM")
    printf 'VM_SHA256=%s\n' "$VM_SHA256"
    if [ "$VM_SHA256" = "$EXPECTED_VM_SHA256" ]; then
        printf 'VM_IDENTITY=PASS\n'
    else
        printf 'VM_IDENTITY=HOLD_MISMATCH\n'
    fi
else
    printf 'VM_IDENTITY=HOLD_MISSING\n'
fi

print_path_gate SOURCE_ASSESSMENT "$SOURCE_ASSESSMENT"
print_path_gate SOURCE_COLLECTION "$SOURCE_COLLECTION"
print_path_gate I2R1_RUN "$I2R1_RUN"
print_path_gate FRESH_COLLECTION "$FRESH_COLLECTION"
print_path_gate CURRENT_I2R1_POINTER "$CURRENT_I2R1_POINTER"

if [ -f "$CURRENT_I2R1_POINTER" ]; then
    PTR_BYTES=$(size1 "$CURRENT_I2R1_POINTER")
    PTR_SHA=$(hash1 "$CURRENT_I2R1_POINTER")
    printf 'CURRENT_I2R1_POINTER_BYTES=%s\n' "$PTR_BYTES"
    printf 'CURRENT_I2R1_POINTER_SHA256=%s\n' "$PTR_SHA"
    if [ "$PTR_BYTES" -le 4096 ]; then
        printf 'CURRENT_I2R1_POINTER_CONTENT_BEGIN\n'
        "$P/bin/cat" "$CURRENT_I2R1_POINTER"
        printf '\nCURRENT_I2R1_POINTER_CONTENT_END\n'
    fi
fi

audit_dir SOURCE_ASSESSMENT_INTERFACE "$SOURCE_ASSESSMENT"
audit_dir I2R1_RUN_INTERFACE "$I2R1_RUN"
audit_dir FRESH_COLLECTION_INTERFACE "$FRESH_COLLECTION"

printf '\nREPORT_COMPLETE=YES\n'
printf 'NEXT_STAGE=I3_NATIVE_POST_FOLLOWUP_OUTCOME_EVALUATION_AND_CONTINUATION\n'
printf 'NEXT_IMPLEMENTATION_REQUIRES=USE_ONLY_DISCOVERED_MECHANICAL_INTERFACE_AND_NATIVE_SIGMA_DECISION_LOGIC\n'
printf 'DO_NOT_RERUN_I2R1_WITHOUT_NEW_ROOT_CAUSE=YES\n'
