# EPUB Build Command

You are an EPUB build specialist. Your task is to build a production-ready EPUB file from the REBRANDED_OUTPUT directory, ensuring proper packaging and compression.

## Build Process

1. **Pre-Build Validation**
   - Run quick validation checks before building
   - Verify all required files are present
   - Check file permissions and accessibility
   - Validate directory structure

2. **EPUB Package Creation**
   - Create mimetype file (uncompressed, must be first)
   - Package META-INF directory
   - Package all XHTML content files
   - Include all assets (images, fonts, stylesheets)
   - Ensure proper compression (mimetype stored, rest deflated)

3. **Build Steps**
   ```bash
   # Navigate to REBRANDED_OUTPUT
   cd /home/user/Fm/REBRANDED_OUTPUT

   # Remove old EPUB if exists
   rm -f The-Artisans-Path.epub

   # Create EPUB with proper structure
   # Step 1: Add mimetype first (no compression)
   zip -X -0 The-Artisans-Path.epub mimetype

   # Step 2: Add META-INF
   zip -X -r The-Artisans-Path.epub META-INF

   # Step 3: Add content.opf
   zip -X -r The-Artisans-Path.epub content.opf

   # Step 4: Add all content directories
   zip -X -r The-Artisans-Path.epub xhtml fonts images styles templates
   ```

4. **Post-Build Validation**
   - Verify EPUB file was created
   - Check file size is reasonable (should be 5-10 MB)
   - Run epubcheck validation on the built file
   - Test EPUB can be extracted without errors

5. **Build Verification**
   - List contents of EPUB to verify structure
   - Check compression ratios
   - Verify mimetype is stored (not compressed)
   - Confirm all assets are included

## Output

Provide a build report:
- 📦 EPUB filename and location
- 📊 File size and compression statistics
- ✅ Validation results (pass/fail)
- 📋 Contents manifest
- 🚀 Ready for distribution status

## Success Criteria

The build is successful when:
- EPUB file is created without errors
- File passes epubcheck validation
- File size is within expected range (5-10 MB)
- All content files are included
- EPUB can be opened in ebook readers
- Structure follows EPUB 3.0 specifications

## Output Location

Built EPUB: `/home/user/Fm/REBRANDED_OUTPUT/The-Artisans-Path.epub`

## Troubleshooting

If build fails:
1. Check all source files are present
2. Verify permissions on files
3. Ensure zip utility is available
4. Check for special characters in filenames
5. Verify content.opf is valid XML
