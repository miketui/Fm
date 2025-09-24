#!/usr/bin/env node

/**
 * XHTML Canvas Visualization Generator
 * Generates a visual representation of the Chapter I XHTML content
 */

const fs = require('fs');
const path = require('path');
const { JSDOM } = require('jsdom');

// Canvas implementation for Node.js
let Canvas, createCanvas, loadImage;
try {
  const canvas = require('canvas');
  Canvas = canvas.Canvas;
  createCanvas = canvas.createCanvas;
  loadImage = canvas.loadImage;
} catch (error) {
  console.log('Canvas not available, installing...');
  require('child_process').execSync('npm install canvas', { stdio: 'inherit' });
  const canvas = require('canvas');
  Canvas = canvas.Canvas;
  createCanvas = canvas.createCanvas;
  loadImage = canvas.loadImage;
}

async function generateVisualization() {
  try {
    // Read the XHTML file
    const xhtmlPath = path.join(__dirname, 'OEBPS/text/9-chapter-i-unveiling-your-creative-odyssey.xhtml');
    console.log('📖 Reading XHTML file:', xhtmlPath);
    
    const xhtmlContent = fs.readFileSync(xhtmlPath, 'utf8');
    
    // Parse the XHTML content using JSDOM
    const dom = new JSDOM(xhtmlContent, { contentType: 'text/html' });
    const doc = dom.window.document;
    
    // Extract content elements
    const parsedContent = {
      title: Array.from(doc.querySelectorAll('.title-line')).map(el => el.textContent.trim()),
      chapterNumber: doc.querySelector('.chapter-number-roman')?.textContent || 'I',
      bibleQuote: doc.querySelector('.bible-quote-text')?.textContent || '',
      bibleReference: doc.querySelector('.bible-quote-reference')?.textContent || '',
      introduction: doc.querySelector('.introduction-paragraph p')?.textContent?.substring(0, 150) + '...' || '',
      sections: Array.from(doc.querySelectorAll('h2')).slice(0, 8).map(h => h.textContent.trim()),
      backgroundColor: '#f7f9fa',
      accentColor: '#1797a6',
      textColor: '#1a1a1a',
      quoteColor: '#e0f2f1'
    };
    
    console.log('🎯 Extracted content elements:');
    console.log('- Chapter Number:', parsedContent.chapterNumber);
    console.log('- Title Lines:', parsedContent.title.length);
    console.log('- Bible Quote Length:', parsedContent.bibleQuote.length);
    console.log('- Sections Found:', parsedContent.sections.length);
    
    // Create canvas
    const width = 1000;
    const height = 800;
    const canvas = createCanvas(width, height);
    const ctx = canvas.getContext('2d');
    
    console.log('🎨 Rendering canvas visualization...');
    
    // Set high-quality rendering
    ctx.antialias = 'subpixel';
    ctx.textDrawingMode = 'path';
    
    // Background gradient
    const bgGradient = ctx.createLinearGradient(0, 0, 0, height);
    bgGradient.addColorStop(0, '#f7f9fa');
    bgGradient.addColorStop(0.3, '#f0f8fa');
    bgGradient.addColorStop(1, '#e8f4f8');
    ctx.fillStyle = bgGradient;
    ctx.fillRect(0, 0, width, height);
    
    // Header background
    ctx.fillStyle = parsedContent.accentColor;
    ctx.globalAlpha = 0.08;
    ctx.fillRect(0, 0, width, 200);
    ctx.globalAlpha = 1.0;
    
    // Decorative brushstroke backgrounds
    ctx.save();
    ctx.fillStyle = parsedContent.accentColor;
    ctx.globalAlpha = 0.25;
    ctx.beginPath();
    ctx.ellipse(180, 110, 160, 60, Math.PI / 10, 0, 2 * Math.PI);
    ctx.fill();
    ctx.globalAlpha = 0.15;
    ctx.beginPath();
    ctx.ellipse(180, 110, 200, 80, Math.PI / 10, 0, 2 * Math.PI);
    ctx.fill();
    ctx.restore();
    
    // Chapter number with enhanced styling
    ctx.save();
    ctx.shadowColor = 'rgba(0,0,0,0.4)';
    ctx.shadowOffsetX = 3;
    ctx.shadowOffsetY = 3;
    ctx.shadowBlur = 8;
    ctx.fillStyle = parsedContent.textColor;
    ctx.font = 'bold 96px serif';
    ctx.textAlign = 'center';
    ctx.fillText(parsedContent.chapterNumber, 180, 130);
    ctx.restore();
    
    // Title stack with enhanced typography
    ctx.save();
    ctx.shadowColor = 'rgba(23,151,166,0.4)';
    ctx.shadowOffsetX = 2;
    ctx.shadowOffsetY = 2;
    ctx.shadowBlur = 4;
    
    parsedContent.title.forEach((line, index) => {
      const fontSize = 48 - (index * 2);
      ctx.font = `bold ${fontSize}px sans-serif`;
      ctx.fillStyle = index === 0 ? parsedContent.accentColor : '#26a69a';
      ctx.textAlign = 'left';
      ctx.fillText(line, 400, 70 + (index * 52));
    });
    ctx.restore();
    
    // Decorative title bar
    const titleBarGradient = ctx.createLinearGradient(400, 45, 650, 45);
    titleBarGradient.addColorStop(0, parsedContent.accentColor);
    titleBarGradient.addColorStop(0.5, '#26a69a');
    titleBarGradient.addColorStop(1, '#4db6ac');
    ctx.fillStyle = titleBarGradient;
    ctx.fillRect(400, 45, 250, 8);
    
    // Bible quote section
    const quoteX = 60, quoteY = 240, quoteW = 880, quoteH = 160;
    
    // Quote background with subtle gradient
    const quoteGradient = ctx.createLinearGradient(quoteX, quoteY, quoteX, quoteY + quoteH);
    quoteGradient.addColorStop(0, '#ffffff');
    quoteGradient.addColorStop(0.5, '#fafffe');
    quoteGradient.addColorStop(1, parsedContent.quoteColor);
    ctx.fillStyle = quoteGradient;
    ctx.fillRect(quoteX, quoteY, quoteW, quoteH);
    
    // Quote decorative border
    ctx.strokeStyle = parsedContent.accentColor;
    ctx.lineWidth = 4;
    ctx.strokeRect(quoteX, quoteY, quoteW, quoteH);
    
    // Quote inner highlight
    ctx.strokeStyle = '#ffffff';
    ctx.lineWidth = 2;
    ctx.strokeRect(quoteX + 2, quoteY + 2, quoteW - 4, quoteH - 4);
    
    // Quote text formatting
    ctx.fillStyle = parsedContent.textColor;
    ctx.font = '24px serif';
    ctx.textAlign = 'left';
    
    // Format bible quote into multiple lines
    const quoteLines = [
      '"For we are God\'s handiwork, created in',
      'Christ Jesus to do good works, which God',
      'prepared in advance for us to do."'
    ];
    
    quoteLines.forEach((line, index) => {
      ctx.fillText(line, quoteX + 30, quoteY + 50 + (index * 35));
    });
    
    // Bible reference
    ctx.font = 'italic 20px sans-serif';
    ctx.fillStyle = parsedContent.accentColor;
    ctx.fillText('— Ephesians 2:10', quoteX + 30, quoteY + 140);
    
    // Content sections with enhanced design
    let yPos = 440;
    const sectionHeight = 50;
    
    console.log('📝 Rendering content sections...');
    
    parsedContent.sections.forEach((section, index) => {
      if (yPos > height - 80) return;
      
      // Section background with alternating design
      const isEven = index % 2 === 0;
      const sectionBg = isEven ? '#f8fcff' : '#f0f9ff';
      const borderColor = isEven ? '#e0f2fe' : '#bfdbfe';
      
      ctx.fillStyle = sectionBg;
      ctx.fillRect(50, yPos - 35, 900, sectionHeight);
      
      // Section border and highlight
      ctx.strokeStyle = borderColor;
      ctx.lineWidth = 2;
      ctx.strokeRect(50, yPos - 35, 900, sectionHeight);
      
      // Section number circle (for major sections)
      if (section.match(/^[IVX]+\./)) {
        ctx.fillStyle = parsedContent.accentColor;
        ctx.beginPath();
        ctx.arc(80, yPos - 10, 15, 0, 2 * Math.PI);
        ctx.fill();
        
        ctx.fillStyle = '#ffffff';
        ctx.font = 'bold 14px sans-serif';
        ctx.textAlign = 'center';
        ctx.fillText((index + 1).toString(), 80, yPos - 5);
      }
      
      // Section text
      ctx.fillStyle = parsedContent.textColor;
      const isIntro = section.toLowerCase().includes('introduction');
      const isMajor = section.match(/^[IVX]+\./);
      const fontSize = isIntro ? 26 : (isMajor ? 22 : 20);
      
      ctx.font = `bold ${fontSize}px sans-serif`;
      ctx.textAlign = 'left';
      
      // Truncate very long section titles
      let displayText = section;
      const maxLength = 65;
      if (section.length > maxLength) {
        displayText = section.substring(0, maxLength - 3) + '...';
      }
      
      const textX = section.match(/^[IVX]+\./) ? 110 : 80;
      ctx.fillText(displayText, textX, yPos - 5);
      
      yPos += sectionHeight + 15;
    });
    
    // Footer decorative elements
    console.log('✨ Adding decorative elements...');
    
    ctx.fillStyle = parsedContent.accentColor;
    ctx.globalAlpha = 0.12;
    
    // Footer wave pattern
    for (let i = 0; i < 15; i++) {
      const x = 70 + (i * 60);
      const y = height - 50 + Math.sin(i * 0.5) * 10;
      const size = 10 + (i % 4) * 4;
      
      ctx.beginPath();
      ctx.arc(x, y, size, 0, 2 * Math.PI);
      ctx.fill();
    }
    
    // Border frame
    ctx.globalAlpha = 1.0;
    ctx.strokeStyle = parsedContent.accentColor;
    ctx.lineWidth = 6;
    ctx.strokeRect(3, 3, width - 6, height - 6);
    
    // Inner frame highlight
    ctx.strokeStyle = '#ffffff';
    ctx.lineWidth = 2;
    ctx.strokeRect(8, 8, width - 16, height - 16);
    
    // Add title at the bottom
    ctx.fillStyle = parsedContent.textColor;
    ctx.font = 'italic 16px sans-serif';
    ctx.textAlign = 'center';
    ctx.globalAlpha = 0.7;
    ctx.fillText('XHTML Canvas Visualization - Chapter I: Unveiling Your Creative Odyssey', width / 2, height - 20);
    ctx.globalAlpha = 1.0;
    
    // Save the image
    const outputPath = path.join(__dirname, 'chapter-i-canvas-visualization.png');
    const buffer = canvas.toBuffer('image/png');
    fs.writeFileSync(outputPath, buffer);
    
    console.log('✅ Canvas visualization generated successfully!');
    console.log('📁 Saved to:', outputPath);
    console.log('📐 Dimensions:', `${width}x${height}px`);
    
    // Also create a smaller preview version
    const previewCanvas = createCanvas(500, 400);
    const previewCtx = previewCanvas.getContext('2d');
    previewCtx.drawImage(canvas, 0, 0, 500, 400);
    
    const previewPath = path.join(__dirname, 'chapter-i-canvas-preview.png');
    const previewBuffer = previewCanvas.toBuffer('image/png');
    fs.writeFileSync(previewPath, previewBuffer);
    
    console.log('🖼️  Preview version saved to:', previewPath);
    
    return {
      fullPath: outputPath,
      previewPath: previewPath,
      dimensions: { width, height },
      contentSummary: {
        title: parsedContent.title.join(' '),
        chapterNumber: parsedContent.chapterNumber,
        sectionsCount: parsedContent.sections.length
      }
    };
    
  } catch (error) {
    console.error('❌ Error generating visualization:', error);
    throw error;
  }
}

// Run the generator if called directly
if (require.main === module) {
  generateVisualization()
    .then(result => {
      console.log('\n🎉 Generation completed successfully!');
      console.log('Result:', result);
    })
    .catch(error => {
      console.error('\n💥 Generation failed:', error.message);
      process.exit(1);
    });
}

module.exports = { generateVisualization };