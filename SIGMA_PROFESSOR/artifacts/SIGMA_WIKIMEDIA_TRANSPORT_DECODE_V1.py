#!/usr/bin/env python3
"""
SIGMA Wikimedia transport decoder V1.

MECHANICAL TRANSPORT DECODE ONLY:
- Reads MediaWiki Action API JSON.
- Emits every non-empty query.pages[].extract string in response order.
- Does not summarize, rank, score, select lessons, generate candidates,
  infer meaning, or modify SIGMA learning state.
"""
import json
import sys

def main():
    if len(sys.argv) != 3:
        print("usage: decoder input.json output.txt", file=sys.stderr)
        return 2

    src, dst = sys.argv[1], sys.argv[2]

    with open(src, "r", encoding="utf-8") as f:
        obj = json.load(f)

    pages = obj.get("query", {}).get("pages", [])
    extracts = []

    if isinstance(pages, list):
        for page in pages:
            if not isinstance(page, dict):
                continue
            text = page.get("extract")
            if isinstance(text, str):
                text = text.replace("\r\n", "\n").replace("\r", "\n").strip()
                if text:
                    extracts.append(text)

    payload = "\n\n".join(extracts).strip()

    with open(dst, "w", encoding="utf-8", newline="\n") as f:
        if payload:
            f.write(payload)
            f.write("\n")

    return 0 if payload else 3

if __name__ == "__main__":
    raise SystemExit(main())
