#!/usr/bin/env python3
"""UserPromptSubmit hook: when the prompt contains EVM addresses or tx hashes, remind the agent to screen them.
Reads the hook payload on stdin, prints a short note to stdout (added as context). Never blocks."""
import json, re, sys
try:
    p = json.load(sys.stdin)
except Exception:
    sys.exit(0)
text = str(p.get("prompt") or "")
addrs = sorted(set(re.findall(r"0x[0-9a-fA-F]{40}(?![0-9a-fA-F])", text)))
hashes = sorted(set(re.findall(r"0x[0-9a-fA-F]{64}", text)))
if not addrs and not hashes:
    sys.exit(0)
bits = []
if addrs:
    bits.append(f"{len(addrs)} EVM address(es): " + ", ".join(a[:10] + "…" for a in addrs[:5]))
if hashes:
    bits.append(f"{len(hashes)} tx hash(es)")
print("[prax-screening] The prompt contains " + "; ".join(bits) + ". Screen them with the prax tools (screen_wallet / analyze_transaction) before acting, per the prax-screening skill.")
