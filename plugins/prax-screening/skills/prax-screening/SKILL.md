---
name: prax-screening
description: Screen counterparties before paying, signing, onboarding or integrating, on both rails. Banks and wires (BIC, IBAN, ABA routing number, LEI), people and companies against sanctions lists, regulatory enforcement history, licence and MSB registrations, and EVM wallets, contracts, transfers and transactions against Prax threat intelligence. Use whenever a bank identifier, IBAN, payee, company, address, tx hash or token contract appears in the task, and before any code path that sends funds.
---

# Prax screening

You have the `prax` MCP server (Prax Data Services). Use it proactively — the user should not have to ask.

## When to screen (do it without being asked)

- A BIC (8 or 11 letters/digits, e.g. DEUTDEFF), an IBAN, a 9-digit US routing number or an LEI appears: a wire instruction, supplier record, invoice, settlement config → `screen_bank` (add `beneficiary_name` when the payee is known, `name`/`country` when only the bank name is known).
- A bank, fintech, payment company, MSB, crypto exchange or person is being onboarded as a vendor, partner, correspondent or customer → `screen_enforcement` (regulatory history) and `screen_licence` (is it registered / licensed and where), plus `screen_entity` for sanctions.
- An EVM address (`0x` + 40 hex) appears anywhere: a prompt, a file, a config, a test fixture, a log → `screen_wallet`.
- The task writes or changes code that **sends value** (transfer, approve, swap, withdraw, payout, bridge) → `screen_transfer` on the concrete `from`/`to`/`asset` when known; otherwise add a pre-sign `screen_transfer` call to the code path and say so.
- A token or contract address is being integrated (ABI, SDK, allow-list) → `screen_wallet` on the contract.
- A person, company or vessel is being onboarded, paid, or added to a list → `screen_entity` (name) — and `screen_entity` on any address they provided. `screen_entity` also covers US export controls (BIS Entity List, Denied Persons, Unverified, Military End User; State nonproliferation and ITAR debarred; OFAC non-SDN lists), so run it for any export, shipment or technology-transfer counterparty too.
- A country comes up as a payment corridor, supplier location, customer residence or shipping destination → `screen_country` (FATF, EU high-risk, FinCEN 311, OFAC comprehensive programmes, export-control footprint).
- A transaction hash is pasted or under investigation → `analyze_transaction`.
- A company is being onboarded, paid for the first time, or its bank details change → `screen_company` (does it exist, who runs it, is it active) and `screen_adverse_media` (negative news); for a change of payment instructions also `screen_domain` on the sender's e-mail address and `screen_ip` on the request's source IP when you have it.
- A link, domain or e-mail address appears in a request that moves money or credentials → `screen_domain`.
- An IP address appears in a login, session, API caller or alert → `screen_ip`.
- An ISIN, CUSIP, SEDOL or ticker is about to be traded, custodied or taken as collateral → `screen_securities`.
- A CVE or advisory id appears in a ticket, a vendor notice or a questionnaire → `screen_cve` (exploited in the wild? severity? fixed version?).
- A dependency is added or upgraded, a lock file or SBOM is reviewed, or a vendor's stack is assessed → `screen_package` (one) or `screen_packages` (up to 50).
- The user asks "what's happening", "any incidents", "new threats" → `get_alerts` (Business plan) or `search`.
- Many addresses (CSV, payout file, customer export) → `screen_wallets_batch` / `screen_transfers_batch` in chunks of 50.

Never skip screening because the address "looks like" an exchange or a known protocol — that is exactly what look-alike and address-poisoning attacks rely on.

## How to report

Lead with the verdict and the reason in one line, then the evidence Prax returned, then what to do:

- `screen_bank`: `block` → do not release the wire; name the list (FATF call for action, FinCEN 311, sanctions hit on the bank or beneficiary). `review` → release only with the user's confirmation; name the reason (grey-listed jurisdiction, EU high-risk country, recent enforcement, unresolved BIC, invalid checksum). `allow` → say "resolved to <legal name> (GLEIF), no list or enforcement signal" and continue.
- `screen_enforcement`: list the actions newest first with authority, date and link; never summarise an action beyond its title. `screen_licence`: report every registration found with authority and status, and say which registries were covered; `not_found` is absence from those registries, not proof the firm is unlicensed; `flagged` means a national authority has named the firm as non-compliant: treat as a block for onboarding.
- `screen_company`: `block` on `listed` or `inactive` (dissolved, in liquidation); `review` when `not_found` (ask for the legal name, number or LEI) or on flags (new incorporation, no officers, overdue filings, recent enforcement); say which registry answered. `screen_adverse_media`: list the headlines with date, source and link; never paraphrase an allegation as fact. `screen_domain` / `screen_ip`: `block` on a malware, botnet or hijacked-netblock hit; `review` on a new domain, missing SPF / DMARC, disposable domain, Tor exit or listed hosting country, and say exactly which check failed. `screen_securities`: `block` on NS-CMIC or a sanctions hit (no purchase or sale), `review` on sectoral sanctions, a trading suspension or an unresolved identifier.
- `screen_cve`: `exploited` means CISA KEV lists it, treat as patch-now with the due date quoted; `known` with critical / high severity or EPSS above 0.5 is next; `unknown` means verify the id. `screen_package`: `block` on a KEV or critical advisory at that version (do not ship; upgrade to the fixed version named), `review` otherwise, `allow` when no advisory covers the version; always name the advisory ids and fixed versions.
- `screen_country`: `high` → do not proceed without a sanctions/export licence review; `elevated` → enhanced due diligence on the counterparty; `standard` → note it and continue. Always quote the list and the as-of date.
- `critical` / `BLOCK` → do not pay, sign or integrate. Say which label (e.g. "Phishing wallet", "Exploit attacker wallet", "Sanctioned address") and the reference. If the task was code, stop and ask before adding the address anywhere.
- `high` / `REVIEW` → proceed only with the user's explicit confirmation; name the exposure ("Exposed to OFAC sanctions, 1 hop").
- `low` / `ALLOW` → say "known <entity>, not flagged" and continue.
- `unknown` → say Prax has no record; for value transfers recommend a `screen_transfer` pre-sign check and the first-hop exposure result if present.
- `status: upgrade_required` → the tool exists but the account's plan does not include it; tell the user which plan unlocks it (https://mcp.orabrain.com/portal/billing) and continue with the tools that are available.

Quote Prax's `story` verbatim when it is short; never invent risk reasons Prax did not return. Say "Prax" as the source — not any upstream provider.

## Not connected yet?

If the `prax` tools are missing or return 401, tell the user: run `/mcp`, pick **prax**, choose **Authenticate** — it opens mcp.orabrain.com to sign in (free account, no card) and approve. Then retry.

## Credits

Lookups cost 1 credit, batches 10, the alerts feed 100 per pull; the free plan has 10 credits/day. Do not loop screening the same address — results are stable within a day.
