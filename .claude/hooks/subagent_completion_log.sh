#!/bin/bash
# Subagent completion logging hook
# Logs subagent execution for audit trail

# Create logs directory if it doesn't exist
mkdir -p .claude/logs

# Log completion with timestamp
TIMESTAMP=$(date "+%Y-%m-%d %H:%M:%S")
echo "[$TIMESTAMP] Subagent task completed" >> .claude/logs/subagent.log

# Display confirmation
echo ""
echo "✅ Subagent task completed successfully"
echo "   Logged to: .claude/logs/subagent.log"
echo ""

exit 0
