import React from 'react';
import { ChapterTitlePage } from './ChapterTitlePage';

/**
 * Example usage of the ChapterTitlePage component
 * 
 * This file demonstrates how to use the ChapterTitlePage component
 * in a React application with different configurations.
 */

// Example 1: Using the component as-is
export function BasicExample() {
  return (
    <div style={{ minHeight: '100vh', background: '#f5f5f5' }}>
      <ChapterTitlePage />
    </div>
  );
}

// Example 2: Multiple chapters using the same component structure
export function MultipleChaptersExample() {
  const chapters = [
    {
      number: "I",
      title: ["UNVEILING YOUR", "CREATIVE ODYSSEY"],
      quote: "For we are God's handiwork, created in Christ Jesus to do good works...",
      reference: "— Ephesians 2:10"
    },
    {
      number: "X",
      title: ["CRAFTING", "ENDURING LEGACIES"],
      quote: "But the fruit of the Spirit is love, joy, peace…",
      reference: "— Galatians 5:22–23"
    },
    {
      number: "XVI",
      title: ["TRESSES AND", "TEXTURES"],
      quote: "There is neither Jew nor Gentile, neither slave nor free...",
      reference: "— Galatians 3:28"
    }
  ];

  const [currentChapter, setCurrentChapter] = React.useState(0);

  return (
    <div style={{ minHeight: '100vh', background: '#f5f5f5' }}>
      <div style={{
        position: 'fixed',
        top: '20px',
        left: '50%',
        transform: 'translateX(-50%)',
        display: 'flex',
        gap: '1rem',
        zIndex: 1000
      }}>
        {chapters.map((_, idx) => (
          <button
            key={idx}
            onClick={() => setCurrentChapter(idx)}
            style={{
              padding: '0.5rem 1rem',
              background: currentChapter === idx ? '#2B9999' : 'white',
              color: currentChapter === idx ? 'white' : '#2B9999',
              border: '2px solid #2B9999',
              borderRadius: '4px',
              cursor: 'pointer',
              fontWeight: 600
            }}
          >
            Chapter {idx + 1}
          </button>
        ))}
      </div>
      
      {/* Note: Current ChapterTitlePage doesn't accept props yet.
          To make this work, you'd need to enhance the component to accept props. */}
      <ChapterTitlePage />
      
      <div style={{
        position: 'fixed',
        bottom: '20px',
        left: '50%',
        transform: 'translateX(-50%)',
        background: 'white',
        padding: '1rem 2rem',
        borderRadius: '8px',
        boxShadow: '0 4px 8px rgba(0,0,0,0.1)',
        textAlign: 'center'
      }}>
        <p style={{ margin: 0, fontSize: '0.875rem', color: '#666' }}>
          Current: <strong style={{ color: '#2B9999' }}>
            Chapter {chapters[currentChapter].number}
          </strong>
        </p>
      </div>
    </div>
  );
}

// Example 3: Scrollable book-like experience
export function BookViewExample() {
  return (
    <div style={{
      background: 'linear-gradient(to bottom, #f8f6f3 0%, #ebe7e0 100%)',
      minHeight: '100vh',
      padding: '2rem'
    }}>
      <div style={{
        maxWidth: '1200px',
        margin: '0 auto',
        background: 'white',
        borderRadius: '8px',
        boxShadow: '0 4px 20px rgba(0, 0, 0, 0.15)',
        overflow: 'hidden'
      }}>
        <ChapterTitlePage />
        
        {/* Additional content below the title page */}
        <div style={{
          padding: '3rem 2rem',
          maxWidth: '65ch',
          margin: '0 auto',
          lineHeight: 1.6
        }}>
          <h2 style={{
            fontFamily: "'Cinzel Decorative', Georgia, serif",
            fontSize: '1.5rem',
            color: '#2B9999',
            marginBottom: '1.5rem'
          }}>
            Chapter Content Continues...
          </h2>
          <p>
            This example shows how the chapter title page can be followed by
            the chapter content in a seamless reading experience.
          </p>
        </div>
      </div>
    </div>
  );
}

