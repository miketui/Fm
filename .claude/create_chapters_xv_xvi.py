#!/usr/bin/env python3
import re

# Read source files
with open('HOME/OEBPS/text/26-chapter-xv-cultivating-resilience-and-well-being-in-hairstyling.xhtml', 'r') as f:
    ch15_src = f.read()
with open('HOME/OEBPS/text/27-chapter-xvi-tresses-and-textures-embracing-diversity-in-hairstyling.xhtml', 'r') as f:
    ch16_src = f.read()

# Extract functions
def get_intro(src):
    m = re.search(r'<div class="introduction-paragraph dropcap-first-letter">(.*?)</div>', src, re.DOTALL)
    return m.group(1).strip() if m else ""

def get_bible(src):
    q = re.search(r'<blockquote class="bible-quote-text"[^>]*>(.*?)</blockquote>', src, re.DOTALL)
    r = re.search(r'<figcaption class="bible-quote-reference"[^>]*>(.*?)</figcaption>', src, re.DOTALL)
    return (q.group(1).strip() if q else "", r.group(1).strip() if r else "")

def get_body(src):
    m = re.search(r'<div class="content-area">(.*?)</div>\s*(?:<aside class="endnotes|</section>)', src, re.DOTALL)
    return m.group(1).strip() if m else ""

def get_endnotes(src):
    m = re.search(r'<aside class="endnotes[^"]*"[^>]*>\s*(<ol>.*?</ol>)\s*</aside>', src, re.DOTALL)
    return m.group(1).strip() if m else None

# Process CH XV
ch15 = {
    'intro': get_intro(ch15_src),
    'quote': get_bible(ch15_src),
    'body': get_body(ch15_src),
    'endnotes': get_endnotes(ch15_src)
}

# Process CH XVI  
ch16 = {
    'intro': get_intro(ch16_src),
    'quote': get_bible(ch16_src),
    'body': get_body(ch16_src),
    'endnotes': get_endnotes(ch16_src)
}

