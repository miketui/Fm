#!/bin/bash
echo "📋 Checking EPUB file structure..."

INPUT_DIR="/workspace/Fm/OEBPS/text"
EXPECTED_FILES=45

if [ ! -d "$INPUT_DIR" ]; then
    echo "❌ Input directory not found: $INPUT_DIR"
    exit 1
fi

ACTUAL_FILES=$(find "$INPUT_DIR" -name "*.xhtml" | wc -l)

echo "Expected files: $EXPECTED_FILES"
echo "Actual files: $ACTUAL_FILES"

if [ "$ACTUAL_FILES" -eq "$EXPECTED_FILES" ]; then
    echo "✅ File count matches!"
else
    echo "⚠️  File count mismatch!"
fi

echo "📝 File listing:"
find "$INPUT_DIR" -name "*.xhtml" | sort
