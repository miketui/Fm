#!/bin/bash

# Setup script for Mother Repository
# This script helps initialize and push the repository to GitHub

set -e  # Exit on any error

echo "=========================================="
echo "Mother Repository Setup Script"
echo "=========================================="
echo ""

# Check if we're in the right directory
if [ ! -d "REBRANDED_OUTPUT" ] || [ ! -d "OEBPS" ]; then
    echo "ERROR: This script must be run from the mother-repo directory"
    echo "Please cd to the mother-repo directory and try again"
    exit 1
fi

# Check if git is installed
if ! command -v git &> /dev/null; then
    echo "ERROR: Git is not installed"
    echo "Please install Git and try again"
    exit 1
fi

# Check if already initialized
if [ -d ".git" ]; then
    echo "Git repository already initialized"
    echo "Current remote:"
    git remote -v
    echo ""
else
    echo "Initializing Git repository..."
    git init
    echo "✓ Git repository initialized"
    echo ""
fi

# Get username for repository
echo "Please enter your GitHub username:"
read -r GITHUB_USERNAME

if [ -z "$GITHUB_USERNAME" ]; then
    echo "ERROR: GitHub username cannot be empty"
    exit 1
fi

REPO_URL="https://github.com/$GITHUB_USERNAME/mother.git"

echo ""
echo "Repository will be: $REPO_URL"
echo ""

# Check if user wants to create the repository
echo "Have you already created the 'mother' repository on GitHub? (yes/no)"
read -r REPO_EXISTS

if [ "$REPO_EXISTS" != "yes" ]; then
    echo ""
    echo "Please create the repository first using one of these methods:"
    echo ""
    echo "Method 1: GitHub CLI (if installed)"
    echo "  gh repo create mother --public"
    echo ""
    echo "Method 2: Web Browser"
    echo "  Visit https://github.com/new"
    echo "  Repository name: mother"
    echo "  Description: Production-ready EPUB files for The Artisan's Path"
    echo "  DO NOT initialize with README, .gitignore, or license"
    echo ""
    echo "After creating the repository, run this script again."
    exit 0
fi

# Add all files
echo "Adding files to Git..."
git add .
echo "✓ Files added"
echo ""

# Check if there are changes to commit
if git diff-index --quiet HEAD -- 2>/dev/null; then
    echo "No changes to commit (already committed)"
else
    # Commit
    echo "Creating initial commit..."
    git commit -m "Initial commit: Transfer REBRANDED_OUTPUT and OEBPS from miketui/Fm

This repository contains the complete production-ready EPUB files for:
The Artisan's Path: A Comprehensive Guide to Professional Hairstyling Excellence
by Michael David Warren Jr., published by Terragon Labs.

Contents:
- REBRANDED_OUTPUT: Complete EPUB 3.2 package (172 MB, 304 files)
- OEBPS: Alternative EPUB structure (11 MB, 208 files)

Total: 46 XHTML files, 44 PDFs, 31 images, 6 fonts, complete documentation"
    echo "✓ Initial commit created"
    echo ""
fi

# Set main branch
echo "Setting main branch..."
git branch -M main
echo "✓ Main branch set"
echo ""

# Check if remote already exists
if git remote | grep -q "origin"; then
    echo "Remote 'origin' already exists:"
    git remote get-url origin
    echo ""
    echo "Do you want to update it to $REPO_URL? (yes/no)"
    read -r UPDATE_REMOTE
    
    if [ "$UPDATE_REMOTE" = "yes" ]; then
        git remote set-url origin "$REPO_URL"
        echo "✓ Remote updated"
        echo ""
    fi
else
    echo "Adding remote origin..."
    git remote add origin "$REPO_URL"
    echo "✓ Remote added: $REPO_URL"
    echo ""
fi

# Ask about large files
echo "=========================================="
echo "IMPORTANT: Large File Consideration"
echo "=========================================="
echo ""
echo "This repository contains a large file:"
echo "  REBRANDED_OUTPUT/The-Artisans-Path.epub (~85 MB)"
echo ""
echo "GitHub allows files up to 100 MB, but warns about files over 50 MB."
echo ""
echo "Do you want to:"
echo "  1) Push as-is (file will be included, may show warning)"
echo "  2) Use Git LFS for large files (requires Git LFS installation)"
echo "  3) Cancel and remove large files manually"
echo ""
echo "Enter choice (1, 2, or 3):"
read -r LARGE_FILE_CHOICE

case $LARGE_FILE_CHOICE in
    1)
        echo "Pushing as-is..."
        ;;
    2)
        echo "Setting up Git LFS..."
        if command -v git-lfs &> /dev/null; then
            git lfs install
            git lfs track "*.epub"
            git lfs track "*.pdf"
            git add .gitattributes
            git commit -m "Configure Git LFS for large files"
            echo "✓ Git LFS configured"
        else
            echo "ERROR: Git LFS is not installed"
            echo "Please install Git LFS from https://git-lfs.github.com/"
            echo "Then run this script again"
            exit 1
        fi
        ;;
    3)
        echo "Cancelled. Please remove large files and run this script again."
        exit 0
        ;;
    *)
        echo "Invalid choice. Exiting."
        exit 1
        ;;
esac

echo ""
echo "=========================================="
echo "Ready to Push"
echo "=========================================="
echo ""
echo "Repository: $REPO_URL"
echo "Branch: main"
echo ""
echo "Push to GitHub now? (yes/no)"
read -r PUSH_NOW

if [ "$PUSH_NOW" = "yes" ]; then
    echo ""
    echo "Pushing to GitHub..."
    git push -u origin main
    echo ""
    echo "=========================================="
    echo "✓ SUCCESS!"
    echo "=========================================="
    echo ""
    echo "Repository pushed to: $REPO_URL"
    echo ""
    echo "Visit your repository at:"
    echo "  https://github.com/$GITHUB_USERNAME/mother"
    echo ""
    echo "Next steps:"
    echo "  1. Verify files uploaded correctly"
    echo "  2. Create a release for distribution"
    echo "  3. Share the repository URL"
    echo ""
else
    echo ""
    echo "Push cancelled. You can push manually later with:"
    echo "  git push -u origin main"
    echo ""
fi

echo "Setup complete!"