# Build Chapter XV XHTML
ch15_xhtml = f'''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" lang="en" xml:lang="en">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Chapter XV – Cultivating Resilience and Well-Being in Hairstyling</title>
  <link rel="stylesheet" type="text/css" href="../styles/fonts.css"/>
  <link rel="stylesheet" type="text/css" href="../styles/style.css"/>
  <link rel="stylesheet" type="text/css" href="../styles/print.css" media="print"/>
</head>
<body class="chapter-page">
  <main epub:type="bodymatter chapter" role="main">
    <section class="chap-title" role="region" aria-label="Chapter XV Title">
      <figure class="chapter-number-figure" role="group" aria-label="Chapter number XV">
        <img class="chapter-number-brush" src="../images/brushstroke.svg" alt="Decorative brushstroke background"/>
        <figcaption class="chapter-number-roman">XV</figcaption>
      </figure>
      <div class="title-stack">
        <div class="title-bar" aria-hidden="true"></div>
        <div class="title-lines">
          <div class="title-line">Cultivating</div>
          <div class="title-line">Resilience</div>
          <div class="title-line">and</div>
          <div class="title-line">Well-Being</div>
          <div class="title-line">in</div>
          <div class="title-line">Hairstyling</div>
        </div>
      </div>
      <figure class="bible-quote-container" role="group" aria-labelledby="bq-text bq-ref">
        <blockquote class="bible-quote-text" id="bq-text">
          {ch15['quote'][0]}
        </blockquote>
        <figcaption class="bible-quote-reference" id="bq-ref">{ch15['quote'][1]}</figcaption>
      </figure>
      <h2 class="introduction-heading">Introduction</h2>
      <div class="introduction-paragraph dropcap-first-letter">
        {ch15['intro']}
      </div>
    </section>
    <div class="page-break"></div>
    <section class="chap-body" role="region" aria-label="Chapter content">
      <div class="content-area">
{ch15['body']}
      </div>
    </section>
    <section class="endnotes" role="region" aria-label="Endnotes">
      <h2 class="endnotes-title">Endnotes</h2>
      {ch15['endnotes']}
    </section>
    <div class="page-break"></div>
    <section class="quiz-container chap-quiz page-break-before avoid-break" role="region" aria-labelledby="quiz-title">
      <h2 id="quiz-title" class="quiz-title">Chapter Quiz</h2>
      <div class="quiz-question-block">
        <p class="quiz-question"><strong>1. The chapter's burnout self-assessment tool serves what purpose?</strong></p>
        <ul class="quiz-options">
          <li class="quiz-option"><span class="opt-label">A)</span> To make stylists feel guilty about struggling</li>
          <li class="quiz-option"><span class="opt-label">B)</span> To provide awareness of burnout symptoms and prompt proactive intervention</li>
          <li class="quiz-option"><span class="opt-label">C)</span> Burnout assessments are unnecessary</li>
          <li class="quiz-option"><span class="opt-label">D)</span> To diagnose clinical mental health conditions</li>
        </ul>
      </div>
      <div class="quiz-question-block">
        <p class="quiz-question"><strong>2. When building resilience through a growth mindset, the chapter recommends:</strong></p>
        <ul class="quiz-options">
          <li class="quiz-option"><span class="opt-label">A)</span> Avoiding all challenges and setbacks</li>
          <li class="quiz-option"><span class="opt-label">B)</span> Viewing failures as personal deficiencies</li>
          <li class="quiz-option"><span class="opt-label">C)</span> Reframing challenges as opportunities to learn, adapt, and strengthen your capacity</li>
          <li class="quiz-option"><span class="opt-label">D)</span> Pretending difficulties don't affect you</li>
        </ul>
      </div>
      <div class="quiz-question-block">
        <p class="quiz-question"><strong>3. The SMART goal methodology emphasized in the chapter helps with:</strong></p>
        <ul class="quiz-options">
          <li class="quiz-option"><span class="opt-label">A)</span> Making vague wishes about the future</li>
          <li class="quiz-option"><span class="opt-label">B)</span> Creating Specific, Measurable, Achievable, Relevant, and Time-bound goals that drive meaningful progress</li>
          <li class="quiz-option"><span class="opt-label">C)</span> Setting impossible standards to push yourself</li>
          <li class="quiz-option"><span class="opt-label">D)</span> Goals are unnecessary if you're passionate</li>
        </ul>
      </div>
      <div class="quiz-question-block">
        <p class="quiz-question"><strong>4. According to the chapter, why is building a support network critical for resilience?</strong></p>
        <ul class="quiz-options">
          <li class="quiz-option"><span class="opt-label">A)</span> Support networks are only for weak people</li>
          <li class="quiz-option"><span class="opt-label">B)</span> You should handle everything alone to prove your strength</li>
          <li class="quiz-option"><span class="opt-label">C)</span> Community, mentorship, and professional support provide perspective, encouragement, and resources during challenges</li>
          <li class="quiz-option"><span class="opt-label">D)</span> Support networks create dependency</li>
        </ul>
      </div>
      <p style="margin-top: 2rem; text-align: center; font-style: italic;">
        For answers, see the Quiz Key in the backmatter.
      </p>
    </section>
    <div class="page-break"></div>
    <section class="worksheet page-break-before avoid-break" role="region" aria-labelledby="ws-title">
      <h2 id="ws-title" class="worksheet-title">Chapter Worksheet</h2>
      <div class="activity-section">
        <p><strong>Reflection Questions:</strong></p>
        <p>Take time to consider how this chapter's concepts apply to your own experience and practice.</p>
        <ol>
          <li>
            <p><strong>Complete the burnout self-assessment from the chapter. What is your current resilience level? What warning signs do you notice?</strong></p>
            <div class="writing-area ruled-paper-bg" style="min-height: 8rem;"></div>
          </li>
          <li>
            <p><strong>Identify a recent professional challenge. How did you respond? Now reframe it using a growth mindset: What did you learn? How did it strengthen you?</strong></p>
            <div class="writing-area ruled-paper-bg" style="min-height: 8rem;"></div>
          </li>
          <li>
            <p><strong>Set 2-3 SMART goals for the next quarter. Ensure each goal is Specific, Measurable, Achievable, Relevant, and Time-bound.</strong></p>
            <div class="writing-area ruled-paper-bg" style="min-height: 8rem;"></div>
          </li>
          <li>
            <p><strong>Map your support network: Who provides emotional support, professional guidance, accountability, and inspiration? Where are gaps? How can you intentionally build community?</strong></p>
            <div class="writing-area ruled-paper-bg" style="min-height: 8rem;"></div>
          </li>
        </ol>
      </div>
    </section>
    <div class="page-break"></div>
    <section class="closing image-quote page-break-before" role="region" aria-label="Inspirational closing">
      <figure>
        <img src="../images/chapter-xv-quote.jpeg" alt="Inspirational quote: Believe in yourself and all that you are. Know that there is something inside you that is greater than any obstacle."/>
        <figcaption style="margin-top: 1rem; font-style: italic; color: #64748b;">
          Optional caption for the closing image
        </figcaption>
      </figure>
    </section>
  </main>
</body>
</html>
'''

