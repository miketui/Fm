import React, { useState, useEffect } from 'react';
import XHTMLCanvasVisualizer from './XHTMLCanvasVisualizer.jsx';

const App = () => {
  const [xhtmlContent, setXhtmlContent] = useState('');
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    // Load the XHTML content
    const loadXHTMLContent = async () => {
      try {
        // Since we're running this in a browser, we'll include the content directly
        // In a real scenario, you might fetch from a server
        const sampleXHTML = `<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" xml:lang="en" lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Chapter I – Unveiling Your Creative Odyssey</title>
  </head>
  <body class="chapter-page">
    <main role="main" epub:type="bodymatter chapter">
      <section class="chap-title" role="region">
        <figure class="chapter-number-figure" role="group" aria-label="Chapter number I">
          <img class="chapter-number-brush" src="../images/brushstroke.svg" alt="Decorative teal brushstroke background" />
          <figcaption class="chapter-number-roman">I</figcaption>
        </figure>

        <div class="title-stack">
          <div class="title-bar"></div>
          <div class="title-lines">
            <div class="title-line">Unveiling</div>
            <div class="title-line">Your</div>
            <div class="title-line">Creative</div>
            <div class="title-line">Odyssey</div>
          </div>
        </div>
        
        <figure class="bible-quote-container image-quote" role="group" aria-labelledby="bq-text bq-ref">
          <blockquote class="bible-quote-text" id="bq-text">
            "For we are God's handiwork, created in Christ Jesus to do good works, which God prepared in advance for us to do."
          </blockquote>
          <figcaption class="bible-quote-reference" id="bq-ref">— Ephesians 2:10</figcaption>
        </figure>
        
        <h2 class="introduction-heading">Introduction</h2>
        <div class="introduction-paragraph dropcap-first-letter">
          <p><strong>P</strong>icture celebrity stylist Ursula Stephen, who transformed Rihanna's look early in her career, catapulting both the singer's and her own careers to new heights. With each cut, Ursula shaped not only her client's confidence but also a bold public identity, proving that hairstyling is more than aesthetics—it's a powerful tool for self-expression and cultural influence.</p>
        </div>
      </section>

      <section class="chap-body" role="region">
        <div class="content-area">
          <h2>I. The Transformative Power of Conscious Hairstyling</h2>
          <h3>Understanding the Psychological Impact of Hairstyling on Self-Esteem</h3>
          
          <h2>II. The Hairstylist as Artist and Storyteller</h2>
          <h3>Embracing the Artistry and Creativity of Hairstyling</h3>
          
          <h2>III. Mastering Classic and Cutting-Edge Techniques</h2>
          <h3>Mastering Classic and Contemporary Methods</h3>
          
          <h2>IV. Understanding Diverse Hair Types and Championing Representation</h2>
          <h3>Unique Needs and Textures</h3>
        </div>
      </section>
    </main>
  </body>
</html>`;
        
        setXhtmlContent(sampleXHTML);
        setLoading(false);
      } catch (err) {
        setError(err.message);
        setLoading(false);
      }
    };

    loadXHTMLContent();
  }, []);

  if (loading) {
    return (
      <div style={{ 
        display: 'flex', 
        justifyContent: 'center', 
        alignItems: 'center', 
        height: '100vh',
        backgroundColor: '#f5f5f5'
      }}>
        <div style={{ textAlign: 'center' }}>
          <div style={{ 
            fontSize: '18px', 
            color: '#1797a6',
            marginBottom: '10px'
          }}>
            Loading XHTML content...
          </div>
          <div style={{
            width: '40px',
            height: '40px',
            border: '4px solid #e0f2f1',
            borderTop: '4px solid #1797a6',
            borderRadius: '50%',
            animation: 'spin 1s linear infinite',
            margin: '0 auto'
          }}></div>
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div style={{ 
        display: 'flex', 
        justifyContent: 'center', 
        alignItems: 'center', 
        height: '100vh',
        backgroundColor: '#f5f5f5'
      }}>
        <div style={{ 
          backgroundColor: 'white',
          padding: '20px',
          borderRadius: '8px',
          boxShadow: '0 2px 4px rgba(0,0,0,0.1)',
          textAlign: 'center',
          color: '#e74c3c'
        }}>
          <h2>Error Loading Content</h2>
          <p>{error}</p>
        </div>
      </div>
    );
  }

  return (
    <div style={{ minHeight: '100vh', backgroundColor: '#f5f5f5' }}>
      <XHTMLCanvasVisualizer xhtmlContent={xhtmlContent} />
    </div>
  );
};

export default App;