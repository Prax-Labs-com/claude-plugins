---
description: Find every EVM address in this repo and screen them with Prax (batch)
---
1. Collect every distinct `0x[0-9a-fA-F]{40}` in the working tree (skip node_modules, .git, build output, lockfiles). Record file:line for each.
2. Screen them with screen_wallets_batch in chunks of 50 (chain eth unless the file context says otherwise).
3. Report a table: address · where it appears · Prax band · label/story (short). Put critical/high first.
4. For anything critical: say which files reference it and ask before changing anything. For unknown contract addresses the code sends value to, recommend adding a screen_transfer pre-sign check.
