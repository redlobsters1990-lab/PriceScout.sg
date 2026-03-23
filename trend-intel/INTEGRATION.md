# Integration Plan

## Objective
Embed a dedicated trend intelligence pipeline into the existing multi-agent workflow without replacing the current research/market/planning roles.

## Agent responsibilities
- `trend_intel`: collect, normalize, cluster, score, forecast, persist, report
- `research`: enrich top clusters with supporting evidence and search expansion
- `market_intel`: assign commercialization and saturation signals
- `planner`: propose experiments, offers, content, or product responses
- `orchestrator`: merge outputs, prioritize, and route reports

## Data flow
1. collectors append raw signals
2. normalization extracts clean entities
3. clustering merges related concepts into trend clusters
4. scoring computes trend/forecast/confidence metrics
5. enrichment asks supporting agents to deepen only top candidates
6. reports and alerts are generated for orchestrator consumption

## Scheduling stance
Keep reporting local until destinations are approved. Do not post to Discord/other channels by default.

## Delivery recommendation
- save full reports to `data/reports/`
- let orchestrator read and summarize
- only add cron announce delivery after approval of target channel/session
