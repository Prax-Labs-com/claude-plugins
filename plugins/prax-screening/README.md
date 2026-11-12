# prax-screening — Claude Code plugin

Counterparty screening for agents that touch money, on both rails: banks and wires (BIC / IBAN / ABA / LEI), sanctions, enforcement history, licence checks, wallets and transfers. Installs the Prax Data Services MCP server and a skill that makes Claude screen every counterparty **before** it pays, signs, onboards or integrates — without being asked.

```
/plugin marketplace add Prax-Labs-com/claude-plugins
/plugin install prax-screening@prax-labs
/mcp  →  prax  →  Authenticate        # free account on mcp.orabrain.com, no card
```

What you get
- `prax` MCP server (OAuth, no key to paste): screen_bank, screen_entity, screen_enforcement, screen_licence, screen_wallet, screen_transfer, analyze_transaction, batches, search/fetch, get_alerts.
- Skill `prax-screening`: when to screen, how to report (verdict → evidence → action), what to do on upgrade_required.
- `/screen <BIC|IBAN|routing no.|LEI|address|hash|transfer|name>` and `/screen-repo` (finds every address in the repo and screens them in batches).

Terms: output is licensed for use inside your own product only — https://mcp.orabrain.com/portal/terms
