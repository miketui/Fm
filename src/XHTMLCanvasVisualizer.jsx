import React, { useEffect, useRef, useState } from 'react';

const XHTMLCanvasVisualizer = ({ xhtmlContent }) => {
  const canvasRef = useRef(null);
  const [parsedContent, setParsedContent] = useState(null);
  
  // Parse XHTML content and extract key visual elements
  useEffect(() => {
    if (!xhtmlContent) return;
    
    // Create a temporary DOM to parse the XHTML
    const parser = new DOMParser();
    const doc = parser.parseFromString(xhtmlContent, 'text/html');
    
    // Extract key elements for visualization
    const extracted = {
      title: doc.querySelector('.title-lines')?.textContent || 'Chapter I',
      chapterNumber: doc.querySelector('.chapter-number-roman')?.textContent || 'I',
      bibleQuote: doc.querySelector('.bible-quote-text')?.textContent || '',
      introduction: doc.querySelector('.introduction-paragraph p')?.textContent || '',
      sections: Array.from(doc.querySelectorAll('h2, h3')).map(h => ({
        level: h.tagName.toLowerCase(),
        text: h.textContent.trim()
      })),
      brushstrokeImage: doc.querySelector('.chapter-number-brush')?.src || '../images/brushstroke.svg',
      backgroundColor: '#f7f9fa',
      accentColor: '#1797a6',
      textColor: '#1a1a1a'
    };
    
    setParsedContent(extracted);
  }, [xhtmlContent]);
  
  // Draw on canvas
  useEffect(() => {
    if (!parsedContent || !canvasRef.current) return;
    
    const canvas = canvasRef.current;
    const ctx = canvas.getContext('2d');
    const { width, height } = canvas;
    
    // Clear canvas
    ctx.fillStyle = parsedContent.backgroundColor;
    ctx.fillRect(0, 0, width, height);
    
    // Draw brushstroke background (simplified as a teal arc)
    ctx.save();
    ctx.fillStyle = parsedContent.accentColor;
    ctx.globalAlpha = 0.3;
    ctx.beginPath();
    ctx.ellipse(150, 100, 120, 40, Math.PI / 6, 0, 2 * Math.PI);
    ctx.fill();
    ctx.restore();
    
    // Draw chapter number
    ctx.fillStyle = parsedContent.textColor;
    ctx.font = 'bold 72px serif';
    ctx.textAlign = 'center';
    ctx.fillText(parsedContent.chapterNumber, 150, 120);
    
    // Draw title lines
    const titleLines = ['Unveiling', 'Your', 'Creative', 'Odyssy'];
    ctx.font = 'bold 36px sans-serif';
    ctx.fillStyle = parsedContent.accentColor;
    titleLines.forEach((line, index) => {
      ctx.fillText(line, 400, 80 + (index * 45));
    });
    
    // Draw title bar (decorative line)
    ctx.fillStyle = parsedContent.accentColor;
    ctx.fillRect(320, 60, 160, 4);
    
    // Draw bible quote box
    ctx.fillStyle = '#e0f2f1';
    ctx.fillRect(50, 220, 700, 120);
    ctx.strokeStyle = parsedContent.accentColor;
    ctx.lineWidth = 2;
    ctx.strokeRect(50, 220, 700, 120);
    
    // Draw bible quote text (truncated)
    ctx.fillStyle = parsedContent.textColor;
    ctx.font = '18px serif';
    ctx.textAlign = 'left';
    const quoteText = '"For we are God\'s handiwork, created in Christ Jesus..."';
    ctx.fillText(quoteText, 70, 250);
    ctx.font = '14px sans-serif';
    ctx.fillText('— Ephesians 2:10', 70, 320);
    
    // Draw section headers
    let yPos = 380;
    ctx.font = 'bold 24px sans-serif';
    ctx.fillStyle = parsedContent.textColor;
    
    const mainSections = [
      'Introduction',
      'I. The Transformative Power of Conscious Hairstyling',
      'II. The Hairstylist as Artist and Storyteller',
      'III. Mastering Classic and Cutting-Edge Techniques'
    ];
    
    mainSections.forEach((section, index) => {
      if (yPos > height - 50) return; // Stop if we run out of space
      
      // Section background
      ctx.fillStyle = index % 2 === 0 ? '#f0f9ff' : '#e0f7fa';
      ctx.fillRect(50, yPos - 25, 700, 35);
      
      // Section text
      ctx.fillStyle = parsedContent.textColor;
      ctx.font = index === 0 ? 'bold 20px sans-serif' : 'bold 18px sans-serif';
      ctx.fillText(section, 60, yPos);
      
      yPos += 50;
    });
    
    // Draw footer pattern
    ctx.fillStyle = parsedContent.accentColor;
    ctx.globalAlpha = 0.1;
    for (let i = 0; i < 10; i++) {
      ctx.beginPath();
      ctx.arc(80 + (i * 70), height - 30, 15, 0, 2 * Math.PI);
      ctx.fill();
    }
    ctx.globalAlpha = 1.0;
    
  }, [parsedContent]);
  
  const downloadCanvas = () => {
    const canvas = canvasRef.current;
    const link = document.createElement('a');
    link.download = 'chapter-i-visualization.png';
    link.href = canvas.toDataURL();
    link.click();
  };
  
  return (
    <div style={{ padding: '20px', backgroundColor: '#f5f5f5' }}>
      <div style={{ marginBottom: '20px', textAlign: 'center' }}>
        <h1 style={{ color: '#1797a6', marginBottom: '10px' }}>
          XHTML Canvas Visualization
        </h1>
        <p style={{ color: '#666', fontSize: '16px' }}>
          Visual representation of "Chapter I – Unveiling Your Creative Odyssey"
        </p>
        <button 
          onClick={downloadCanvas}
          style={{
            backgroundColor: '#1797a6',
            color: 'white',
            border: 'none',
            padding: '10px 20px',
            borderRadius: '5px',
            cursor: 'pointer',
            fontSize: '14px',
            marginTop: '10px'
          }}
        >
          Download as PNG
        </button>
      </div>
      
      <div style={{ 
        textAlign: 'center', 
        backgroundColor: 'white', 
        padding: '20px', 
        borderRadius: '10px',
        boxShadow: '0 4px 8px rgba(0,0,0,0.1)'
      }}>
        <canvas
          ref={canvasRef}
          width={800}
          height={600}
          style={{ 
            border: '2px solid #1797a6',
            borderRadius: '8px',
            maxWidth: '100%',
            height: 'auto'
          }}
        />
      </div>
      
      <div style={{ 
        marginTop: '20px', 
        padding: '15px', 
        backgroundColor: 'white', 
        borderRadius: '8px',
        boxShadow: '0 2px 4px rgba(0,0,0,0.1)'
      }}>
        <h3 style={{ color: '#1797a6', marginTop: '0' }}>Visualization Elements:</h3>
        <ul style={{ color: '#666', lineHeight: '1.6' }}>
          <li><strong>Chapter Number:</strong> Roman numeral "I" with teal brushstroke background</li>
          <li><strong>Title Stack:</strong> "Unveiling Your Creative Odyssey" in stacked format</li>
          <li><strong>Bible Quote:</strong> Featured quotation in highlighted box</li>
          <li><strong>Section Headers:</strong> Main content sections with alternating backgrounds</li>
          <li><strong>Visual Elements:</strong> Decorative patterns and color scheme matching EPUB design</li>
        </ul>
      </div>
    </div>
  );
};

export default XHTMLCanvasVisualizer;