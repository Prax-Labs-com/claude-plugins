# prax-screening — Claude Code plugin

Wallet, transfer and sanctions screening for agents that touch money. Installs the Prax Data Services MCP server and a skill that makes Claude screen every counterparty **before** it pays, signs, onboards or integrates — without being asked.

```
/plugin marketplace add prax-labs/claude-plugins
/plugin install prax-screening@prax-labs
/mcp  →  prax  →  Authenticate        # free account on mcp.orabrain.com, no card
```

What you get
- `prax` MCP server (OAuth, no key to paste): screen_wallet, screen_transfer, screen_entity, analyze_transaction, batches, search/fetch, get_alerts.
- Skill `prax-screening`: when to screen, how to report (verdict → evidence → action), what to do on upgrade_required.
- `/screen <address|hash|transfer|name>` and `/screen-repo` (finds every address in the repo and screens them in batches).
- A prompt hook that flags addresses/hashes in your prompt so they get screened.

Terms: output is licensed for use inside your own product only — https://mcp.orabrain.com/portal/terms
