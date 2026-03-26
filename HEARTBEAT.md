# HEARTBEAT.md

# Keep this file empty (or with only comments) to skip heartbeat API calls.

# Add tasks below when you want the agent to check something periodically.

# DAF Discord reliability: retry failed executive brief deliveries
- Run: python3 /Users/chozengone/.openclaw/workspace-daf-shared/daf/automation/discord_reliable.py retry-dead-letter
  Every: 4 hours
  Purpose: Retry Discord delivery failures that were queued for later
