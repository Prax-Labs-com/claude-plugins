---
description: Screen an address, tx hash, transfer or entity name with Prax Data Services
argument-hint: <0xaddress | 0xtxhash | "from to amount asset" | "entity name">
---
Screen $ARGUMENTS with the Prax tools and report per the prax-screening skill:
- 40-hex address → screen_wallet (chain eth unless the user said otherwise)
- 64-hex hash → analyze_transaction
- "from to amount [asset]" → screen_transfer
- anything else → screen_entity
Lead with verdict + reason, then evidence, then the recommended action.
