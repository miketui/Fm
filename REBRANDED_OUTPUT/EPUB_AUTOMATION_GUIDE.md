# EPUB Automation System Guide
## Skills, Subagents, and Hooks for Error-Free EPUB Production

**Version:** 1.0
**Last Updated:** November 14, 2025
**Purpose:** Complete automation system for preparing HTML/XHTML files for error-free EPUB distribution

---

## 📚 Table of Contents

1. [Overview](#overview)
2. [System Architecture](#system-architecture)
3. [Installation & Setup](#installation--setup)
4. [Claude Code Skills (Slash Commands)](#claude-code-skills-slash-commands)
5. [Subagent Scripts](#subagent-scripts)
6. [Hooks](#hooks)
7. [Complete Workflow](#complete-workflow)
8. [Troubleshooting](#troubleshooting)
9. [Best Practices](#best-practices)

---

## Overview

This automation system provides a comprehensive set of tools, commands, and workflows to ensure your XHTML files are properly validated, formatted, and packaged for EPUB distribution with zero errors.

### What's Included

- **3 Claude Code Skills** - Slash commands for common EPUB tasks
- **4 Subagent Scripts** - Automated validation and building scripts
- **2 Hooks** - Session start and pre-commit validation hooks
- **Complete Documentation** - This guide and inline documentation

### Key Features

✅ **Automated XHTML Validation** - Validates all XHTML files for proper structure
✅ **EPUB Package Verification** - Ensures EPUB structure meets specifications
✅ **Content Integrity Checking** - Verifies all assets and references
✅ **One-Command Building** - Build production-ready EPUBs instantly
✅ **Pre-Commit Validation** - Prevents committing invalid XHTML
✅ **Session Start Setup** - Auto-checks environment on session start

---

## System Architecture

```
REBRANDED_OUTPUT/
├── .claude/
│   ├── commands/                    # Claude Code Skills
│   │   ├── epub-validate.md        # Validation skill
│   │   ├── epub-build.md           # Build skill
│   │   └── epub-prepare.md         # Full workflow skill
│   └── hooks/                       # Automation Hooks
│       ├── session-start.sh        # Runs on session start
│       └── pre-commit.sh           # Runs before git commit
│
├── scripts/
│   └── subagents/                   # Automation Scripts
│       ├── validate-xhtml.sh       # XHTML validator
│       ├── validate-epub-package.sh # Package validator
│       ├── check-content-integrity.sh # Content checker
│       └── build-epub.sh           # EPUB builder
│
├── xhtml/                           # XHTML content files
├── images/                          # Image assets
├── fonts/                           # Font files
├── styles/                          # CSS stylesheets
├── META-INF/                        # EPUB metadata
├── content.opf                      # EPUB package document
├── mimetype                         # EPUB mimetype
└── The-Artisans-Path.epub          # Built EPUB (generated)
```

---

## Installation & Setup

### Prerequisites

1. **Required Tools:**
   - `bash` (shell interpreter)
   - `zip` (EPUB packaging)
   - `git` (version control, for hooks)

2. **Recommended Tools:**
   - `xmllint` (enhanced XHTML validation) - Install: `apt-get install libxml2-utils`
   - `java` + `epubcheck.jar` (final EPUB validation)

3. **Claude Code:**
   - This system is designed for use with Claude Code CLI
   - Skills are invoked using slash commands (e.g., `/epub-validate`)

### Setup Steps

1. **Navigate to REBRANDED_OUTPUT directory:**
   ```bash
   cd /path/to/REBRANDED_OUTPUT
   ```

2. **Verify directory structure:**
   ```bash
   ls -la
   # Should show: xhtml/, images/, fonts/, styles/, META-INF/, etc.
   ```

3. **Make scripts executable (already done if using this system):**
   ```bash
   chmod +x scripts/subagents/*.sh
   chmod +x .claude/hooks/*.sh
   ```

4. **Test installation:**
   ```bash
   # Run session start hook manually
   ./.claude/hooks/session-start.sh
   ```

### Git Integration (Optional)

To enable pre-commit validation:

```bash
# Link pre-commit hook to git
ln -s ../../REBRANDED_OUTPUT/.claude/hooks/pre-commit.sh ../.git/hooks/pre-commit
chmod +x ../.git/hooks/pre-commit
```

---

## Claude Code Skills (Slash Commands)

Skills are invoked in Claude Code using slash commands.

### `/epub-validate` - Validate EPUB Files

**Purpose:** Thoroughly validate all XHTML files and EPUB package structure

**What it does:**
1. Validates XHTML structure and syntax
2. Checks EPUB package (content.opf, container.xml)
3. Verifies all asset references
4. Checks standards compliance
5. Generates validation report

**Usage:**
```
/epub-validate
```

**Output:** Detailed validation report with errors, warnings, and recommendations

---

### `/epub-build` - Build EPUB File

**Purpose:** Build production-ready EPUB file from source files

**What it does:**
1. Pre-build validation checks
2. Creates EPUB package with proper structure
3. Adds mimetype (uncompressed, first)
4. Packages all content and assets
5. Post-build verification

**Usage:**
```
/epub-build
```

**Output:** Built EPUB file: `The-Artisans-Path.epub`

---

### `/epub-prepare` - Complete Preparation Workflow

**Purpose:** Run complete end-to-end EPUB preparation workflow

**What it does:**
1. **Phase 1:** Pre-flight checks
2. **Phase 2:** XHTML formatting & linting
3. **Phase 3:** Content verification
4. **Phase 4:** Package validation
5. **Phase 5:** Standards compliance checking
6. **Phase 6:** Build & final validation

**Usage:**
```
/epub-prepare
```

**Output:** Comprehensive preparation report and production-ready EPUB

**When to use:** Before publishing or distributing your EPUB

---

## Subagent Scripts

Subagent scripts are standalone bash scripts that can be run directly or invoked by skills.

### validate-xhtml.sh

**Purpose:** Validate all XHTML files for proper structure and syntax

**Features:**
- XML well-formedness checking
- DOCTYPE validation
- Namespace verification
- Common issue detection (unclosed tags, missing alt attributes)
- Character encoding checks

**Usage:**
```bash
./scripts/subagents/validate-xhtml.sh
```

**Output:** Validation summary with file-by-file results

---

### validate-epub-package.sh

**Purpose:** Validate EPUB package structure and metadata

**Features:**
- Mimetype validation
- container.xml verification
- content.opf validation
- Manifest and spine checking
- Navigation document validation
- File existence verification

**Usage:**
```bash
./scripts/subagents/validate-epub-package.sh
```

**Output:** Package validation report with errors and warnings

---

### check-content-integrity.sh

**Purpose:** Verify content integrity and asset references

**Features:**
- File count verification
- Chapter presence checking
- Frontmatter/backmatter verification
- Image reference validation
- CSS reference checking
- Internal link validation

**Usage:**
```bash
./scripts/subagents/check-content-integrity.sh
```

**Output:** Integrity report with broken references and missing files

---

### build-epub.sh

**Purpose:** Build production-ready EPUB file

**Features:**
- Pre-build validation
- Proper EPUB structure (mimetype first, uncompressed)
- Sequential packaging of all content
- Post-build verification
- Detailed build report

**Usage:**
```bash
./scripts/subagents/build-epub.sh
```

**Output:** `The-Artisans-Path.epub` file + build report

---

## Hooks

Hooks are scripts that run automatically in response to events.

### session-start.sh

**Triggers:** When Claude Code session starts in REBRANDED_OUTPUT directory

**Purpose:** Verify environment and display available commands

**What it does:**
1. Checks directory structure
2. Verifies required files
3. Tests validation tools availability
4. Displays available commands
5. Shows quick status

**Output:** Environment status report and available commands

**Configuration:** Runs automatically when session starts

---

### pre-commit.sh

**Triggers:** Before git commit (when integrated with git hooks)

**Purpose:** Validate XHTML files before allowing commits

**What it does:**
1. Gets list of staged XHTML files
2. Validates each file's XML structure
3. Checks DOCTYPE and namespaces
4. Looks for common issues
5. Blocks commit if errors found

**Output:** Validation results, blocks commit on errors

**Configuration:**
```bash
# Link to git hooks
ln -s ../../REBRANDED_OUTPUT/.claude/hooks/pre-commit.sh ../.git/hooks/pre-commit
```

---

## Complete Workflow

### Quick Start Workflow

For a complete EPUB preparation from start to finish:

```bash
# 1. Start Claude Code session (session-start hook runs automatically)
claude-code

# 2. Run complete preparation workflow
/epub-prepare

# 3. Built EPUB is ready at: The-Artisans-Path.epub
```

### Manual Workflow

For step-by-step manual control:

```bash
# 1. Validate XHTML files
./scripts/subagents/validate-xhtml.sh

# 2. Validate EPUB package
./scripts/subagents/validate-epub-package.sh

# 3. Check content integrity
./scripts/subagents/check-content-integrity.sh

# 4. Build EPUB
./scripts/subagents/build-epub.sh

# 5. (Optional) Validate with epubcheck
java -jar ../epubcheck/epubcheck.jar The-Artisans-Path.epub
```

### Claude Code Workflow

Using Claude Code skills:

```bash
# 1. Validate everything
/epub-validate

# 2. If validation passes, build EPUB
/epub-build

# Or run complete workflow:
/epub-prepare
```

### Development Workflow

When editing XHTML files:

```bash
# 1. Edit XHTML files
vim xhtml/chapter-i.xhtml

# 2. Test changes manually
./scripts/subagents/validate-xhtml.sh

# 3. Commit (pre-commit hook runs automatically)
git add xhtml/chapter-i.xhtml
git commit -m "Update chapter i content"
# -> Pre-commit validation runs automatically

# 4. Rebuild EPUB
./scripts/subagents/build-epub.sh
```

---

## Troubleshooting

### Common Issues

#### Issue: "xmllint not found"

**Solution:**
```bash
# Ubuntu/Debian
sudo apt-get install libxml2-utils

# macOS
brew install libxml2

# Or continue without xmllint (basic validation still works)
```

#### Issue: "zip not found"

**Solution:**
```bash
# Ubuntu/Debian
sudo apt-get install zip

# macOS
brew install zip
```

#### Issue: "XHTML validation fails with syntax errors"

**Solution:**
1. Run `./scripts/subagents/validate-xhtml.sh` to see specific errors
2. Use xmllint to see detailed errors: `xmllint --noout file.xhtml`
3. Common fixes:
   - Close all tags properly: `<br/>` not `<br>`
   - Add missing namespaces
   - Fix DOCTYPE declaration
   - Escape special characters in content

#### Issue: "Image references broken"

**Solution:**
1. Run `./scripts/subagents/check-content-integrity.sh`
2. Verify images exist in `images/` directory
3. Check image paths in XHTML files match actual filenames
4. Ensure paths are relative (e.g., `../images/foo.jpg` from xhtml/)

#### Issue: "EPUB won't open in reader"

**Solution:**
1. Validate with epubcheck: `java -jar epubcheck.jar file.epub`
2. Check mimetype is first in archive: `unzip -l file.epub | head`
3. Rebuild EPUB with proper structure: `./scripts/subagents/build-epub.sh`

#### Issue: "Pre-commit hook not running"

**Solution:**
```bash
# Link the hook
cd /path/to/repo/.git/hooks
ln -sf ../../REBRANDED_OUTPUT/.claude/hooks/pre-commit.sh pre-commit
chmod +x pre-commit

# Test it
cd /path/to/repo
git commit --dry-run
```

---

## Best Practices

### Before Making Changes

1. ✅ Run `/epub-validate` to ensure current state is valid
2. ✅ Create a backup: `cp -r xhtml xhtml.backup`
3. ✅ Work on one file at a time

### While Editing XHTML

1. ✅ Always close tags properly (`<br/>`, `<img/>`, etc.)
2. ✅ Include alt attributes on all images
3. ✅ Use semantic HTML5 elements
4. ✅ Maintain proper heading hierarchy (h1 → h2 → h3)
5. ✅ Validate frequently during editing

### Before Committing

1. ✅ Run `./scripts/subagents/validate-xhtml.sh` manually
2. ✅ Fix all errors before committing
3. ✅ Pre-commit hook will catch issues, but manual check is faster

### Before Building

1. ✅ Run `/epub-validate` or complete validation
2. ✅ Fix all errors and warnings
3. ✅ Check content integrity
4. ✅ Verify all assets are present

### Before Publishing

1. ✅ Run `/epub-prepare` for complete workflow
2. ✅ Validate built EPUB with epubcheck
3. ✅ Test in multiple readers (Calibre, Apple Books, etc.)
4. ✅ Check on different devices if possible
5. ✅ Archive source files and built EPUB

### Maintenance

1. ✅ Keep epubcheck updated
2. ✅ Periodically re-validate entire EPUB
3. ✅ Back up validated versions
4. ✅ Document any custom modifications

---

## File Reference

### Skills (Slash Commands)

| File | Purpose | Usage |
|------|---------|-------|
| `.claude/commands/epub-validate.md` | XHTML & package validation | `/epub-validate` |
| `.claude/commands/epub-build.md` | Build EPUB file | `/epub-build` |
| `.claude/commands/epub-prepare.md` | Complete workflow | `/epub-prepare` |

### Subagent Scripts

| File | Purpose | Usage |
|------|---------|-------|
| `scripts/subagents/validate-xhtml.sh` | XHTML validation | `./scripts/subagents/validate-xhtml.sh` |
| `scripts/subagents/validate-epub-package.sh` | Package validation | `./scripts/subagents/validate-epub-package.sh` |
| `scripts/subagents/check-content-integrity.sh` | Content checking | `./scripts/subagents/check-content-integrity.sh` |
| `scripts/subagents/build-epub.sh` | EPUB building | `./scripts/subagents/build-epub.sh` |

### Hooks

| File | Trigger | Purpose |
|------|---------|---------|
| `.claude/hooks/session-start.sh` | Session start | Environment check |
| `.claude/hooks/pre-commit.sh` | Before commit | XHTML validation |

---

## Support & Resources

### EPUB Specifications

- EPUB 3.0: https://www.w3.org/publishing/epub3/
- IDPF: http://idpf.org/epub

### Validation Tools

- epubcheck: https://github.com/w3c/epubcheck
- W3C Validator: https://validator.w3.org/

### Documentation

- This guide: `EPUB_AUTOMATION_GUIDE.md`
- Main README: `README.md`
- Completion report: `COMPLETION_REPORT.md`

---

## Quick Reference Card

```
┌─────────────────────────────────────────────────────────────┐
│                 EPUB AUTOMATION QUICK REFERENCE             │
├─────────────────────────────────────────────────────────────┤
│ CLAUDE CODE SKILLS (use in Claude Code)                    │
│   /epub-validate   - Validate XHTML & package              │
│   /epub-build      - Build EPUB file                       │
│   /epub-prepare    - Complete preparation workflow         │
├─────────────────────────────────────────────────────────────┤
│ SUBAGENT SCRIPTS (run from command line)                   │
│   ./scripts/subagents/validate-xhtml.sh                    │
│   ./scripts/subagents/validate-epub-package.sh             │
│   ./scripts/subagents/check-content-integrity.sh           │
│   ./scripts/subagents/build-epub.sh                        │
├─────────────────────────────────────────────────────────────┤
│ HOOKS (run automatically)                                   │
│   session-start.sh - On session start                      │
│   pre-commit.sh    - Before git commit                     │
├─────────────────────────────────────────────────────────────┤
│ QUICK WORKFLOW                                              │
│   1. /epub-validate                                         │
│   2. Fix any errors                                         │
│   3. /epub-build                                            │
│   4. Test EPUB in readers                                   │
└─────────────────────────────────────────────────────────────┘
```

---

## Version History

- **v1.0** (Nov 14, 2025) - Initial release
  - 3 Claude Code skills
  - 4 subagent scripts
  - 2 automation hooks
  - Complete documentation

---

## License & Copyright

Copyright © 2025 Michael David Warren Jr.
Automation system by Terry, Terragon Labs

This automation system is provided as-is for use with The Artisan's Path EPUB production.

---

**🚀 Ready to build error-free EPUBs!**

For questions or issues, refer to the troubleshooting section or consult the inline documentation in each script.
