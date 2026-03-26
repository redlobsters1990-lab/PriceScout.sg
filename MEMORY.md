# MEMORY.md

## User / project preferences
- User wants a fully automated Digital Asset Farming (DAF) system inside OpenClaw that can run unattended, use minimal tokens, keep roles strictly separated, avoid duplicate work/reporting, and use Discord only for human control, executive briefs, and alerts.
- User prefers `market_intel` and `research` to remain separate: `market_intel` handles discovery; `research` handles qualification.
- User has shifted the system goal toward a Singapore comparison-page / affiliate publishing business rather than a broad generic DAF model.
- User wants all agents to maintain both short-term and long-term memory and to read their own memory before repeating prior work or handling updates.
- User prefers the workspace docs to be organized cleanly with clear file roles and reduced overlap/duplication.
- User wants the `chief_of_staff` to be the final internal decision maker for which approved opportunities become pages.

## DAF operating model
- The DAF system uses 9 core agents: `chief_of_staff`, `orchestrator`, `market_intel`, `research`, `planner`, `builder`, `publisher`, `revenue_ops`, `growth_ops`.
- Shared DAF operational state/code lives at `/Users/chozengone/.openclaw/workspace-daf-shared/daf`.
- Discord routing intent is: orchestrator for control and alerts, chief_of_staff for executive brief, no specialist-to-specialist Discord chatter.
- `trend_intel` is used as an upstream signal watcher; `market_intel` remains the executable discovery lane for DAF.

## Current workflow emphasis
- Core business model is now automated Singapore comparison-page publishing.
- The system should:
  - find high-search, low-competition buyer-intent queries
  - detect product and trend signals
  - generate structured comparison pages automatically
  - update prices, rankings, listings, and summaries over time
- Priority source classes include Shopee, Lazada, Amazon SG, Google Trends-style signals, Reddit Singapore, forums, and Facebook-style discussion signals.
- Default page pattern is like: `Best [Product] in Singapore 2026 – Compare Prices & Reviews`.
- Preferred page blocks include specs, ranking blocks, price comparison tables, review summaries, affiliate CTA buttons, optional email capture, and schema markup.
- Monetization priority is:
  1. affiliate
  2. optional lead capture
  3. background ads

## Agent memory policy
- Every agent should keep:
  - short-term memory in `memory/YYYY-MM-DD.md`
  - long-term memory in `MEMORY.md`
- Every agent should read its own memory before redoing prior work, re-checking old findings, or handling updates.
- This is intended to reduce duplicate work and let each specialist reuse its own prior decisions, fixes, and findings.

## Current implementation status
- A working local DAF core already existed in the shared DAF workspace with queues, lifecycle state, orchestrator, specialist modules, local auto-publish, and reporting artifacts.
- I updated `/Users/chozengone/.openclaw/openclaw.json` so orchestrator can route to `publisher`, `revenue_ops`, and `chief_of_staff` in addition to the previously allowed specialists.
- I added a local unattended DAF cycle runner at `/Users/chozengone/.openclaw/workspace-daf-shared/daf/automation/run_daf_cycle.py` plus contract/queue files and per-agent contract files across the workspaces.
- I added and later disabled a silent cron job `daf-local-cycle` (job id `9ee947eb-9291-4ced-bdff-0caabc566a8d`) at the user's request to stop all crons.
- I updated Mission Control to include a `DAF Ops` GUI page and richer memory visibility across the main workspace and agent workspaces.
- I updated the Mission Control board and shared DAF contracts to reflect the Singapore comparison-page / affiliate workflow.
- I added per-agent `AGENTS.md` files across the workspaces to make the memory policy explicit.
- I rewrote specialist role docs/memory seeds to replace stale generic roles with the new workflow.
- I added `workspace-daf-shared/daf/DOCS_STRUCTURE.md` to clarify the purpose of `SOUL.md`, `CONTRACT.md`, `AGENTS.md`, `MEMORY.md`, and daily memory files.
- Verified status at setup time: 5 monitored assets, 35 successful workflow runs, 5 known locally published pages.
- Added production-style product screening config (`state/product_screening_config.json`) with catalog-backed live product source (`state/live_product_catalog.json`).
- Rebuilt `research.py` with product validation, HTTPS/price enforcement, vendor preference sorting, provenance tracking, and safe fallback logic.
- Added Discord reliability layer (`automation/discord_reliable.py`) with exponential backoff retry, dead-letter queue, and automatic retry cron (disabled pending user re-enable).
- Added Singapore resilience content framing: discovery and research now support three-lens analysis (Cost Pressure, Disruption Risk, Mitigation/Preparedness) for practical Singapore consumer guidance.
- Expanded product catalog with resilience categories: air purifiers (haze), dehumidifiers, portable power stations, water filter pitchers, vacuum sealers, water storage containers.
- Fixed product screening config (`require_image_url: false`) to allow catalog-backed validation without image URLs.
- Enhanced manual market signals for resilience topics with Singapore-specific evidence URLs and trend classifications.

## Constraints / missing prerequisites
- Local unattended DAF logic exists, but all crons are currently disabled.
- Full production operation still requires external credentials/integrations where needed: production publish target, analytics/search console, affiliate systems, and lead routing destination.
- Strong ongoing automation in this new model also depends on reliable marketplace/product data extraction for prices, stock/listings, and review-summary refreshes.
