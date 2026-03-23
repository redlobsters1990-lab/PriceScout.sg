# Cron Plan

Do not enable outbound delivery until a destination is approved.

Suggested local pipeline cadence:
- every 2h: `python -m trend_intel.cli collect`
- every 2h + 10m: `python -m trend_intel.cli normalize`
- every 6h: `python -m trend_intel.cli cluster`
- every 6h + 10m: `python -m trend_intel.cli score`
- daily 08:00: `python -m trend_intel.cli report-daily`
- every 2h + 30m: `python -m trend_intel.cli alert`

Suggested agent workflow:
1. `trend_intel` updates local report artifacts
2. `orchestrator` reads report artifacts
3. `research` enriches top candidates only
4. `market_intel` scores commercial angles on shortlisted items
5. `planner` converts validated opportunities into action plans