# Build Chapter XVI XHTML  
ch16_xhtml = f'''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" lang="en" xml:lang="en">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Chapter XVI – Tresses and Textures - Embracing Diversity in Hairstyling</title>
  <link rel="stylesheet" type="text/css" href="../styles/fonts.css"/>
  <link rel="stylesheet" type="text/css" href="../styles/style.css"/>
  <link rel="stylesheet" type="text/css" href="../styles/print.css" media="print"/>
</head>
<body class="chapter-page">
  <main epub:type="bodymatter chapter" role="main">
    <section class="chap-title" role="region" aria-label="Chapter XVI Title">
      <figure class="chapter-number-figure" role="group" aria-label="Chapter number XVI">
        <img class="chapter-number-brush" src="../images/brushstroke.svg" alt="Decorative brushstroke background"/>
        <figcaption class="chapter-number-roman">XVI</figcaption>
      </figure>
      <div class="title-stack">
        <div class="title-bar" aria-hidden="true"></div>
        <div class="title-lines">
          <div class="title-line">Tresses</div>
          <div class="title-line">and</div>
          <div class="title-line">Textures</div>
          <div class="title-line">-</div>
          <div class="title-line">Embracing</div>
          <div class="title-line">Diversity</div>
          <div class="title-line">in</div>
          <div class="title-line">Hairstyling</div>
        </div>
      </div>
      <figure class="bible-quote-container" role="group" aria-labelledby="bq-text bq-ref">
        <blockquote class="bible-quote-text" id="bq-text">
          {ch16['quote'][0]}
        </blockquote>
        <figcaption class="bible-quote-reference" id="bq-ref">{ch16['quote'][1]}</figcaption>
      </figure>
      <h2 class="introduction-heading">Introduction</h2>
      <div class="introduction-paragraph dropcap-first-letter">
        {ch16['intro']}
      </div>
    </section>
    <div class="page-break"></div>
    <section class="chap-body" role="region" aria-label="Chapter content">
      <div class="content-area">
{ch16['body']}
      </div>
    </section>
    <section class="endnotes" role="region" aria-label="Endnotes">
      <h2 class="endnotes-title">Endnotes</h2>
      {ch16['endnotes']}
    </section>
    <div class="page-break"></div>
    <section class="quiz-container chap-quiz page-break-before avoid-break" role="region" aria-labelledby="quiz-title">
      <h2 id="quiz-title" class="quiz-title">Chapter Quiz</h2>
      <div class="quiz-question-block">
        <p class="quiz-question"><strong>1. The chapter's emphasis on understanding and honoring hair diversity serves what purpose?</strong></p>
        <ul class="quiz-options">
          <li class="quiz-option"><span class="opt-label">A)</span> It's a trend that will pass</li>
          <li class="quiz-option"><span class="opt-label">B)</span> Inclusive expertise expands your market, serves clients better, and honors the cultural significance of hair</li>
          <li class="quiz-option"><span class="opt-label">C)</span> Textured hair education is only for stylists of color</li>
          <li class="quiz-option"><span class="opt-label">D)</span> Diversity training is politically correct but not practically important</li>
        </ul>
      </div>
      <div class="quiz-question-block">
        <p class="quiz-question"><strong>2. The case study on "Transforming Client Experience Through Language" demonstrated:</strong></p>
        <ul class="quiz-options">
          <li class="quiz-option"><span class="opt-label">A)</span> Language and terminology don't matter in hair services</li>
          <li class="quiz-option"><span class="opt-label">B)</span> Using respectful, informed language creates trust, safety, and better client relationships</li>
          <li class="quiz-option"><span class="opt-label">C)</span> Clients don't notice or care about the words you use</li>
          <li class="quiz-option"><span class="opt-label">D)</span> Traditional industry terms should never be questioned</li>
        </ul>
      </div>
      <div class="quiz-question-block">
        <p class="quiz-question"><strong>3. When building an inclusive hair care practice, the chapter recommends:</strong></p>
        <ul class="quiz-options">
          <li class="quiz-option"><span class="opt-label">A)</span> Claiming expertise in all hair types without proper education</li>
          <li class="quiz-option"><span class="opt-label">B)</span> Refusing to serve hair types you're unfamiliar with</li>
          <li class="quiz-option"><span class="opt-label">C)</span> Investing in comprehensive education, using inclusive language, and creating a welcoming environment for all textures</li>
          <li class="quiz-option"><span class="opt-label">D)</span> Inclusion is only about marketing, not actual skill</li>
        </ul>
      </div>
      <div class="quiz-question-block">
        <p class="quiz-question"><strong>4. The chapter highlights cultural competency in textured hair care. What does this involve?</strong></p>
        <ul class="quiz-options">
          <li class="quiz-option"><span class="opt-label">A)</span> Treating all hair the same regardless of texture</li>
          <li class="quiz-option"><span class="opt-label">B)</span> Understanding the cultural, historical, and social significance of Black hair and textured hair care</li>
          <li class="quiz-option"><span class="opt-label">C)</span> Cultural competency is unnecessary if you have technical skills</li>
          <li class="quiz-option"><span class="opt-label">D)</span> Avoiding conversations about culture and race entirely</li>
        </ul>
      </div>
      <p style="margin-top: 2rem; text-align: center; font-style: italic;">
        For answers, see the Quiz Key in the backmatter.
      </p>
    </section>
    <div class="page-break"></div>
    <section class="worksheet page-break-before avoid-break" role="region" aria-labelledby="ws-title">
      <h2 id="ws-title" class="worksheet-title">Chapter Worksheet</h2>
      <div class="activity-section">
        <p><strong>Reflection Questions:</strong></p>
        <p>Take time to consider how this chapter's concepts apply to your own experience and practice.</p>
        <ol>
          <li>
            <p><strong>Assess your current expertise across hair textures: What textures are you confident serving? Where do you need education? Be honest about your gaps.</strong></p>
            <div class="writing-area ruled-paper-bg" style="min-height: 8rem;"></div>
          </li>
          <li>
            <p><strong>Create your textured hair education plan: Research 3-5 courses, workshops, or mentorship opportunities focused on diverse hair textures and cultural competency.</strong></p>
            <div class="writing-area ruled-paper-bg" style="min-height: 8rem;"></div>
          </li>
          <li>
            <p><strong>Audit your language and environment: Do your marketing, consultations, and salon language reflect inclusivity? What changes could make clients of all backgrounds feel welcomed and understood?</strong></p>
            <div class="writing-area ruled-paper-bg" style="min-height: 8rem;"></div>
          </li>
          <li>
            <p><strong>Reflect on representation: Does your portfolio, social media, and client base reflect the diversity of your community? If not, what systemic or skill barriers exist, and how can you address them?</strong></p>
            <div class="writing-area ruled-paper-bg" style="min-height: 8rem;"></div>
          </li>
        </ol>
      </div>
    </section>
    <div class="page-break"></div>
    <section class="closing image-quote page-break-before" role="region" aria-label="Inspirational closing">
      <figure>
        <img src="../images/chapter-xvi-quote.jpeg" alt="Inspirational quote: Believe in yourself and all that you are. Know that there is something inside you that is greater than any obstacle."/>
        <figcaption style="margin-top: 1rem; font-style: italic; color: #64748b;">
          Optional caption for the closing image
        </figcaption>
      </figure>
    </section>
  </main>
</body>
</html>
'''

# Write output files
with open('REBRANDED_OUTPUT/xhtml/26-chapter-xv-cultivating-resilience-and-well-being-in-hairstyling.xhtml', 'w') as f:
    f.write(ch15_xhtml)
with open('REBRANDED_OUTPUT/xhtml/27-chapter-xvi-tresses-and-textures-embracing-diversity-in-hairstyling.xhtml', 'w') as f:
    f.write(ch16_xhtml)

print("Successfully created Chapter XV and XVI files!")
