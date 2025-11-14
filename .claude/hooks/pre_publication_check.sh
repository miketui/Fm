#!/bin/bash
# Pre-tool-use hook for dangerous operations
# Blocks destructive commands and warns about editing critical EPUB files

COMMAND="$TOOL_INPUT"

# Block destructive commands
if echo "$COMMAND" | grep -qE "rm -rf|git push -f|git push --force|git reset --hard"; then
  cat <<EOF
{
  "continue": false,
  "stopReason": "Dangerous command blocked for safety",
  "systemMessage": "⚠️  BLOCKED: This command could cause data loss or break the publication workflow. Destructive operations require explicit user approval."
}
EOF
  exit 0
fi

# Warn about editing critical EPUB files
if echo "$COMMAND" | grep -qE "REBRANDED_OUTPUT/(content\.opf|mimetype|META-INF)"; then
  cat <<EOF
{
  "continue": false,
  "stopReason": "Critical EPUB file modification blocked",
  "systemMessage": "⚠️  BLOCKED: Attempting to modify critical EPUB package files (content.opf, mimetype, or META-INF/). These files should only be edited with explicit user approval and careful validation."
}
EOF
  exit 0
fi

# Warn about bulk deletions in REBRANDED_OUTPUT
if echo "$COMMAND" | grep -qE "rm.*REBRANDED_OUTPUT.*\.(xhtml|css|pdf)"; then
  cat <<EOF
{
  "continue": false,
  "stopReason": "Deletion of publication files blocked",
  "systemMessage": "⚠️  BLOCKED: Attempting to delete XHTML, CSS, or PDF files in REBRANDED_OUTPUT/. These are publication assets and should not be deleted without user approval."
}
EOF
  exit 0
fi

# All clear - continue with command
exit 0
