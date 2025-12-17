import React, { useState } from 'react';
import { ChevronLeft, ChevronRight, Scissors, Sparkles, Heart, BookOpen, Target, Star } from 'lucide-react';

const ArtisanPathViewer = () => {
  const [currentPage, setCurrentPage] = useState(0);

  const pages = [
    {
      type: 'title',
      name: '1-TitlePage.xhtml',
      content: (
        <div className="page page--title" style={{
          textAlign: 'center',
          display: 'flex',
          flexDirection: 'column',
          justifyContent: 'center',
          minHeight: '75vh'
        }}>
          <div style={{ marginBottom: '2rem' }}>
            <Scissors size={48} style={{
              margin: '0 auto',
              color: '#c9a961',
              strokeWidth: 1.5
            }} />
          </div>

          <h1 style={{
            fontFamily: 'Cinzel Decorative, serif',
            fontSize: '2.75rem',
            lineHeight: '1.2',
            margin: '0 0 1rem',
            color: '#2c1810',
            letterSpacing: '1px'
          }}>
            THE ARTISAN'S PATH
          </h1>

          <div style={{
            width: '80px',
            height: '2px',
            background: 'linear-gradient(to right, transparent, #c9a961, transparent)',
            margin: '1.5rem auto'
          }} />

          <h2 style={{
            fontSize: '1.35rem',
            fontWeight: 400,
            opacity: 0.85,
            margin: '0 0 2rem',
            fontStyle: 'italic',
            color: '#5a4a3a',
            lineHeight: '1.6'
          }}>
            A Comprehensive Guide to Mastering<br />
            Freelance Creative Hairstyling
          </h2>

          <div style={{
            display: 'flex',
            gap: '1rem',
            justifyContent: 'center',
            marginBottom: '2.5rem',
            opacity: 0.7
          }}>
            <Sparkles size={20} style={{ color: '#c9a961' }} />
            <Star size={20} style={{ color: '#c9a961' }} />
            <Sparkles size={20} style={{ color: '#c9a961' }} />
          </div>

          <p style={{
            fontSize: '1.125rem',
            fontWeight: 500,
            letterSpacing: '2px',
            textTransform: 'uppercase',
            color: '#2c1810',
            opacity: 0.8
          }}>
            Curls Contemporary Collective
          </p>

          <p style={{
            fontSize: '0.95rem',
            marginTop: '0.5rem',
            color: '#5a4a3a',
            opacity: 0.7
          }}>
            Volume I: Foundations & Excellence
          </p>
        </div>
      )
    },
    {
      type: 'copyright',
      name: '2-Copyright.xhtml',
      content: (
        <div className="page page--content" style={{ fontSize: '0.9rem' }}>
          <h2 style={{
            fontFamily: 'Cinzel Decorative, serif',
            fontSize: '1.25rem',
            marginBottom: '2rem',
            textAlign: 'center',
            color: '#2c1810'
          }}>
            Copyright & Publishing Information
          </h2>

          <div style={{ textAlign: 'center', marginBottom: '2rem' }}>
            <p style={{ margin: '0.5rem 0', fontWeight: 600 }}>
              The Artisan's Path
            </p>
            <p style={{ margin: '0.5rem 0', opacity: 0.8 }}>
              A Comprehensive Guide to Mastering Freelance Creative Hairstyling
            </p>
          </div>

          <p style={{ margin: '1.5rem 0', textAlign: 'center' }}>
            Copyright © 2025 Curls Contemporary Collective<br />
            All rights reserved.
          </p>

          <p style={{ margin: '1.5rem 0', lineHeight: '1.7' }}>
            No part of this publication may be reproduced, distributed, or transmitted in any form or by any means, including photocopying, recording, or other electronic or mechanical methods, without the prior written permission of the publisher, except in the case of brief quotations embodied in critical reviews and certain other noncommercial uses permitted by copyright law.
          </p>

          <p style={{ margin: '1.5rem 0', lineHeight: '1.7' }}>
            The information provided in this book is designed to provide helpful guidance on the subjects discussed. This book is not meant to be used, nor should it be used, to diagnose or treat any medical condition. The publisher and author are not responsible for any specific health or allergy needs that may require medical supervision and are not liable for any damages or negative consequences from any treatment, action, application, or preparation to any person reading or following the information in this book.
          </p>

          <div style={{
            marginTop: '3rem',
            paddingTop: '1.5rem',
            borderTop: '1px solid #e0d5c7'
          }}>
            <p style={{ margin: '0.5rem 0' }}>
              <strong>Publisher:</strong> Curls Contemporary Collective Press
            </p>
            <p style={{ margin: '0.5rem 0' }}>
              <strong>First Edition:</strong> 2025
            </p>
            <p style={{ margin: '0.5rem 0' }}>
              <strong>ISBN:</strong> 978-1-234567-89-0 (eBook)
            </p>
            <p style={{ margin: '0.5rem 0' }}>
              <strong>Website:</strong> www.curlscontemporary.com
            </p>
          </div>

          <p style={{
            marginTop: '2rem',
            textAlign: 'center',
            fontSize: '0.85rem',
            opacity: 0.7,
            fontStyle: 'italic'
          }}>
            Printed with sustainable practices in mind
          </p>
        </div>
      )
    },
    {
      type: 'toc',
      name: '3-TableOfContents.xhtml',
      content: (
        <div className="page page--content">
          <h2 style={{
            fontFamily: 'Cinzel Decorative, serif',
            fontSize: '2rem',
            marginBottom: '2rem',
            textAlign: 'center',
            color: '#2c1810'
          }}>
            CONTENTS
          </h2>

          <div style={{
            borderTop: '2px solid #c9a961',
            paddingTop: '1.5rem'
          }}>
            <div style={{ marginBottom: '2rem' }}>
              <p style={{
                fontSize: '0.85rem',
                textTransform: 'uppercase',
                letterSpacing: '1.5px',
                color: '#c9a961',
                fontWeight: 600,
                marginBottom: '0.75rem'
              }}>
                Frontmatter
              </p>
              <div style={{ paddingLeft: '1rem' }}>
                <div style={{ display: 'flex', justifyContent: 'space-between', margin: '0.5rem 0' }}>
                  <span>Title Page</span>
                  <span style={{ opacity: 0.5 }}>i</span>
                </div>
                <div style={{ display: 'flex', justifyContent: 'space-between', margin: '0.5rem 0' }}>
                  <span>Copyright</span>
                  <span style={{ opacity: 0.5 }}>ii</span>
                </div>
                <div style={{ display: 'flex', justifyContent: 'space-between', margin: '0.5rem 0' }}>
                  <span>Table of Contents</span>
                  <span style={{ opacity: 0.5 }}>iii</span>
                </div>
                <div style={{ display: 'flex', justifyContent: 'space-between', margin: '0.5rem 0' }}>
                  <span>Dedication</span>
                  <span style={{ opacity: 0.5 }}>iv</span>
                </div>
                <div style={{ display: 'flex', justifyContent: 'space-between', margin: '0.5rem 0' }}>
                  <span>Self-Assessment</span>
                  <span style={{ opacity: 0.5 }}>v</span>
                </div>
                <div style={{ display: 'flex', justifyContent: 'space-between', margin: '0.5rem 0' }}>
                  <span>Affirmation Odyssey</span>
                  <span style={{ opacity: 0.5 }}>vi</span>
                </div>
                <div style={{ display: 'flex', justifyContent: 'space-between', margin: '0.5rem 0' }}>
                  <span>Preface</span>
                  <span style={{ opacity: 0.5 }}>vii</span>
                </div>
              </div>
            </div>

            <div style={{ marginBottom: '2rem' }}>
              <p style={{
                fontSize: '0.85rem',
                textTransform: 'uppercase',
                letterSpacing: '1.5px',
                color: '#c9a961',
                fontWeight: 600,
                marginBottom: '0.75rem'
              }}>
                Part I: Foundations of Creative Hairstyling
              </p>
              <div style={{ paddingLeft: '1rem' }}>
                <div style={{ display: 'flex', justifyContent: 'space-between', margin: '0.5rem 0' }}>
                  <span>Chapter I: Unveiling Your Creative Odyssey</span>
                  <span style={{ opacity: 0.5 }}>3</span>
                </div>
                <div style={{ display: 'flex', justifyContent: 'space-between', margin: '0.5rem 0' }}>
                  <span>Chapter II: Refining Your Creative Toolkit</span>
                  <span style={{ opacity: 0.5 }}>23</span>
                </div>
                <div style={{ display: 'flex', justifyContent: 'space-between', margin: '0.5rem 0' }}>
                  <span>Chapter III: Reigniting Your Creative Fire</span>
                  <span style={{ opacity: 0.5 }}>45</span>
                </div>
              </div>
            </div>

            <div style={{ marginBottom: '2rem' }}>
              <p style={{
                fontSize: '0.85rem',
                textTransform: 'uppercase',
                letterSpacing: '1.5px',
                color: '#c9a961',
                fontWeight: 600,
                marginBottom: '0.75rem'
              }}>
                Part II: Building Your Professional Practice
              </p>
              <div style={{ paddingLeft: '1rem' }}>
                <div style={{ display: 'flex', justifyContent: 'space-between', margin: '0.5rem 0' }}>
                  <span>Chapter IV: The Art of Networking</span>
                  <span style={{ opacity: 0.5 }}>67</span>
                </div>
                <div style={{ display: 'flex', justifyContent: 'space-between', margin: '0.5rem 0' }}>
                  <span>Chapter V: Cultivating Creative Excellence</span>
                  <span style={{ opacity: 0.5 }}>89</span>
                </div>
                <div style={{ display: 'flex', justifyContent: 'space-between', margin: '0.5rem 0' }}>
                  <span>Chapter VI: Mastering the Business</span>
                  <span style={{ opacity: 0.5 }}>109</span>
                </div>
                <div style={{ display: 'flex', justifyContent: 'space-between', margin: '0.5rem 0' }}>
                  <span>Chapter VII: Wellness and Self-Care</span>
                  <span style={{ opacity: 0.5 }}>129</span>
                </div>
                <div style={{ display: 'flex', justifyContent: 'space-between', margin: '0.5rem 0' }}>
                  <span>Chapter VIII: Continuous Education</span>
                  <span style={{ opacity: 0.5 }}>149</span>
                </div>
              </div>
            </div>

            <p style={{
              textAlign: 'center',
              marginTop: '2rem',
              fontSize: '0.875rem',
              fontStyle: 'italic',
              opacity: 0.7
            }}>
              Continue to Part III & Part IV...
            </p>
          </div>
        </div>
      )
    },
    {
      type: 'dedication',
      name: '4-Dedication.xhtml',
      content: (
        <div className="page page--title" style={{
          display: 'flex',
          flexDirection: 'column',
          justifyContent: 'center',
          minHeight: '70vh'
        }}>
          <div style={{ textAlign: 'center', marginBottom: '2rem' }}>
            <Heart size={36} style={{
              color: '#c9a961',
              margin: '0 auto',
              strokeWidth: 1.5
            }} />
          </div>

          <h2 style={{
            fontFamily: 'Cinzel Decorative, serif',
            fontSize: '1.5rem',
            textAlign: 'center',
            marginBottom: '2.5rem',
            color: '#2c1810',
            letterSpacing: '1px'
          }}>
            DEDICATION
          </h2>

          <div style={{
            width: '60px',
            height: '2px',
            background: 'linear-gradient(to right, transparent, #c9a961, transparent)',
            margin: '0 auto 2.5rem'
          }} />

          <p style={{
            fontSize: '1.125rem',
            lineHeight: '1.8',
            textAlign: 'center',
            fontStyle: 'italic',
            color: '#2c1810',
            maxWidth: '32rem',
            margin: '0 auto 2rem'
          }}>
            For those who see beauty where others see only hair—<br />
            those who transform strands into stories, and texture into testimony.
          </p>

          <div style={{ maxWidth: '38rem', margin: '0 auto', textAlign: 'center', lineHeight: '1.8' }}>
            <p style={{ marginBottom: '1.5rem' }}>
              To the <em style={{ color: '#c9a961', fontWeight: 600 }}>artists</em> whose hands tremble with excitement before they create, who see possibilities in every curl pattern and potential in every client. This is for you who have turned rejection into redirection, who understand that your uniqueness isn't a barrier but your greatest gift. Your fingertips hold magic that cannot be taught, only cultivated.
            </p>

            <p style={{ marginBottom: '1.5rem' }}>
              To the <em style={{ color: '#c9a961', fontWeight: 600 }}>apprentices</em> standing nervously with combs in hand, questioning your place: I was once you. Your doubt is the shadow of your greatness waiting to emerge. Study every movement of those before you. The way they listen with their hands, the silent language between stylist and client. These moments contain universes of wisdom.
            </p>

            <div style={{
              background: '#faf8f5',
              padding: '1.5rem',
              borderLeft: '3px solid #c9a961',
              borderRadius: '4px',
              marginBottom: '1.5rem'
            }}>
              <p style={{ margin: 0 }}>
                And to my <em style={{ color: '#c9a961', fontWeight: 600 }}>lighthouse keepers</em> in the storm—<strong>Yusef Williams/Naphia White</strong>, who taught me that technique without heart is just mechanical motion; <strong>Naeemah Lafond</strong>, whose fierce advocacy showed me our work transcends beauty to become cultural affirmation; and <strong>Vernon François</strong>, who helped me see that every curl has a voice if only we'd listen carefully enough—thank you doesn't begin to cover the debt. You didn't just shape my hands; you sculpted my vision.
              </p>
            </div>

            <p style={{ marginBottom: '1.5rem' }}>
              To <em style={{ color: '#c9a961', fontWeight: 600 }}>every hairstylist</em> reading these words: our craft is ancient magic in a modern world. We don't just style hair—we hold stories between our fingers, build confidence with our brushes, and weave heritage into every strand we touch.
            </p>
          </div>

          <p style={{
            fontSize: '1rem',
            marginTop: '2.5rem',
            textAlign: 'center',
            fontWeight: 500,
            color: '#c9a961',
            letterSpacing: '0.5px'
          }}>
            The world is waiting for your signature touch.
          </p>
        </div>
      )
    },
    {
      type: 'worksheet',
      name: '5-SelfAssessment.xhtml',
      content: (
        <div className="page page--worksheet">
          <div style={{ textAlign: 'center', marginBottom: '2rem' }}>
            <Target size={32} style={{ color: '#c9a961', margin: '0 auto 1rem' }} />
            <h2 style={{
              fontFamily: 'Cinzel Decorative, serif',
              fontSize: '1.75rem',
              margin: '0 0 0.5rem',
              color: '#2c1810'
            }}>
              SELF-ASSESSMENT
            </h2>
            <div style={{
              width: '60px',
              height: '2px',
              background: 'linear-gradient(to right, transparent, #c9a961, transparent)',
              margin: '1.5rem auto'
            }} />
            <p style={{
              fontSize: '0.95rem',
              fontStyle: 'italic',
              opacity: 0.75,
              margin: 0
            }}>
              Reflect on your current journey as a freelance hairstylist
            </p>
          </div>

          <div style={{
            background: '#faf8f5',
            padding: '1.25rem',
            borderRadius: '8px',
            marginBottom: '1.5rem',
            borderLeft: '3px solid #c9a961'
          }}>
            <p style={{ margin: '0', fontSize: '0.95rem', lineHeight: '1.7' }}>
              This self-assessment is designed to help you reflect on your current journey as a freelance hairstylist. Take your time to answer each question thoughtfully.
            </p>
          </div>

          <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '2rem' }}>
            {/* Left Column */}
            <div>
              {[
                { num: 1, q: "What initially drew you to the art of hairstyling?", sub: "What sparked your passion for this creative calling?" },
                { num: 2, q: "As you embark on this journey of conscious hairstyling, what are your biggest hopes, dreams, and aspirations", sub: "for your craft and career?" },
                { num: 3, q: "Reflect on your current hairstyling techniques, philosophies, and practices.", sub: "In what areas do you feel you have room to grow and evolve?" },
                { num: 4, q: "How would you describe your current approach to connecting with and understanding your clients' needs, desires, and unique beauty?", sub: "How could you deepen this empathy and attunement?" },
                { num: 5, q: "What does being a \"conscious hairstylist\" mean to you at this stage?", sub: "What values and intentions do you want to bring more fully into your work?" }
              ].map(item => (
                <div key={item.num} style={{ marginBottom: '1.5rem' }}>
                  <div style={{
                    display: 'inline-block',
                    width: '2rem',
                    height: '2rem',
                    background: '#c9a961',
                    color: 'white',
                    borderRadius: '50%',
                    textAlign: 'center',
                    lineHeight: '2rem',
                    fontWeight: 600,
                    marginBottom: '0.75rem',
                    fontSize: '0.9rem'
                  }}>{item.num}</div>
                  <div style={{ fontSize: '0.95rem', lineHeight: '1.6', marginBottom: '0.75rem' }}>
                    <span style={{ fontWeight: 600 }}>{item.q}</span> {item.sub}
                  </div>
                  <div style={{ borderBottom: '2px solid #e0d5c7', minHeight: '4rem' }}></div>
                </div>
              ))}
            </div>

            {/* Right Column */}
            <div>
              {[
                { num: 6, q: "In what ways do you hope to make a positive impact", sub: "on your clients, community, and the beauty industry through your hairstyling?" },
                { num: 7, q: "As you reflect on the current beauty industry, what opportunities do you see for greater inclusivity, sustainability, and empowerment?", sub: "How might you contribute to that vision?" },
                { num: 8, q: "What self-care practices do you currently use to nurture your own well-being and creative inspiration?", sub: "Where could you expand your repertoire?" },
                { num: 9, q: "What mentors, collaborators, or educational resources do you currently draw upon for ongoing growth and development?", sub: "Where might you broaden your support network?" },
                { num: 10, q: "As you look ahead, what are you most excited to learn, experience, and create through the sacred art of hairstyling?", sub: "What's calling to your heart?" }
              ].map(item => (
                <div key={item.num} style={{ marginBottom: '1.5rem' }}>
                  <div style={{
                    display: 'inline-block',
                    width: '2rem',
                    height: '2rem',
                    background: '#c9a961',
                    color: 'white',
                    borderRadius: '50%',
                    textAlign: 'center',
                    lineHeight: '2rem',
                    fontWeight: 600,
                    marginBottom: '0.75rem',
                    fontSize: '0.9rem'
                  }}>{item.num}</div>
                  <div style={{ fontSize: '0.95rem', lineHeight: '1.6', marginBottom: '0.75rem' }}>
                    <span style={{ fontWeight: 600 }}>{item.q}</span> {item.sub}
                  </div>
                  <div style={{ borderBottom: '2px solid #e0d5c7', minHeight: '4rem' }}></div>
                </div>
              ))}
            </div>
          </div>
        </div>
      )
    },
    {
      type: 'worksheet',
      name: '6-AffirmationOdyssey.xhtml',
      content: (
        <div className="page page--worksheet">
          <div style={{ textAlign: 'center', marginBottom: '2rem' }}>
            <Sparkles size={32} style={{ color: '#c9a961', margin: '0 auto 1rem' }} />
            <h2 style={{
              fontFamily: 'Cinzel Decorative, serif',
              fontSize: '1.75rem',
              margin: '0 0 0.5rem',
              color: '#2c1810'
            }}>
              AFFIRMATION ODYSSEY
            </h2>
            <p style={{
              fontSize: '0.95rem',
              fontStyle: 'italic',
              opacity: 0.75,
              margin: '0.5rem 0 1.5rem'
            }}>
              Building Your Creative Confidence
            </p>
            <div style={{
              width: '60px',
              height: '2px',
              background: 'linear-gradient(to right, transparent, #c9a961, transparent)',
              margin: '0 auto'
            }} />
          </div>

          <div style={{
            background: '#faf8f5',
            padding: '1.25rem',
            borderRadius: '8px',
            marginBottom: '1.5rem',
            borderLeft: '3px solid #c9a961'
          }}>
            <p style={{ margin: '0', fontSize: '0.95rem', lineHeight: '1.7' }}>
              This is more than an activity; it's a step toward personal growth. As you dive into this eBook, you'll gradually build your own affirmation, reflecting and finding your inner voice along the way. By the end, you'll have crafted a 12-line testament to your creativity and self-awareness. Start with your first three lines now and watch your affirmation take shape.
            </p>
          </div>

          {/* Your Affirmation Section */}
          <div style={{ marginBottom: '2rem' }}>
            <div style={{
              display: 'flex',
              alignItems: 'center',
              gap: '1rem',
              marginBottom: '1.5rem'
            }}>
              <div style={{ flex: 1, height: '1px', background: 'rgba(201, 169, 97, 0.3)' }}></div>
              <div style={{
                fontWeight: 600,
                textTransform: 'uppercase',
                letterSpacing: '1px',
                fontSize: '0.9rem',
                color: '#c9a961'
              }}>Your Affirmation</div>
              <div style={{ flex: 1, height: '1px', background: 'rgba(201, 169, 97, 0.3)' }}></div>
            </div>

            {[1, 2, 3].map(num => (
              <div key={num} style={{ display: 'flex', alignItems: 'center', gap: '1rem', marginBottom: '1rem' }}>
                <div style={{
                  width: '2rem',
                  height: '2rem',
                  background: '#c9a961',
                  color: 'white',
                  borderRadius: '50%',
                  textAlign: 'center',
                  lineHeight: '2rem',
                  fontWeight: 600,
                  flexShrink: 0,
                  fontSize: '0.9rem'
                }}>{num}</div>
                <div style={{ flex: 1, borderBottom: '2px solid #e0d5c7', minHeight: '2.5rem' }}></div>
              </div>
            ))}
          </div>

          {/* Inspiration Section */}
          <div>
            <div style={{
              display: 'flex',
              alignItems: 'center',
              gap: '1rem',
              marginBottom: '1.5rem'
            }}>
              <div style={{ flex: 1, height: '1px', background: 'rgba(201, 169, 97, 0.3)' }}></div>
              <div style={{
                fontWeight: 600,
                textTransform: 'uppercase',
                letterSpacing: '1px',
                fontSize: '0.9rem',
                color: '#c9a961'
              }}>Inspiration</div>
              <div style={{ flex: 1, height: '1px', background: 'rgba(201, 169, 97, 0.3)' }}></div>
            </div>

            <div style={{ display: 'flex', flexDirection: 'column', gap: '0.75rem' }}>
              {[
                "I am capable and strong, with endless potential.",
                "Today, I move closer to my dreams.",
                "My mind is focused; my heart and spirit are ready.",
                "Challenges are opportunities for growth.",
                "I deserve success, happiness, and fulfillment.",
                "I learn, evolve, and improve daily.",
                "My actions spread positivity.",
                "I am thankful for every experience.",
                "I believe in my vision and trust my journey.",
                "I radiate positivity and resilience.",
                "Every step is toward my true potential.",
                "Daily, I grow stronger in my purpose."
              ].map((text, idx) => (
                <div key={idx} style={{
                  display: 'flex',
                  alignItems: 'flex-start',
                  gap: '1rem',
                  padding: '0.75rem',
                  background: 'white',
                  borderLeft: '3px solid #c9a961',
                  boxShadow: '0 1px 3px rgba(0,0,0,0.05)'
                }}>
                  <div style={{
                    color: '#c9a961',
                    fontWeight: 600,
                    fontSize: '1.2rem',
                    flexShrink: 0
                  }}>•</div>
                  <div style={{ fontStyle: 'italic', lineHeight: '1.7', fontSize: '0.95rem' }}>
                    {text}
                  </div>
                </div>
              ))}
            </div>
          </div>

          <p style={{
            textAlign: 'center',
            margin: '2rem 0 1rem',
            fontWeight: 500,
            lineHeight: '1.7'
          }}>
            Repeat these affirmations daily to remind yourself of your strength and potential.
          </p>
        </div>
      )
    },
    {
      type: 'preface',
      name: '7-Preface.xhtml',
      content: (
        <div className="page page--content">
          <div style={{ textAlign: 'center', marginBottom: '2.5rem' }}>
            <BookOpen size={32} style={{ color: '#c9a961', margin: '0 auto 1rem' }} />
            <h2 style={{
              fontFamily: 'Cinzel Decorative, serif',
              fontSize: '1.75rem',
              margin: '0 0 1.5rem',
              color: '#2c1810'
            }}>
              PREFACE
            </h2>
            <div style={{
              width: '60px',
              height: '2px',
              background: 'linear-gradient(to right, transparent, #c9a961, transparent)',
              margin: '0 auto'
            }} />
          </div>

          <h3 style={{
            fontSize: '1.3rem',
            fontWeight: 600,
            margin: '2rem 0 1.5rem',
            color: '#2c1810'
          }}>
            Introduction to The Artisan's Path
          </h3>

          <p style={{
            fontSize: '1.125rem',
            margin: '0 0 1.5rem',
            lineHeight: '1.8'
          }}>
            <span style={{
              float: 'left',
              fontSize: '3.5em',
              lineHeight: '0.9',
              marginRight: '0.1em',
              fontWeight: 'bold',
              color: '#c9a961',
              fontFamily: 'Cinzel Decorative, serif'
            }}>T</span>
            he creative spirit stirs, restless and unbounded by four walls. The familiar rhythms of appointment books and studio lighting begin to feel like beautiful constraints rather than destinations. In this pivotal moment of yearning for something more, <em style={{ fontStyle: 'italic', color: '#5a4a3a' }}>The Artisan's Path</em> was born—not merely as a book, but as a manifesto for those who sense that their artistry deserves a canvas larger than the chair, a stage greater than the salon floor.
          </p>

          <p style={{ margin: '0 0 1rem', lineHeight: '1.7' }}>
            What you hold in your hands is a roadmap for the ambitious hairstylist who gazes beyond the horizon. This is not simply another guide to perfect your technique; it is a companion for your exodus from the conventional, illuminating pathways to expression, entrepreneurship, and expansion that exist when you dare to redefine what it means to be a hair artist in today's boundless landscape.
          </p>

          <p style={{ margin: '0 0 1rem', lineHeight: '1.7' }}>
            Throughout these chapters, I share not only the strategies that liberated my career from the confines of a single location, but the profound inner transformations required to reimagine my identity as an artist without borders. You'll witness the unfiltered journey of reinvention: from salon dependent to location independent, from service provider to content creator, from employee to visionary entrepreneur whose influence transcends physical space.
          </p>

          <p style={{ margin: '0 0 1rem', lineHeight: '1.7' }}>
            In a profession where most are taught that success means a loyal clientele and a busy chair, we face unique challenges when seeking to build something more expansive. Here, we redefine success entirely. The fear of walking away from consistent bookings? The catalyst for creating multiple revenue streams. The uncertainty of building a personal brand? Your gateway to genuine artistic freedom. The vertigo of entrepreneurial risk? The foundation of an empire that travels wherever your creativity leads.
          </p>

          <p style={{ margin: '0 0 1rem', lineHeight: '1.7' }}>
            <em style={{ fontStyle: 'italic', color: '#5a4a3a' }}>The Artisan's Path</em> invites you to break through the invisible ceiling that keeps too many brilliant artists tethered to a single mode of expression. Within these pages, you'll discover how to translate your technical mastery into diverse opportunities—editorial work, education platforms, product development, digital content, and business models that generate income while you sleep.
          </p>

          <p style={{ margin: '0 0 1rem', lineHeight: '1.7' }}>
            As you turn each page, embrace the identity of pioneer rather than practitioner, of creator rather than service provider, of visionary rather than technician. The wisdom captured here isn't meant to simply improve your existing career, but to completely reimagine what's possible when you liberate your talents from traditional expectations and physical limitations.
          </p>

          <p style={{ margin: '0 0 1rem', lineHeight: '1.7' }}>
            Welcome to your professional metamorphosis. Welcome to a life and career designed entirely on your terms. Welcome to <em style={{ fontStyle: 'italic', color: '#5a4a3a' }}>The Artisan's Path</em>.
          </p>

          <div style={{
            marginTop: '3rem',
            paddingTop: '2rem',
            borderTop: '1px solid #e0d5c7'
          }}>
            <div style={{ width: '150px', height: '1px', background: '#c9a961', margin: '0 0 1rem 0' }}></div>
            <p style={{ fontStyle: 'italic', margin: '0.5rem 0', opacity: 0.85 }}>
              With boundless creativity and unwavering belief in your journey beyond the chair,
            </p>
            <p style={{
              fontWeight: 600,
              fontSize: '1.125rem',
              margin: '1rem 0 0',
              color: '#2c1810'
            }}>
              Curls Contemporary Collective
            </p>
            <div style={{
              width: '40px',
              height: '2px',
              background: '#c9a961',
              margin: '2rem 0 0'
            }}></div>
          </div>
        </div>
      )
    }
  ];

  const nextPage = () => {
    if (currentPage < pages.length - 1) {
      setCurrentPage(currentPage + 1);
    }
  };

  const prevPage = () => {
    if (currentPage > 0) {
      setCurrentPage(currentPage - 1);
    }
  };

  return (
    <div style={{
      minHeight: '100vh',
      background: 'linear-gradient(to bottom, #f8f6f3 0%, #ebe7e0 100%)',
      padding: '2rem 1rem',
      fontFamily: 'Georgia, serif'
    }}>
      <style>{`
        @import url('https://fonts.googleapis.com/css2?family=Cinzel+Decorative:wght@400;700&family=Libre+Baskerville:ital,wght@0,400;0,700;1,400&display=swap');

        body {
          -webkit-hyphens: auto;
          hyphens: auto;
        }

        .page {
          max-width: 42rem;
          margin: 0 auto;
          padding: 2.5rem 2rem;
          box-sizing: border-box;
          background: white;
          min-height: 75vh;
          box-shadow: 0 4px 20px rgba(0,0,0,0.08);
          font-family: 'Libre Baskerville', serif;
          line-height: 1.7;
          border-radius: 2px;
        }

        .page--worksheet {
          padding: 1.5rem 2rem;
        }
      `}</style>

      <div style={{
        maxWidth: '48rem',
        margin: '0 auto',
        marginBottom: '2rem'
      }}>
        <div style={{
          display: 'flex',
          justifyContent: 'space-between',
          alignItems: 'center',
          marginBottom: '1rem',
          flexWrap: 'wrap',
          gap: '1rem'
        }}>
          <div>
            <h1 style={{
              fontSize: '1.5rem',
              fontWeight: 600,
              color: '#2c1810',
              margin: '0 0 0.25rem',
              fontFamily: 'Cinzel Decorative, serif'
            }}>
              The Artisan's Path
            </h1>
            <p style={{
              fontSize: '0.875rem',
              color: '#5a4a3a',
              margin: 0,
              opacity: 0.8
            }}>
              Frontmatter Pages Preview (Rebranded)
            </p>
          </div>
          <div style={{
            fontSize: '0.875rem',
            color: '#2c1810',
            background: 'white',
            padding: '0.75rem 1.25rem',
            borderRadius: '6px',
            boxShadow: '0 2px 8px rgba(0,0,0,0.06)',
            border: '1px solid #e0d5c7'
          }}>
            <div style={{ fontWeight: 600, marginBottom: '0.25rem' }}>
              Page {currentPage + 1} of {pages.length}
            </div>
            <div style={{
              fontSize: '0.75rem',
              color: '#c9a961',
              textTransform: 'uppercase',
              letterSpacing: '0.5px'
            }}>
              {pages[currentPage].name}
            </div>
          </div>
        </div>
      </div>

      {pages[currentPage].content}

      <div style={{
        maxWidth: '48rem',
        margin: '2rem auto 0',
        display: 'flex',
        justifyContent: 'space-between',
        alignItems: 'center',
        gap: '1rem'
      }}>
        <button
          onClick={prevPage}
          disabled={currentPage === 0}
          style={{
            display: 'flex',
            alignItems: 'center',
            gap: '0.5rem',
            padding: '0.875rem 1.75rem',
            background: currentPage === 0 ? '#e0d5c7' : '#c9a961',
            color: currentPage === 0 ? '#999' : '#2c1810',
            border: 'none',
            borderRadius: '6px',
            cursor: currentPage === 0 ? 'not-allowed' : 'pointer',
            fontSize: '1rem',
            fontWeight: 600,
            transition: 'all 0.3s',
            boxShadow: currentPage === 0 ? 'none' : '0 2px 8px rgba(201, 169, 97, 0.3)'
          }}
        >
          <ChevronLeft size={20} />
          Previous
        </button>

        <div style={{
          display: 'flex',
          gap: '0.5rem',
          alignItems: 'center'
        }}>
          {pages.map((_, idx) => (
            <button
              key={idx}
              onClick={() => setCurrentPage(idx)}
              style={{
                width: idx === currentPage ? '24px' : '10px',
                height: '10px',
                borderRadius: '5px',
                border: 'none',
                background: idx === currentPage ? '#c9a961' : '#d0c8bc',
                cursor: 'pointer',
                transition: 'all 0.3s'
              }}
              aria-label={`Go to page ${idx + 1}`}
            />
          ))}
        </div>

        <button
          onClick={nextPage}
          disabled={currentPage === pages.length - 1}
          style={{
            display: 'flex',
            alignItems: 'center',
            gap: '0.5rem',
            padding: '0.875rem 1.75rem',
            background: currentPage === pages.length - 1 ? '#e0d5c7' : '#c9a961',
            color: currentPage === pages.length - 1 ? '#999' : '#2c1810',
            border: 'none',
            borderRadius: '6px',
            cursor: currentPage === pages.length - 1 ? 'not-allowed' : 'pointer',
            fontSize: '1rem',
            fontWeight: 600,
            transition: 'all 0.3s',
            boxShadow: currentPage === pages.length - 1 ? 'none' : '0 2px 8px rgba(201, 169, 97, 0.3)'
          }}
        >
          Next
          <ChevronRight size={20} />
        </button>
      </div>
    </div>
  );
};

export default ArtisanPathViewer;
