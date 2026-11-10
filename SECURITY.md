# Security policy

## Reporting a vulnerability

Email **security@prax-labs.com** with a description, steps to reproduce and the affected component (this repository, the MCP server at mcp.orabrain.com, or the developer portal). We acknowledge reports within two business days and keep you informed until the issue is resolved. Please do not open a public issue for security reports.

## Scope

- This repository: plugin manifests, skill, commands, hooks and examples.
- The hosted service: `https://mcp.orabrain.com/mcp` (MCP), `https://mcp.orabrain.com/v1` (REST) and the portal at `https://mcp.orabrain.com/portal/`.

## What the service does with your input

Inputs are addresses, transaction hashes and entity names. They are metered to your account and are not shared with other customers or added to any list. Authentication is OAuth 2.1 (PKCE, dynamic client registration) or an API key you create in the portal; keys can be revoked at any time. All tools are read-only and never write to a chain or to your data.

## Supported versions

Only the latest published version of the plugin and the live service are supported.
