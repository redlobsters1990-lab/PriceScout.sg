# Trend Intelligence Integration

This folder contains the concrete scaffold for integrating a fully automated trend intelligence pipeline into the existing OpenClaw workflow.

## Existing workflow mapping
- `orchestrator`: final synthesis and control plane
- `research`: evidence validation and SERP/intent analysis
- `market_intel`: monetization and market relevance
- `planner`: turns validated trends into executable ideas
- `trend_intel`: new pipeline steward for collection, scoring, forecasting, and reports

## Build status
- agent added to OpenClaw config
- workspace created for `trend_intel`
- code scaffold created here
- no autonomous outbound delivery enabled yet

## Next operational step
Choose report destinations and alert thresholds, then schedule cron jobs against this scaffold.
