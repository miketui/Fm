import React from 'react';

/**
 * ChapterTitlePage Component
 * 
 * A React visual canvas component that displays the chapter title page
 * matching the EPUB structure from "The Artisan's Path" book.
 * 
 * Features:
 * - Chapter Number Emblem with decorative brushstroke
 * - Title Stack with stacked title lines
 * - Scripture Quote in styled container
 * - Introduction section with drop cap
 * 
 * Based on: REBRANDED_OUTPUT/xhtml/20-chapter-x-crafting-enduring-legacies.xhtml
 */
export function ChapterTitlePage() {
  return (
    <section
      className="chap-title"
      style={{
        minHeight: '90vh',
        display: 'flex',
        flexDirection: 'column',
        justifyContent: 'center',
        alignItems: 'center',
        padding: '3rem 1.5rem',
        textAlign: 'center',
        backgroundColor: '#FFFFFF',
      }}
    >
      {/* Chapter Number Emblem */}
      <div
        className="chapter-number-figure"
        style={{
          position: 'relative',
          width: 'clamp(200px, 40vw, 280px)',
          height: 'clamp(200px, 40vw, 280px)',
          margin: '0 auto 2rem',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
        }}
      >
        <img
          src="/assets/brush-teal.png"
          alt=""
          className="chapter-number-brush"
          style={{
            position: 'absolute',
            width: '100%',
            height: '100%',
            objectFit: 'contain',
            opacity: 0.9,
          }}
          onError={(e) => {
            // Fallback: Display a teal circle if image not found
            e.target.style.display = 'none';
            e.target.nextSibling.style.backgroundColor = '#2B9999';
            e.target.nextSibling.style.borderRadius = '50%';
            e.target.nextSibling.style.width = '280px';
            e.target.nextSibling.style.height = '280px';
            e.target.nextSibling.style.display = 'flex';
            e.target.nextSibling.style.alignItems = 'center';
            e.target.nextSibling.style.justifyContent = 'center';
          }}
        />
        <span
          className="chapter-number-roman"
          style={{
            position: 'relative',
            zIndex: 1,
            fontFamily: "'Cinzel Decorative', Georgia, 'Times New Roman', serif",
            fontSize: 'clamp(4rem, 10vw, 6rem)',
            fontWeight: 400,
            color: '#FFFFFF',
            textShadow: '0 2px 4px rgba(0, 0, 0, 0.1)',
          }}
        >
          X
        </span>
      </div>

      {/* Title Stack */}
      <div
        className="title-stack"
        style={{
          marginBottom: '3rem',
          maxWidth: '800px',
        }}
      >
        <div
          className="title-bar"
          style={{
            height: '4px',
            width: '60px',
            margin: '0 auto 1.5rem',
            background: 'linear-gradient(90deg, #C9A961, transparent 60%)',
            borderRadius: '9999px',
          }}
          aria-hidden="true"
        />
        <div
          className="title-lines"
          style={{
            display: 'flex',
            flexDirection: 'column',
            gap: '0.75rem',
          }}
        >
          <span
            className="title-line"
            style={{
              fontFamily: "'Cinzel Decorative', Georgia, 'Times New Roman', serif",
              fontSize: 'clamp(2rem, 5vw, 3rem)',
              fontWeight: 400,
              color: '#2B9999',
              textTransform: 'uppercase',
              letterSpacing: '0.05em',
              lineHeight: 1.25,
            }}
          >
            CRAFTING
          </span>
          <span
            className="title-line"
            style={{
              fontFamily: "'Cinzel Decorative', Georgia, 'Times New Roman', serif",
              fontSize: 'clamp(2rem, 5vw, 3rem)',
              fontWeight: 400,
              color: '#2B9999',
              textTransform: 'uppercase',
              letterSpacing: '0.05em',
              lineHeight: 1.25,
            }}
          >
            ENDURING LEGACIES
          </span>
        </div>
      </div>

      {/* Scripture Quote */}
      <div
        className="bible-quote-container"
        style={{
          maxWidth: '600px',
          margin: '0 auto 3rem',
          padding: '1.75rem 2rem',
          paddingLeft: '2.5rem',
          background: '#F5F3EF',
          borderRadius: '1rem',
          boxShadow: '0 4px 6px rgba(15, 22, 22, 0.1)',
          position: 'relative',
          borderLeft: '4px solid #C9A961',
        }}
      >
        <p
          className="bible-quote-text"
          style={{
            fontFamily: "'Libre Baskerville', Georgia, 'Times New Roman', serif",
            fontSize: 'clamp(1.05rem, 1.1vw, 1.2rem)',
            fontStyle: 'italic',
            lineHeight: 1.8,
            color: '#2B2B2B',
            marginBottom: '1rem',
            textAlign: 'center',
          }}
        >
          "But the fruit of the Spirit is love, joy, peace…"
        </p>
        <span
          className="bible-quote-reference"
          style={{
            fontFamily: "'Montserrat', Arial, 'Helvetica Neue', sans-serif",
            fontSize: 'clamp(0.94rem, 0.9vw, 1.05rem)',
            color: '#C9A961',
            fontWeight: 600,
            textAlign: 'right',
            display: 'block',
            fontStyle: 'italic',
          }}
        >
          — Galatians 5:22–23
        </span>
      </div>

      {/* Introduction */}
      <h2
        className="introduction-heading"
        style={{
          fontFamily: "'Cinzel Decorative', Georgia, 'Times New Roman', serif",
          fontSize: 'clamp(1.8rem, 2.8vw, 2.25rem)',
          color: '#2B9999',
          textAlign: 'center',
          margin: '3rem 0 1.75rem',
        }}
      >
        Introduction
      </h2>

      <div
        className="introduction-paragraph dropcap-first-letter"
        style={{
          maxWidth: '65ch',
          margin: '0 auto',
          textAlign: 'left',
        }}
      >
        <p
          style={{
            fontFamily: "'Libre Baskerville', Georgia, 'Times New Roman', serif",
            fontSize: 'clamp(1.05rem, 1.1vw, 1.2rem)',
            lineHeight: 1.6,
            color: '#0F1616',
          }}
        >
          <span
            style={{
              fontFamily: "'Cinzel Decorative', Georgia, 'Times New Roman', serif",
              fontSize: 'clamp(3rem, 6vw, 4rem)',
              fontWeight: 700,
              lineHeight: 0.8,
              float: 'left',
              margin: '0.1em 0.1em 0 0',
              color: '#2B9999',
            }}
          >
            C
          </span>
          onsider the impact of your work not just today, but as a legacy…
        </p>
      </div>
    </section>
  );
}

export default ChapterTitlePage;