// Example 4: With custom styling wrapper
export function StyledWrapperExample() {
  return (
    <div style={{
      minHeight: '100vh',
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'center',
      background: 'linear-gradient(135deg, rgba(43,153,153,0.05) 0%, rgba(201,169,97,0.05) 100%)',
      padding: '2rem'
    }}>
      <div style={{
        maxWidth: '1000px',
        width: '100%',
        background: 'white',
        borderRadius: '16px',
        boxShadow: '0 20px 40px rgba(0, 0, 0, 0.1)',
        border: '1px solid rgba(43, 153, 153, 0.1)'
      }}>
        <ChapterTitlePage />
      </div>
    </div>
  );
}

// Example 5: Responsive mobile-first layout
export function ResponsiveExample() {
  return (
    <div style={{
      minHeight: '100vh',
      background: '#fff',
      padding: '1rem'
    }}>
      <style>{`
        @media (max-width: 768px) {
          .responsive-container {
            padding: 0.5rem !important;
          }
        }
      `}</style>
      
      <div 
        className="responsive-container"
        style={{
          padding: '2rem',
          transition: 'all 0.3s ease'
        }}
      >
        <ChapterTitlePage />
      </div>
      
      <div style={{
        maxWidth: '600px',
        margin: '2rem auto',
        padding: '1rem',
        background: '#f5f5f5',
        borderRadius: '8px',
        fontSize: '0.875rem'
      }}>
        <p style={{ margin: 0 }}>
          <strong>Tip:</strong> Resize your browser window to see the responsive behavior!
        </p>
      </div>
    </div>
  );
}

// Main demo component that showcases all examples
export function ChapterTitlePageDemo() {
  const [activeExample, setActiveExample] = React.useState('basic');

  const examples = {
    basic: { component: BasicExample, name: 'Basic Usage' },
    multiple: { component: MultipleChaptersExample, name: 'Multiple Chapters' },
    book: { component: BookViewExample, name: 'Book View' },
    styled: { component: StyledWrapperExample, name: 'Styled Wrapper' },
    responsive: { component: ResponsiveExample, name: 'Responsive Layout' }
  };

  const ActiveComponent = examples[activeExample].component;

  return (
    <div>
      <nav style={{
        background: '#2B9999',
        padding: '1rem',
        position: 'sticky',
        top: 0,
        zIndex: 1000,
        boxShadow: '0 2px 8px rgba(0,0,0,0.1)'
      }}>
        <div style={{
          maxWidth: '1200px',
          margin: '0 auto',
          display: 'flex',
          justifyContent: 'space-between',
          alignItems: 'center',
          flexWrap: 'wrap',
          gap: '1rem'
        }}>
          <h1 style={{
            color: 'white',
            margin: 0,
            fontSize: '1.25rem',
            fontFamily: "'Cinzel Decorative', Georgia, serif"
          }}>
            Chapter Title Page Examples
          </h1>
          
          <div style={{ display: 'flex', gap: '0.5rem', flexWrap: 'wrap' }}>
            {Object.entries(examples).map(([key, { name }]) => (
              <button
                key={key}
                onClick={() => setActiveExample(key)}
                style={{
                  padding: '0.5rem 1rem',
                  background: activeExample === key ? '#C9A961' : 'white',
                  color: activeExample === key ? 'white' : '#2B9999',
                  border: 'none',
                  borderRadius: '4px',
                  cursor: 'pointer',
                  fontSize: '0.875rem',
                  fontWeight: 600,
                  transition: 'all 0.2s'
                }}
              >
                {name}
              </button>
            ))}
          </div>
        </div>
      </nav>
      
      <ActiveComponent />
    </div>
  );
}

export default ChapterTitlePageDemo;
