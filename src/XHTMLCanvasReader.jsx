import React, { useEffect, useRef, useState } from 'react';
import fs from 'fs';
import path from 'path';

const XHTMLCanvasReader = () => {
  const canvasRef = useRef(null);
  const [xhtmlContent, setXhtmlContent] = useState('');
  const [parsedContent, setParsedContent] = useState(null);
  const [loading, setLoading] = useState(true);

  // Load XHTML file content
  useEffect(() => {
    const loadXHTMLFile = async () => {
      try {
        const xhtmlPath = path.join(process.cwd(), 'OEBPS/text/9-chapter-i-unveiling-your-creative-odyssey.xhtml');
        const content = fs.readFileSync(xhtmlPath, 'utf8');
        setXhtmlContent(content);
        
        // Parse the content
        const parser = new DOMParser();
        const doc = parser.parseFromString(content, 'text/html');
        
        const extracted = {
          title: Array.from(doc.querySelectorAll('.title-line')).map(el => el.textContent).join(' '),
          chapterNumber: doc.querySelector('.chapter-number-roman')?.textContent || 'I',
          bibleQuote: doc.querySelector('.bible-quote-text')?.textContent || '',
          bibleReference: doc.querySelector('.bible-quote-reference')?.textContent || '',
          introduction: doc.querySelector('.introduction-paragraph p')?.textContent?.substring(0, 200) + '...' || '',
          sections: Array.from(doc.querySelectorAll('h2')).slice(0, 6).map(h => h.textContent.trim()),
          backgroundColor: '#f7f9fa',
          accentColor: '#1797a6',
          textColor: '#1a1a1a',
          quoteColor: '#e0f2f1'
        };
        
        setParsedContent(extracted);
        setLoading(false);
      } catch (error) {
        console.error('Error loading XHTML:', error);
        setLoading(false);
      }
    };

    loadXHTMLFile();
  }, []);

  // Enhanced canvas drawing
  useEffect(() => {
    if (!parsedContent || !canvasRef.current) return;
    
    const canvas = canvasRef.current;
    const ctx = canvas.getContext('2d');
    const { width, height } = canvas;
    
    // Clear canvas with gradient background
    const gradient = ctx.createLinearGradient(0, 0, 0, height);
    gradient.addColorStop(0, '#f7f9fa');
    gradient.addColorStop(1, '#e8f4f8');
    ctx.fillStyle = gradient;
    ctx.fillRect(0, 0, width, height);
    
    // Draw decorative header background
    ctx.fillStyle = parsedContent.accentColor;
    ctx.globalAlpha = 0.1;
    ctx.fillRect(0, 0, width, 180);
    ctx.globalAlpha = 1.0;
    
    // Draw brushstroke background (enhanced)
    ctx.save();
    ctx.fillStyle = parsedContent.accentColor;
    ctx.globalAlpha = 0.4;
    ctx.beginPath();
    ctx.ellipse(150, 90, 140, 50, Math.PI / 8, 0, 2 * Math.PI);
    ctx.fill();
    ctx.globalAlpha = 0.2;
    ctx.beginPath();
    ctx.ellipse(150, 90, 160, 60, Math.PI / 8, 0, 2 * Math.PI);
    ctx.fill();
    ctx.restore();
    
    // Draw chapter number with shadow
    ctx.save();
    ctx.shadowColor = 'rgba(0,0,0,0.3)';
    ctx.shadowOffsetX = 2;
    ctx.shadowOffsetY = 2;
    ctx.shadowBlur = 4;
    ctx.fillStyle = parsedContent.textColor;
    ctx.font = 'bold 84px serif';
    ctx.textAlign = 'center';
    ctx.fillText(parsedContent.chapterNumber, 150, 110);
    ctx.restore();
    
    // Draw title with enhanced styling
    const titleWords = ['Unveiling', 'Your', 'Creative', 'Odyssey'];
    ctx.save();
    ctx.shadowColor = 'rgba(23,151,166,0.3)';
    ctx.shadowOffsetX = 1;
    ctx.shadowOffsetY = 1;
    ctx.shadowBlur = 2;
    
    titleWords.forEach((word, index) => {
      const fontSize = 42 - (index * 2); // Slightly decreasing size
      ctx.font = `bold ${fontSize}px sans-serif`;
      ctx.fillStyle = parsedContent.accentColor;
      ctx.textAlign = 'left';
      ctx.fillText(word, 320, 60 + (index * 48));
    });
    ctx.restore();
    
    // Draw decorative title bar with gradient
    const barGradient = ctx.createLinearGradient(320, 40, 520, 40);
    barGradient.addColorStop(0, parsedContent.accentColor);
    barGradient.addColorStop(1, '#26a69a');
    ctx.fillStyle = barGradient;
    ctx.fillRect(320, 40, 200, 6);
    
    // Draw bible quote section with enhanced styling
    const quoteX = 50, quoteY = 200, quoteW = 700, quoteH = 140;
    
    // Quote background with gradient
    const quoteGradient = ctx.createLinearGradient(quoteX, quoteY, quoteX, quoteY + quoteH);
    quoteGradient.addColorStop(0, '#ffffff');
    quoteGradient.addColorStop(1, parsedContent.quoteColor);
    ctx.fillStyle = quoteGradient;
    ctx.fillRect(quoteX, quoteY, quoteW, quoteH);
    
    // Quote border
    ctx.strokeStyle = parsedContent.accentColor;
    ctx.lineWidth = 3;
    ctx.strokeRect(quoteX, quoteY, quoteW, quoteH);
    
    // Quote text with better formatting
    ctx.fillStyle = parsedContent.textColor;
    ctx.font = '20px serif';
    ctx.textAlign = 'left';
    
    const quoteText = '"For we are God\'s handiwork, created in Christ Jesus';
    const quoteText2 = 'to do good works, which God prepared in advance for us to do."';
    ctx.fillText(quoteText, quoteX + 20, quoteY + 40);
    ctx.fillText(quoteText2, quoteX + 20, quoteY + 70);
    
    ctx.font = 'italic 16px sans-serif';
    ctx.fillStyle = parsedContent.accentColor;
    ctx.fillText('— Ephesians 2:10', quoteX + 20, quoteY + 110);
    
    // Draw content sections with enhanced layout
    let yPos = 370;
    const sectionHeight = 45;
    
    parsedContent.sections.forEach((section, index) => {
      if (yPos > height - 60) return;
      
      // Section background with alternating colors
      const sectionBg = index % 2 === 0 ? '#f8fcff' : '#f0f9ff';
      ctx.fillStyle = sectionBg;
      ctx.fillRect(40, yPos - 30, 720, sectionHeight);
      
      // Section border
      ctx.strokeStyle = parsedContent.accentColor;
      ctx.lineWidth = 1;
      ctx.globalAlpha = 0.3;
      ctx.strokeRect(40, yPos - 30, 720, sectionHeight);
      ctx.globalAlpha = 1.0;
      
      // Section text
      ctx.fillStyle = parsedContent.textColor;
      const fontSize = section.toLowerCase().includes('introduction') ? 22 : 18;
      ctx.font = `bold ${fontSize}px sans-serif`;
      ctx.textAlign = 'left';
      
      // Truncate long section titles
      let displayText = section;
      if (section.length > 60) {
        displayText = section.substring(0, 57) + '...';
      }
      
      ctx.fillText(displayText, 60, yPos);
      yPos += sectionHeight + 10;
    });
    
    // Draw footer with decorative elements
    ctx.fillStyle = parsedContent.accentColor;
    ctx.globalAlpha = 0.15;
    
    // Footer pattern
    for (let i = 0; i < 12; i++) {
      const x = 60 + (i * 60);
      const y = height - 40;
      const size = 12 + (i % 3) * 3;
      
      ctx.beginPath();
      ctx.arc(x, y, size, 0, 2 * Math.PI);
      ctx.fill();
    }
    
    // Add border frame
    ctx.globalAlpha = 1.0;
    ctx.strokeStyle = parsedContent.accentColor;
    ctx.lineWidth = 4;
    ctx.strokeRect(2, 2, width - 4, height - 4);
    
  }, [parsedContent]);

  const downloadCanvas = () => {
    const canvas = canvasRef.current;
    const link = document.createElement('a');
    link.download = 'chapter-i-creative-odyssey-visualization.png';
    link.href = canvas.toDataURL('image/png', 1.0);
    link.click();
  };

  if (loading) {
    return (
      <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', height: '100vh' }}>
        <div>Loading XHTML content...</div>
      </div>
    );
  }

  return (
    <div style={{ padding: '20px', backgroundColor: '#f5f5f5', minHeight: '100vh' }}>
      <div style={{ textAlign: 'center', marginBottom: '30px' }}>
        <h1 style={{ color: '#1797a6', fontSize: '32px', marginBottom: '10px' }}>
          📖 XHTML Canvas Visualization
        </h1>
        <h2 style={{ color: '#333', fontSize: '20px', fontWeight: 'normal', marginBottom: '15px' }}>
          Chapter I – Unveiling Your Creative Odyssey
        </h2>
        <p style={{ color: '#666', fontSize: '16px', maxWidth: '600px', margin: '0 auto 20px' }}>
          Interactive canvas visualization of the EPUB chapter content, showcasing the visual layout and design elements.
        </p>
        <button 
          onClick={downloadCanvas}
          style={{
            backgroundColor: '#1797a6',
            color: 'white',
            border: 'none',
            padding: '12px 24px',
            borderRadius: '6px',
            cursor: 'pointer',
            fontSize: '16px',
            fontWeight: 'bold',
            transition: 'background-color 0.3s'
          }}
          onMouseOver={(e) => e.target.style.backgroundColor = '#137a87'}
          onMouseOut={(e) => e.target.style.backgroundColor = '#1797a6'}
        >
          📥 Download Visualization
        </button>
      </div>
      
      <div style={{ 
        display: 'flex',
        justifyContent: 'center',
        backgroundColor: 'white', 
        padding: '30px', 
        borderRadius: '12px',
        boxShadow: '0 8px 16px rgba(0,0,0,0.1)',
        maxWidth: '900px',
        margin: '0 auto'
      }}>
        <canvas
          ref={canvasRef}
          width={800}
          height={700}
          style={{ 
            border: '3px solid #1797a6',
            borderRadius: '8px',
            maxWidth: '100%',
            height: 'auto',
            backgroundColor: 'white'
          }}
        />
      </div>
      
      <div style={{ 
        marginTop: '30px', 
        padding: '20px', 
        backgroundColor: 'white', 
        borderRadius: '10px',
        boxShadow: '0 4px 8px rgba(0,0,0,0.1)',
        maxWidth: '900px',
        margin: '30px auto 0'
      }}>
        <h3 style={{ color: '#1797a6', marginTop: '0', fontSize: '20px' }}>🎨 Visualization Features:</h3>
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(300px, 1fr))', gap: '15px' }}>
          <div>
            <h4 style={{ color: '#333', margin: '0 0 8px 0' }}>📍 Chapter Elements</h4>
            <ul style={{ color: '#666', lineHeight: '1.6', margin: '0', paddingLeft: '20px' }}>
              <li>Roman numeral chapter number with brushstroke</li>
              <li>Stacked title design: "Unveiling Your Creative Odyssey"</li>
              <li>Biblical quotation in highlighted container</li>
            </ul>
          </div>
          <div>
            <h4 style={{ color: '#333', margin: '0 0 8px 0' }}>🎯 Visual Design</h4>
            <ul style={{ color: '#666', lineHeight: '1.6', margin: '0', paddingLeft: '20px' }}>
              <li>Teal accent color scheme (#1797a6)</li>
              <li>Gradient backgrounds and shadow effects</li>
              <li>Professional typography and spacing</li>
            </ul>
          </div>
        </div>
        
        <div style={{ marginTop: '20px', padding: '15px', backgroundColor: '#f8fcff', borderRadius: '6px', border: '1px solid #e0f2f1' }}>
          <p style={{ color: '#555', margin: '0', fontStyle: 'italic', textAlign: 'center' }}>
            🔍 This canvas visualization transforms the XHTML structure into a visual representation that captures the essence of the chapter's design and content organization.
          </p>
        </div>
      </div>
    </div>
  );
};

export default XHTMLCanvasReader;