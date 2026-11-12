---
description: Screen a bank (BIC / IBAN / ABA / LEI), an address, a tx hash, a transfer or a company / person with Prax Data Services
argument-hint: <BIC | IBAN | routing no. | LEI | 0xaddress | 0xtxhash | "from to amount asset" | "company or person">
---
Screen $ARGUMENTS with the Prax tools and report per the prax-screening skill:
- BIC (8/11 chars), IBAN, 9-digit routing number or 20-char LEI → screen_bank (pass a beneficiary name if given)
- a company or firm name with words like bank, payments, exchange, fintech, MSB → screen_entity + screen_enforcement + screen_licence
- 40-hex address → screen_wallet (chain eth unless the user said otherwise)
- 64-hex hash → analyze_transaction
- "from to amount [asset]" → screen_transfer
- anything else → screen_entity
Lead with verdict + reason, then evidence, then the recommended action.
