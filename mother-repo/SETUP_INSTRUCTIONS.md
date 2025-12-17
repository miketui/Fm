# Setup Instructions for Mother Repository

This guide will help you create the new GitHub repository and push the contents.

## Prerequisites

- Git installed on your machine
- GitHub account
- GitHub CLI (`gh`) installed (recommended) OR access to GitHub web interface

## Option 1: Using GitHub CLI (Recommended)

### Step 1: Create the Repository on GitHub

```bash
# Navigate to the mother-repo directory
cd /path/to/mother-repo

# Create a new repository on GitHub
gh repo create mother --public --description "Production-ready EPUB files for The Artisan's Path by Michael David Warren Jr."

# Or for private repository:
gh repo create mother --private --description "Production-ready EPUB files for The Artisan's Path by Michael David Warren Jr."
```

### Step 2: Initialize Git and Push

```bash
# Initialize git repository
git init

# Add all files
git add .

# Create initial commit
git commit -m "Initial commit: Transfer REBRANDED_OUTPUT and OEBPS from miketui/Fm"

# Set the main branch
git branch -M main

# Add remote (replace YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/mother.git

# Push to GitHub
git push -u origin main
```

## Option 2: Using GitHub Web Interface

### Step 1: Create Repository on GitHub.com

1. Go to https://github.com/new
2. Repository name: `mother`
3. Description: "Production-ready EPUB files for The Artisan's Path by Michael David Warren Jr."
4. Choose Public or Private
5. DO NOT initialize with README, .gitignore, or license (we already have these)
6. Click "Create repository"

### Step 2: Initialize Git and Push

```bash
# Navigate to the mother-repo directory
cd /path/to/mother-repo

# Initialize git repository
git init

# Add all files
git add .

# Create initial commit
git commit -m "Initial commit: Transfer REBRANDED_OUTPUT and OEBPS from miketui/Fm"

# Set the main branch
git branch -M main

# Add remote (replace YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/mother.git

# Push to GitHub
git push -u origin main
```

## Step 3: Verify the Upload

After pushing, visit your repository at:
```
https://github.com/YOUR_USERNAME/mother
```

You should see:
- ✅ README.md displayed on the main page
- ✅ REBRANDED_OUTPUT directory (172 MB, 304 files)
- ✅ OEBPS directory (11 MB, 208 files)
- ✅ .gitignore file
- ✅ This SETUP_INSTRUCTIONS.md file

## Large File Considerations

**Note:** The total repository size is approximately 183 MB. GitHub allows repositories up to 100 GB, but warns about files larger than 50 MB.

### Large Files in this Repository:

1. **REBRANDED_OUTPUT/The-Artisans-Path.epub** (~85 MB)
   - This is the pre-built EPUB file
   - Consider if you need this in the repository or if it should be a release asset

If you encounter issues with large files, consider:

### Option A: Use Git LFS (Large File Storage)

```bash
# Install Git LFS
git lfs install

# Track large files
git lfs track "*.epub"
git lfs track "*.pdf"

# Add .gitattributes
git add .gitattributes

# Commit and push
git commit -m "Configure Git LFS for large files"
git push
```

### Option B: Remove Large Files from Tracking

```bash
# Remove the pre-built EPUB (it can be rebuilt or added as a release)
git rm --cached REBRANDED_OUTPUT/The-Artisans-Path.epub

# Add to .gitignore
echo "REBRANDED_OUTPUT/The-Artisans-Path.epub" >> .gitignore

# Commit the change
git add .gitignore
git commit -m "Remove pre-built EPUB from tracking"
git push
```

## Creating Releases

After the repository is set up, you can create releases for distribution:

```bash
# Tag a release
git tag -a v1.0.0 -m "Production-ready EPUB and PDF files"
git push origin v1.0.0

# Create a release with GitHub CLI
gh release create v1.0.0 \
  REBRANDED_OUTPUT/The-Artisans-Path.epub \
  --title "The Artisan's Path v1.0.0" \
  --notes "Production-ready EPUB and PDF files for digital and print distribution"
```

## Repository Settings (Optional)

After creating the repository, you may want to:

1. **Add Topics:**
   - epub
   - ebook
   - publishing
   - print-on-demand
   - hairstyling

2. **Enable Issues:** For tracking updates or bug reports

3. **Add a License:** If appropriate for your content

4. **Configure Branch Protection:** To protect the main branch

5. **Add Collaborators:** If others need access

## Troubleshooting

### Error: "Repository not found"
- Make sure you replaced `YOUR_USERNAME` with your actual GitHub username
- Verify the repository was created on GitHub

### Error: "failed to push some refs"
- Run `git pull origin main --rebase` to sync any changes
- Then try `git push origin main` again

### Error: "file too large"
- Use Git LFS as described above
- Or remove large files from tracking

### Permission Denied
- Make sure you're authenticated with GitHub
- Use `gh auth login` to authenticate with GitHub CLI
- Or set up SSH keys: https://docs.github.com/en/authentication

## Next Steps

After successfully pushing to GitHub:

1. Review the README.md on GitHub to ensure it displays correctly
2. Test downloading the repository to verify all files transferred
3. Create a release with the pre-built EPUB file
4. Share the repository URL with collaborators or customers
5. Consider setting up GitHub Pages for documentation

## Support

For questions about the EPUB content or structure, refer to:
- `README.md` - Repository overview
- `REBRANDED_OUTPUT/README.md` - Detailed EPUB documentation
- `REBRANDED_OUTPUT/FINAL_PROJECT_SUMMARY.md` - Complete project details

---

**Note:** This repository was transferred from the main production repository (miketui/Fm) and contains the complete production-ready files for "The Artisan's Path."
