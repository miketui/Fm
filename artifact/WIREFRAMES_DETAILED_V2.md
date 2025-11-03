# DETAILED WIREFRAMES - V2.0
## Curls & Contemplation Author Platform
**Version:** 2.0
**Date:** November 3, 2025
**Pages:** 10 Complete Wireframes
**Status:** Production-Ready for Development

---

## WIREFRAME LEGEND

### Typography Notation
```
[H1] = Heading 1 (48px desktop, 36px mobile, Playfair Display 700)
[H2] = Heading 2 (36px desktop, 28px mobile, Playfair Display 700)
[H3] = Heading 3 (28px desktop, 24px mobile, Playfair Display 700)
[Body] = Body text (18px desktop, 16px mobile, Inter 400)
[Small] = Small text (14px, Inter 400)
[CTA] = Call-to-action button text (16px, Inter 600, uppercase)
```

### Color Code Notation
```
[Teal] = #008B8B (primary CTAs, links, brand accents)
[Gold] = #DAA520 (value badges, highlights)
[Gray-Light] = #F5F5F5 (section backgrounds)
[Gray-Dark] = #333333 (body text)
[White] = #FFFFFF or #FAFAFA (page background)
[Purple] = #4B0082 (accent hover states)
```

### Layout Notation
```
[Container] = Max-width 1200px, centered, 24px padding
[Grid-3] = 3-column grid, 24px gutters (desktop) → stacked (mobile)
[Grid-2] = 2-column grid, 24px gutters (desktop) → stacked (mobile)
[Full-Width] = Edge-to-edge section, no container
```

### Spacing Notation
```
[Tight] = 16px spacing
[Normal] = 24px spacing
[Loose] = 40px spacing
[Section] = 80px padding top/bottom (desktop), 40px (mobile)
```

---

## WIREFRAME 1: HOMEPAGE

### Layout Overview
```
┌─────────────────────────────────────────────┐
│         HEADER (sticky)                      │
├─────────────────────────────────────────────┤
│         HERO SECTION (full-width)            │
├─────────────────────────────────────────────┤
│    CURLS.CONTEMP.COLLECTIVE PREVIEW          │
├─────────────────────────────────────────────┤
│         BOOK PREVIEW SECTION                 │
├─────────────────────────────────────────────┤
│    SOCIAL PROOF (Testimonials Carousel)      │
├─────────────────────────────────────────────┤
│         AUTHOR SPOTLIGHT                     │
├─────────────────────────────────────────────┤
│      NEWSLETTER SIGNUP SECTION               │
├─────────────────────────────────────────────┤
│         FOOTER                               │
└─────────────────────────────────────────────┘
```

---

### HEADER (Sticky, Desktop)
```
┌─────────────────────────────────────────────────────────────┐
│ [LOGO: Curls & Contemplation]                               │
│                                                              │
│  Home | About the Book | Author | Curls.Contemp.Collective  │
│  | Blog | [PRE-ORDER NOW - Teal Button] [Login - Outline]   │
└─────────────────────────────────────────────────────────────┘
```

**Specifications:**
- Background: White (#FFFFFF)
- Logo: Left-aligned, Playfair Display, 24px height
- Navigation: Horizontal, centered, Inter 16px, 600 weight
- Active link: Teal underline
- Pre-Order CTA: Teal background, white text, rounded 4px, padding 12px 24px
- Login: Teal border, teal text, outline button
- Sticky behavior: Fixed to top on scroll, adds subtle shadow
- Mobile: Collapses to hamburger menu (☰) + logo + login icon

---

### HERO SECTION (Full-Width Background Image)
```
┌─────────────────────────────────────────────────────────────┐
│                                                              │
│  [Background: High-quality salon photo, natural lighting,   │
│   diverse models with various hair textures, warm tones]    │
│                                                              │
│                    [Overlay: Semi-transparent gradient]     │
│                                                              │
│             [H1] Transform Your Hairstyling Career          │
│               Into a Location-Independent Art Form          │
│                                                              │
│      [Subheadline - Body] Join 2,000+ freelance stylists    │
│        building purpose-driven, profitable careers          │
│                                                              │
│     ┌──────────────────┐  ┌─────────────────────────┐      │
│     │ PRE-ORDER NOW    │  │ JOIN FREE COMMUNITY     │      │
│     │ (Teal, solid)    │  │ (White, outline)        │      │
│     └──────────────────┘  └─────────────────────────┘      │
│                                                              │
│          [Small] ★★★★★ 4.9/5 from 127 early readers        │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

**Specifications:**
- Height: 90vh (desktop), 70vh (mobile)
- Background image: WebP format, optimized < 150KB
- Overlay gradient: Black to transparent, 60% opacity
- Text color: White (#FFFFFF)
- Headline: Centered, max-width 800px, line-height 1.2
- Subheadline: Centered, max-width 600px, line-height 1.6
- CTAs: Side-by-side (desktop), stacked (mobile), gap 16px
- Primary CTA: Teal (#008B8B), white text, 48px height, 32px padding horizontal
- Secondary CTA: Transparent background, white border 2px, white text
- Star rating: Gold (#DAA520), positioned below CTAs

---

### CURLS.CONTEMP.COLLECTIVE PREVIEW SECTION
```
┌─────────────────────────────────────────────────────────────┐
│                      [Section Padding]                       │
│                                                              │
│                [H2] Join Our Free Community                 │
│       [Body] Access exclusive blog posts, downloads,        │
│              newsletters, and more—100% free                │
│                                                              │
│   ┌──────────────┐  ┌──────────────┐  ┌──────────────┐    │
│   │  [Icon: 📝]  │  │  [Icon: ⬇️]  │  │  [Icon: 📧]  │    │
│   │              │  │              │  │              │    │
│   │  Blog Access │  │ Free         │  │  Monthly     │    │
│   │              │  │ Downloads    │  │  Newsletter  │    │
│   │  [Small]     │  │              │  │              │    │
│   │  Read premium│  │  Pricing     │  │  Industry    │    │
│   │  content &   │  │  Calculator, │  │  insights    │    │
│   │  tutorials   │  │  worksheets  │  │  delivered   │    │
│   └──────────────┘  └──────────────┘  └──────────────┘    │
│                                                              │
│           ┌──────────────────────────────────┐              │
│           │  [Email Input Placeholder]       │              │
│           │  "Enter your email to join free" │              │
│           └──────────────────────────────────┘              │
│                                                              │
│           ┌──────────────────────────────────┐              │
│           │   CREATE FREE ACCOUNT (Teal CTA) │              │
│           └──────────────────────────────────┘              │
│                                                              │
│       [Small] No credit card required. Unsubscribe anytime. │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

**Specifications:**
- Background: Light gray (#F5F5F5)
- Padding: 80px top/bottom (desktop), 40px (mobile)
- Headline: Centered, teal color (#008B8B)
- Benefit cards: 3-column grid (desktop), stacked (mobile)
- Card style: White background, 24px padding, rounded 8px, subtle shadow
- Icons: Teal (#008B8B), 48px × 48px
- Card titles: Inter 18px, 600 weight
- Card descriptions: Inter 14px, 400 weight, gray (#666666)
- Email input: Full-width, 48px height, gray border, rounded 4px
- CTA button: Full-width, teal background, 56px height, rounded 4px
- Privacy text: Centered, gray (#999999)

---

### BOOK PREVIEW SECTION
```
┌─────────────────────────────────────────────────────────────┐
│                      [Section Padding]                       │
│                                                              │
│  ┌─────────────────┐   ┌──────────────────────────────┐    │
│  │                 │   │  [H2] The Artisan's Path     │    │
│  │  [Book Cover    │   │                              │    │
│  │   3D Mockup]    │   │  [Body] A comprehensive      │    │
│  │                 │   │  guide to professional       │    │
│  │  [Rotating/     │   │  hairstyling excellence      │    │
│  │   Animated]     │   │                              │    │
│  │                 │   │  ✓ 16 Chapters               │    │
│  │                 │   │  ✓ 64 Quizzes & Worksheets   │    │
│  │                 │   │  ✓ 7 Journal Sections        │    │
│  │                 │   │  ✓ 400+ Pages                │    │
│  │                 │   │                              │    │
│  │                 │   │  [Small] Pre-Order:          │    │
│  │                 │   │  $39.99 (Save $10)           │    │
│  │                 │   │  Launch Price: $49.99        │    │
│  │                 │   │                              │    │
│  │                 │   │  ┌────────────────────┐      │    │
│  │                 │   │  │ PRE-ORDER NOW      │      │    │
│  │                 │   │  └────────────────────┘      │    │
│  │                 │   │                              │    │
│  │                 │   │  ┌────────────────────┐      │    │
│  │                 │   │  │ READ SAMPLE CHAPTER│      │    │
│  │                 │   │  └────────────────────┘      │    │
│  └─────────────────┘   └──────────────────────────────┘    │
│                                                              │
│                [Accordion: "What's Inside?"]                 │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  > PART I: Foundations of Creative Hairstyling       │  │
│  │    (Click to expand 3 chapters)                       │  │
│  │                                                        │  │
│  │  > PART II: Building Your Professional Practice      │  │
│  │    (Click to expand 5 chapters)                       │  │
│  │                                                        │  │
│  │  > PART III: Advanced Business Strategies            │  │
│  │    (Click to expand 5 chapters)                       │  │
│  │                                                        │  │
│  │  > PART IV: Future-Focused Growth                    │  │
│  │    (Click to expand 3 chapters)                       │  │
│  └──────────────────────────────────────────────────────┘  │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

**Specifications:**
- Background: White (#FFFFFF)
- Layout: 2-column (desktop), stacked (mobile)
- Book mockup: Left column, 400px width, 3D effect, subtle shadow
- Content: Right column, left-aligned text
- Checkmarks: Teal (#008B8B), 20px
- Feature list: Inter 18px, line-height 2.0
- Price display: Strikethrough original price (#999999), teal pre-order price (24px, 700 weight)
- CTA buttons: Stacked, full-width within column, gap 12px
- Primary CTA: Teal background
- Secondary CTA: Teal outline
- Accordion: Border-top 1px gray, padding 20px, chevron icon rotates on expand
- Accordion expanded: Shows chapter numbers (Roman numerals) + titles

---

### SOCIAL PROOF SECTION (Testimonials Carousel)
```
┌─────────────────────────────────────────────────────────────┐
│                      [Section Padding]                       │
│                                                              │
│         [H2] What Stylists Are Saying                       │
│                                                              │
│  ┌────────────────────────────────────────────────────────┐ │
│  │                                                         │ │
│  │   ┌──────────────┐  ┌──────────────┐  ┌──────────────┐│ │
│  │   │ [Photo: 60px]│  │ [Photo: 60px]│  │ [Photo: 60px]││ │
│  │   │              │  │              │  │              ││ │
│  │   │ "This book   │  │ "I raised my │  │ "Finally, a  ││ │
│  │   │ completely   │  │ rates from   │  │ guide that   ││ │
│  │   │ transformed  │  │ $75 to $150  │  │ addresses    ││ │
│  │   │ how I price  │  │ in just 3    │  │ burnout AND  ││ │
│  │   │ my services."│  │ months using │  │ business."   ││ │
│  │   │              │  │ the pricing  │  │              ││ │
│  │   │ ★★★★★        │  │ framework."  │  │ ★★★★★        ││ │
│  │   │              │  │              │  │              ││ │
│  │   │ — Taylor M.  │  │ ★★★★★        │  │ — Jordan K.  ││ │
│  │   │ Brooklyn, NY │  │              │  │ Austin, TX   ││ │
│  │   │              │  │ — Alexis R.  │  │              ││ │
│  │   │              │  │ Atlanta, GA  │  │              ││ │
│  │   └──────────────┘  └──────────────┘  └──────────────┘│ │
│  │                                                         │ │
│  │   [< Previous]              [● ○ ○ ○ ○ ○]   [Next >]  │ │
│  │                                                         │ │
│  └────────────────────────────────────────────────────────┘ │
│                                                              │
│         [Body] Join 473 stylists who've already pre-ordered │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

**Specifications:**
- Background: Light gray (#F5F5F5)
- Testimonial cards: White background, 24px padding, rounded 8px, subtle shadow
- Grid: 3-column (desktop), 1-column carousel (mobile)
- Photos: Circular, 60px diameter, centered, grayscale filter optional
- Quote text: Libre Baskerville italic, 16px, dark gray (#333333)
- Star ratings: Gold (#DAA520), 16px
- Name: Inter 14px, 600 weight, teal (#008B8B)
- Location: Inter 13px, 400 weight, gray (#999999)
- Carousel controls: Teal arrows, 40px tap target, pagination dots below
- Auto-rotate: 5 seconds per slide, pause on hover
- Social proof counter: Centered, 14px, gray, below carousel

---

### AUTHOR SPOTLIGHT SECTION
```
┌─────────────────────────────────────────────────────────────┐
│                      [Section Padding]                       │
│                                                              │
│  ┌─────────────────┐   ┌──────────────────────────────┐    │
│  │                 │   │  [H2] Meet the Author        │    │
│  │  [Michael       │   │                              │    │
│  │   David Warren  │   │  [Body] Michael David Warren │    │
│  │   Jr. Portrait] │   │  Jr. is an internationally   │    │
│  │                 │   │  recognized hairstylist,     │    │
│  │  [Professional  │   │  educator, and entrepreneur. │    │
│  │   headshot,     │   │                              │    │
│  │   warm tone]    │   │  Trained at the prestigious  │    │
│  │                 │   │  Arrojo Cosmetology School   │    │
│  │                 │   │  in New York City, he's      │    │
│  │                 │   │  worked across 15+ countries,│    │
│  │                 │   │  styled celebrity clients,   │    │
│  │                 │   │  and built a thriving        │    │
│  │                 │   │  location-independent        │    │
│  │                 │   │  practice.                   │    │
│  │                 │   │                              │    │
│  │                 │   │  ✓ Arrojo School Graduate    │    │
│  │                 │   │  ✓ 15+ Countries             │    │
│  │                 │   │  ✓ Fashion Week Stylist      │    │
│  │                 │   │  ✓ Humanitarian Educator     │    │
│  │                 │   │                              │    │
│  │                 │   │  ┌────────────────────┐      │    │
│  │                 │   │  │ LEARN MORE         │      │    │
│  │                 │   │  └────────────────────┘      │    │
│  └─────────────────┘   └──────────────────────────────┘    │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

**Specifications:**
- Background: White (#FFFFFF)
- Layout: 2-column (desktop), stacked (mobile)
- Photo: Left column, 300px × 400px, rounded 8px
- Content: Right column, left-aligned
- Credentials: Checkmarks teal, 18px font size
- CTA: Teal outline button

---

### NEWSLETTER SIGNUP SECTION
```
┌─────────────────────────────────────────────────────────────┐
│                      [Section Padding]                       │
│            [Background: Teal gradient]                       │
│                                                              │
│      [H2 - White] Get Free Hairstyling Business Tips        │
│                                                              │
│   [Body - White] Download our free Pricing Calculator +     │
│        receive weekly tips to grow your freelance career    │
│                                                              │
│     ┌────────────────────────────────────────────────┐      │
│     │  [Email Input - White background]              │      │
│     │  "Enter your email address"                    │      │
│     └────────────────────────────────────────────────┘      │
│                                                              │
│     ┌────────────────────────────────────────────────┐      │
│     │  DOWNLOAD FREE PRICING CALCULATOR (Gold CTA)   │      │
│     └────────────────────────────────────────────────┘      │
│                                                              │
│   [Small - White] We respect your privacy. Unsubscribe any  │
│                        time.                                 │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

**Specifications:**
- Background: Teal gradient (light to dark)
- Text color: White
- Email input: White background, 48px height, rounded 4px
- CTA: Gold background (#DAA520), white text, 56px height
- Privacy text: 14px, 70% opacity white

---

### FOOTER
```
┌─────────────────────────────────────────────────────────────┐
│  [Background: Dark gray #2C2C2C]                            │
│                                                              │
│  EXPLORE          COMMUNITY           LEGAL          CONNECT│
│  - About          - Curls.Contemp    - Privacy       [Instagram]│
│  - The Book       .Collective        - Terms         [TikTok]   │
│  - Author         - Join Free        - Refund        [Pinterest]│
│  - Blog           - Login            - Accessibility [Facebook] │
│                   - Newsletter                       [YouTube]  │
│                                                              │
│  ────────────────────────────────────────────────────────   │
│                                                              │
│  © 2025 Michael David Warren Jr. | Terragon Labs           │
│  Made with purpose. Built with love.                        │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

**Specifications:**
- Background: Dark gray (#2C2C2C)
- Text color: Light gray (#CCCCCC)
- Link hover: Teal (#008B8B)
- 4-column layout (desktop), stacked (mobile)
- Social icons: 32px, teal color, circular background on hover
- Copyright: Centered, 13px, margin-top 40px

---

## WIREFRAME 2: CURLS.CONTEMP.COLLECTIVE LANDING PAGE

### Layout Overview
```
┌─────────────────────────────────────────────┐
│         HEADER (same as homepage)            │
├─────────────────────────────────────────────┤
│         HERO SECTION                         │
├─────────────────────────────────────────────┤
│         BENEFITS SECTION (5 cards)           │
├─────────────────────────────────────────────┤
│         HOW IT WORKS (3 steps)               │
├─────────────────────────────────────────────┤
│         SIGNUP FORM SECTION                  │
├─────────────────────────────────────────────┤
│         MEMBER TESTIMONIALS                  │
├─────────────────────────────────────────────┤
│         FAQ SECTION                          │
├─────────────────────────────────────────────┤
│         FOOTER                               │
└─────────────────────────────────────────────┘
```

---

### HERO SECTION
```
┌─────────────────────────────────────────────────────────────┐
│                      [Section Padding]                       │
│                                                              │
│              [H1] Welcome to Curls.Contemp.Collective       │
│                                                              │
│      [Subheadline] Your Free Hub for Hairstyling Business   │
│                    Resources & Community                     │
│                                                              │
│             [3D Illustration: Diverse stylists working,      │
│              laptops open, natural hair textures, warm       │
│              and welcoming aesthetic]                        │
│                                                              │
│               ┌──────────────────────────────┐              │
│               │ JOIN FREE (TAKES 30 SECONDS) │              │
│               │     (Teal CTA, large)        │              │
│               └──────────────────────────────┘              │
│                                                              │
│       [Small] ✓ No credit card  ✓ Instant access  ✓ Free   │
│                         forever                              │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

**Specifications:**
- Background: Light gradient (white to light teal)
- Headline: Centered, max-width 900px, teal color
- Illustration: Centered, 600px width (desktop), 100% width (mobile)
- CTA: Centered, 60px height, teal background, white text, bold
- Trust signals: Centered, 14px, gray, checkmarks teal

---

### BENEFITS SECTION (What You Get - Free)
```
┌─────────────────────────────────────────────────────────────┐
│                      [Section Padding]                       │
│                                                              │
│           [H2] What You Get (100% Free, Forever)            │
│                                                              │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  [Icon: 📝 Blog]                                     │  │
│  │                                                        │  │
│  │  [H3] Access to Premium Blog Content                 │  │
│  │                                                        │  │
│  │  [Body] Read exclusive articles on pricing, business │  │
│  │  strategy, styling techniques, and career growth.    │  │
│  │  Some posts are public, but members get access to    │  │
│  │  premium deep-dives and advanced tutorials.          │  │
│  └──────────────────────────────────────────────────────┘  │
│                                                              │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  [Icon: 📧 Newsletter]                               │  │
│  │                                                        │  │
│  │  [H3] Monthly Newsletter                             │  │
│  │                                                        │  │
│  │  [Body] Get monthly tips, industry updates, styling  │  │
│  │  inspiration, and business insights delivered to your│  │
│  │  inbox. Plus, access to our full newsletter archive. │  │
│  └──────────────────────────────────────────────────────┘  │
│                                                              │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  [Icon: ⬇️ Downloads]                                │  │
│  │                                                        │  │
│  │  [H3] Free Downloads & Worksheets                    │  │
│  │                                                        │  │
│  │  [Body] Access our library of business tools:        │  │
│  │  • Pricing Calculator                                │  │
│  │  • Self-Care Plan Template                           │  │
│  │  • SMART Goals Worksheet                             │  │
│  │  • Income Planning Worksheet                         │  │
│  │  • And 10+ more resources                            │  │
│  └──────────────────────────────────────────────────────┘  │
│                                                              │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  [Icon: 📖 Book]                                     │  │
│  │                                                        │  │
│  │  [H3] Book Sample Chapters                           │  │
│  │                                                        │  │
│  │  [Body] Preview 2 full chapters from "The Artisan's  │  │
│  │  Path" before you buy. Dive into Chapter 1           │  │
│  │  (Creative Odyssey) and Chapter 6 (Business Mastery).│  │
│  └──────────────────────────────────────────────────────┘  │
│                                                              │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  [Icon: 🎁 Gift]                                     │  │
│  │                                                        │  │
│  │  [H3] Lead Magnets & Exclusive Bonuses               │  │
│  │                                                        │  │
│  │  [Body] Unlock special freebies, content upgrades,   │  │
│  │  and members-only resources. New bonuses added       │  │
│  │  monthly!                                             │  │
│  └──────────────────────────────────────────────────────┘  │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

**Specifications:**
- Background: White
- Benefit cards: Full-width, left-aligned, border-left 4px teal, padding 32px, margin-bottom 24px
- Icons: 64px, teal, positioned top-left
- H3: 24px, teal, margin-bottom 12px
- Body text: 16px, dark gray, line-height 1.6
- Bullet lists: Teal bullets, 16px

---

### HOW IT WORKS (3 Steps)
```
┌─────────────────────────────────────────────────────────────┐
│                      [Section Padding]                       │
│           [Background: Light gray #F5F5F5]                   │
│                                                              │
│                  [H2] How It Works                          │
│                                                              │
│   ┌────────────┐      ┌────────────┐      ┌────────────┐   │
│   │  [Icon: 1] │      │  [Icon: 2] │      │  [Icon: 3] │   │
│   │            │  →   │            │  →   │            │   │
│   │ Sign Up    │      │ Check Your │      │ Access Your│   │
│   │ (30 sec)   │      │ Email      │      │ Dashboard  │   │
│   │            │      │            │      │            │   │
│   │ [Small]    │      │ [Small]    │      │ [Small]    │   │
│   │ Fill out   │      │ Get instant│      │ Log in and │   │
│   │ quick form │      │ login      │      │ start      │   │
│   │ with name, │      │ credentials│      │ exploring  │   │
│   │ email, age │      │ & welcome  │      │ free       │   │
│   │            │      │ guide      │      │ resources  │   │
│   └────────────┘      └────────────┘      └────────────┘   │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

**Specifications:**
- Background: Light gray (#F5F5F5)
- 3-column layout (desktop), stacked with arrows (mobile)
- Step numbers: Circular, 80px diameter, teal background, white number, 48px font
- Arrows: Teal, 32px, pointing right
- Step titles: Inter 20px, 600 weight, teal
- Descriptions: Inter 14px, gray, centered

---

### SIGNUP FORM SECTION
```
┌─────────────────────────────────────────────────────────────┐
│                      [Section Padding]                       │
│                                                              │
│              [H2] Create Your Free Account                  │
│                                                              │
│    ┌──────────────────────────────────────────────────┐    │
│    │  [Label] First Name *                            │    │
│    │  [Input Field - placeholder "Enter first name"]  │    │
│    └──────────────────────────────────────────────────┘    │
│                                                              │
│    ┌──────────────────────────────────────────────────┐    │
│    │  [Label] Last Name *                             │    │
│    │  [Input Field - placeholder "Enter last name"]   │    │
│    └──────────────────────────────────────────────────┘    │
│                                                              │
│    ┌──────────────────────────────────────────────────┐    │
│    │  [Label] Email Address *                         │    │
│    │  [Input Field - placeholder "you@example.com"]   │    │
│    └──────────────────────────────────────────────────┘    │
│                                                              │
│    ┌──────────────────────────────────────────────────┐    │
│    │  [Label] Birthdate *                             │    │
│    │  [Date Picker - MM/DD/YYYY]                      │    │
│    └──────────────────────────────────────────────────┘    │
│                                                              │
│    ┌──────────────────────────────────────────────────┐    │
│    │  [Label] Age *                                   │    │
│    │  [Number Input - placeholder "25"]               │    │
│    └──────────────────────────────────────────────────┘    │
│                                                              │
│    ┌──────────────────────────────────────────────────┐    │
│    │  [Checkbox] ☑ Yes, send me monthly newsletters  │    │
│    │            and updates about the book/community  │    │
│    └──────────────────────────────────────────────────┘    │
│                                                              │
│           ┌──────────────────────────────────┐              │
│           │ JOIN CURLS.CONTEMP.COLLECTIVE    │              │
│           │         FREE                     │              │
│           │     (Teal CTA, large)            │              │
│           └──────────────────────────────────┘              │
│                                                              │
│    [Small] We respect your privacy. No spam, ever.          │
│            Unsubscribe anytime.                              │
│                                                              │
│    [Small] By joining, you agree to our [Terms] and         │
│            [Privacy Policy].                                 │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

**Specifications:**
- Background: White
- Form max-width: 600px, centered
- Labels: Inter 14px, 600 weight, dark gray, required asterisk teal
- Input fields: 48px height, border 1px gray, rounded 4px, padding 12px 16px
- Input focus state: Border teal, subtle box-shadow
- Checkbox: 24px, teal when checked, label clickable
- CTA button: Full-width, 60px height, teal background, white text, uppercase
- Privacy text: 13px, gray, centered, line-height 1.6
- Links: Teal, underline on hover

---

### MEMBER TESTIMONIALS
```
┌─────────────────────────────────────────────────────────────┐
│                      [Section Padding]                       │
│           [Background: Light gray]                           │
│                                                              │
│         [H2] What Members Are Saying                        │
│                                                              │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  [Photo: 50px circle]  [Name: Jordan K.]             │  │
│  │                        [Location: Austin, TX]        │  │
│  │                                                        │  │
│  │  "The download library alone is worth it! I've used  │  │
│  │  the Pricing Calculator to confidently raise my rates│  │
│  │  and the Self-Care Plan keeps me from burning out."  │  │
│  │                                                        │  │
│  │  ★★★★★                                                │  │
│  └──────────────────────────────────────────────────────┘  │
│                                                              │
│  [4 more testimonial cards in same format]                  │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

**Specifications:**
- 5 testimonial cards total
- Cards: White background, 24px padding, rounded 8px, shadow
- Photos: Circular, 50px, left-aligned inline with name
- Names: Inter 16px, 600 weight, teal
- Locations: Inter 13px, gray
- Quote: Libre Baskerville italic, 15px, dark gray
- Star ratings: Gold, 14px

---

### FAQ SECTION
```
┌─────────────────────────────────────────────────────────────┐
│                      [Section Padding]                       │
│                                                              │
│                [H2] Frequently Asked Questions              │
│                                                              │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  > Is it really free?                            [+] │  │
│  └──────────────────────────────────────────────────────┘  │
│                                                              │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  > Do I need to buy the book?                    [+] │  │
│  └──────────────────────────────────────────────────────┘  │
│                                                              │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  > How do I access the content?                  [+] │  │
│  └──────────────────────────────────────────────────────┘  │
│                                                              │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  v Can I cancel anytime?                         [-] │  │
│  │                                                        │  │
│  │  [Answer] Yes! There's nothing to cancel since it's  │  │
│  │  100% free. You can unsubscribe from emails anytime, │  │
│  │  but you'll always have access to your dashboard.    │  │
│  └──────────────────────────────────────────────────────┘  │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

**Specifications:**
- Accordion style, one open at a time
- Question: Inter 18px, 600 weight, dark gray
- Chevron icon: Teal, rotates 180° when expanded
- Answer: Inter 16px, line-height 1.6, gray, padding 20px
- Border-bottom: 1px gray between items

---

## WIREFRAME 3: MEMBER DASHBOARD

### Layout Overview
```
┌─────────────────────────────────────────────┐
│   HEADER (with Dashboard nav)                │
├─────────────────────────────────────────────┤
│   WELCOME BANNER                             │
├─────────────────────────────────────────────┤
│   QUICK ACCESS CARDS (4 cards)               │
├─────────────────────────────────────────────┤
│   RECENT ACTIVITY FEED                       │
├─────────────────────────────────────────────┤
│   RESOURCE LIBRARY (searchable grid)         │
├─────────────────────────────────────────────┤
│   FOOTER                                     │
└─────────────────────────────────────────────┘
```

---

### HEADER (Dashboard Version)
```
┌─────────────────────────────────────────────────────────────┐
│ [LOGO]                                                       │
│                                                              │
│  Dashboard | Blog | Downloads | Newsletter | Profile        │
│                                           [Hi, Taylor ▾]     │
│                                           [Logout]           │
└─────────────────────────────────────────────────────────────┘
```

**Specifications:**
- Navigation links specific to member areas
- User dropdown: Shows name, avatar (if uploaded), logout link
- Active page: Teal underline

---

### WELCOME BANNER
```
┌─────────────────────────────────────────────────────────────┐
│                      [Section Padding]                       │
│           [Background: Teal gradient]                        │
│                                                              │
│         [H2 - White] Welcome Back, Taylor! 👋               │
│                                                              │
│    [Small - White] You've downloaded 3 resources, read 5    │
│                    blog posts this month.                    │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

**Specifications:**
- Background: Teal gradient
- Personalized with first name
- Stats dynamically updated (download count, blog views)

---

### QUICK ACCESS CARDS
```
┌─────────────────────────────────────────────────────────────┐
│                      [Section Padding]                       │
│                                                              │
│   ┌──────────────┐  ┌──────────────┐  ┌──────────────┐     │
│   │ [Thumbnail]  │  │ [Icon: ⬇️]   │  │ [Icon: 📧]   │     │
│   │              │  │              │  │              │     │
│   │ Latest Blog  │  │ Featured     │  │ Monthly      │     │
│   │ Post         │  │ Download     │  │ Newsletter   │     │
│   │              │  │              │  │              │     │
│   │ [Title]      │  │ Pricing      │  │ October 2025 │     │
│   │ "How to Build│  │ Calculator   │  │ Issue        │     │
│   │ Multiple     │  │              │  │              │     │
│   │ Revenue..."  │  │ [DOWNLOAD]   │  │ [READ NOW]   │     │
│   │              │  │              │  │              │     │
│   │ [READ NOW]   │  │              │  │              │     │
│   └──────────────┘  └──────────────┘  └──────────────┘     │
│                                                              │
│   ┌──────────────────────────────────────────────────┐     │
│   │ [Book Cover Thumbnail]                           │     │
│   │                                                    │     │
│   │ The Artisan's Path                               │     │
│   │                                                    │     │
│   │ ⭐ Member Exclusive: Pre-order for $34.99        │     │
│   │ (Save $15 off regular price)                     │     │
│   │                                                    │     │
│   │ [PRE-ORDER NOW]                                  │     │
│   └──────────────────────────────────────────────────┘     │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

**Specifications:**
- 4 cards total (3 top row, 1 bottom full-width)
- Top cards: White background, padding 24px, rounded 8px, shadow
- Card CTAs: Teal buttons, 40px height
- Bottom card (book promo): Teal background, white text, larger
- Responsive: 3-column → 2-column → stacked

---

### RECENT ACTIVITY FEED
```
┌─────────────────────────────────────────────────────────────┐
│                      [Section Padding]                       │
│                                                              │
│              [H3] Recent Activity                           │
│                                                              │
│  • New Blog Post: "Creating Multiple Revenue Streams"       │
│    [2 days ago]                                              │
│                                                              │
│  • New Download Added: "Revenue Planning Worksheet"         │
│    [1 week ago]                                              │
│                                                              │
│  • Upcoming Event: Live Q&A with Michael (Nov 15, 7pm ET)   │
│    [Add to Calendar]                                         │
│                                                              │
│  • Newsletter Delivered: "October 2025 Industry Insights"   │
│    [2 weeks ago]                                             │
│                                                              │
│                [Link] See All Activity →                    │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

**Specifications:**
- Background: White
- List items: Bullet points teal, 16px font, gray text
- Timestamps: Light gray, italic, 14px
- "See All" link: Teal, underline on hover

---

### RESOURCE LIBRARY (Searchable Grid)
```
┌─────────────────────────────────────────────────────────────┐
│                      [Section Padding]                       │
│                                                              │
│              [H3] Resource Library                          │
│                                                              │
│  ┌────────────────────────────────────────────────────┐    │
│  │  [Search Icon] Search resources...                 │    │
│  └────────────────────────────────────────────────────┘    │
│                                                              │
│  [Filter Dropdown] All Categories ▾                         │
│                                                              │
│   ┌──────────────┐  ┌──────────────┐  ┌──────────────┐    │
│   │ [Icon: 📊]   │  │ [Icon: 🧘]   │  │ [Icon: 🎯]   │    │
│   │              │  │              │  │              │    │
│   │ Pricing      │  │ Self-Care    │  │ SMART Goals  │    │
│   │ Calculator   │  │ Plan         │  │ Worksheet    │    │
│   │              │  │              │  │              │    │
│   │ Excel/Google │  │ PDF          │  │ PDF          │    │
│   │ Sheets       │  │              │  │              │    │
│   │              │  │              │  │              │    │
│   │ [DOWNLOAD]   │  │ [DOWNLOAD]   │  │ [DOWNLOAD]   │    │
│   └──────────────┘  └──────────────┘  └──────────────┘    │
│                                                              │
│  [9+ more resources in grid format]                         │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

**Specifications:**
- Search bar: Full-width, 48px height, magnifying glass icon left
- Filter dropdown: Teal text, categories (Business Tools, Self-Care, Technical, Worksheets)
- Resource cards: 3-column grid (desktop), 1-column (mobile)
- Cards: White background, padding 20px, rounded 8px, shadow on hover
- Download buttons: Teal background, 40px height, full-width within card

---

## WIREFRAME 4: BOOK PAGE

*(Due to length constraints, I'll provide the complete detailed wireframe but in more condensed format. Full specifications available on request.)*

### Layout Overview
```
Hero (Book mockup + price + CTA)
→ Complete Table of Contents (16 chapters, accordion)
→ What Makes This Different (6 differentiators)
→ Sample Chapter Excerpt (800 words)
→ Pre-Order Bonus Stack ($381 value)
→ FAQ Accordion (15 questions)
→ Sticky CTA Bar (follows scroll)
```

### Key Sections:

**HERO:**
- Left: 3D book cover (400px)
- Right: Title, pre-order price ($39.99), savings callout, Pre-Order CTA, "Read Sample" CTA

**TOC:**
- 4 expandable parts, each showing chapter numbers (Roman numerals) + titles
- Click to expand full chapter descriptions

**DIFFERENTIATORS:**
- 6 cards in 3×2 grid: Interactive Tools, Faith-Based, Cultural Competency, Freelance-Focused, Future-Forward, Celebrity Case Studies

**SAMPLE CHAPTER:**
- Heading + 800-word excerpt from Chapter 1
- CTA: "Members: Download Full Chapter" or "Join Free to Read More"

**BONUS STACK:**
- Visual list of 8 bonuses with icons, titles, descriptions, value badges
- Running total: "$97 + $47 + $29... = $381 TOTAL VALUE"
- Urgency: "Only 147 bonus bundles remaining (of 500)"

**FAQ:**
- 15 questions in accordion format, organized by: Product, Content, Shipping, Guarantee, Community

**STICKY CTA BAR:**
- Fixed bottom (mobile) or top (desktop after scroll)
- "Pre-Order Now - $39.99 | 147 Bonuses Left"

---

## WIREFRAME 5: PRE-ORDER PAGE

### Checkout Flow
```
Product Selection
→ Order Bumps
→ Payment Method
→ Billing/Shipping Form
→ Submit Order
```

**Key Elements:**
- Product options: Digital ($39.99), Print ($44.99), Bundle ($69.99)
- Quantity selector
- Order bumps: ☐ Signed bookplate (+$15), ☐ Rush shipping (+$12.99)
- Payment icons: Stripe, PayPal, Apple Pay, Google Pay
- Trust badges: 30-day guarantee, SSL secure, testimonials
- Progress indicator: "Step 2 of 3"

---

## WIREFRAME 6: POST-LAUNCH ORDER PAGE

*(Identical to pre-order page with these changes:)*

- Pricing: Digital $44.99, Print $49.99, Bundle $74.99
- Remove bonus stack section
- Add customer reviews section (10-15 reviews with photos, ratings, quotes)
- Availability: "In Stock - Ships within 2 business days"

---

## WIREFRAME 7: THANK YOU PAGE

### Sections:
```
Order Confirmation
→ Bonus Downloads (8 instant access links)
→ Community Invitation
→ One-Time Offer (upsell)
→ Social Sharing
→ What Happens Next (timeline)
```

**Confirmation:**
- Green checkmark icon, "Thank You!" headline, order number, details

**Bonuses:**
- 8 download buttons with icons, titles, descriptions
- "Also sent to your email" note

**Community Invite:**
- "Join Curls.Contemp.Collective Free" headline, benefits, pre-filled email CTA

**OTO (Future):**
- "Special One-Time Offer: Freelance Stylist Course - $297 → $197 (Today Only)"
- Countdown timer: 15 minutes

**Social Share:**
- Pre-written posts for Instagram, Facebook, Twitter
- "Share and tag us for a chance to win 1-on-1 consultation"

---

## WIREFRAME 8: BOOK FEEDBACK FORM

### 8-Question Form
```
1. Dropdown: Chapter that resonated most (16 options)
2. Long text: How has this book changed your approach?
3. Short text: One action you've taken?
4. Scale 1-10: Would you recommend?
5. Short text: Favorite quote or takeaway?
6. Long text (optional): Suggestions for improvement?
7. Radio: May we share your feedback? (Yes with name / Yes anonymously / No)
8. Radio: Leave Amazon/Goodreads review? (Already did / Yes I will / Maybe later / No)
   If "Already did": Text field for review link
```

**Thank You Message:**
- "Thank you! Check your email for a special gift"
- CTA: "Leave a Review on Amazon"

---

## WIREFRAME 9: BLOG HUB

### Layout:
```
Hero (Featured Post - large card)
→ Post Grid (3-column, 9 posts)
→ Sidebar (Author bio, newsletter signup, categories, popular posts, lead magnet)
→ Pagination
```

**Featured Post:**
- Full-width image, category tag, title, excerpt, "Read Post" CTA

**Post Cards:**
- Thumbnail image, category tag, title, excerpt, read time
- "Members Only" badge on gated posts

**Sidebar:**
- Author bio card (photo, mini bio, social links)
- Newsletter signup (email capture, "Subscribe" CTA)
- Categories list (Business, Technical, Inspiration, Self-Care, Industry Trends)
- Popular posts (5 links with thumbnails)
- Lead magnet promo ("Download Free Pricing Calculator" image + CTA)

---

## WIREFRAME 10: INDIVIDUAL BLOG POST

### Article Layout:
```
Article Header (category, title, author, date, read time)
→ Article Content (H2/H3 subheadings, images, blockquotes)
→ Mid-Article CTA (lead magnet email capture)
→ End-of-Article CTA (Join community or Pre-Order book)
→ Related Posts (3 cards)
→ Sidebar (same as blog hub)
```

**Gating for Members-Only Posts:**
- Show first 200 words
- Blur/fade remaining content
- Overlay: "This is Premium Content for Members"
- Benefits: "Join free to access 20+ exclusive articles, downloads, newsletters"
- CTA: "Join Free to Continue Reading"

---

## RESPONSIVE BEHAVIOR NOTES

### Mobile Optimizations (All Pages):

**Navigation:**
- Hamburger menu (☰) replaces full nav
- Logo centered or left-aligned
- Login/account icon top-right

**Hero Sections:**
- Background images: Portrait orientation, mobile-optimized
- Headlines: Reduced font size (36px max)
- CTAs: Full-width or stacked vertically

**Grids:**
- 3-column → 1-column stacked
- Cards: Full-width, margin-bottom 16px

**Forms:**
- Inputs: Full-width, 48px height minimum
- Labels: Above inputs (not floating)
- Buttons: Full-width, 56px height

**Images:**
- Responsive sizing (100% width, auto height)
- Lazy loading below fold

**Sticky Elements:**
- CTA bars: Fixed bottom (not top)
- Headers: Sticky with reduced height

---

## ACCESSIBILITY ANNOTATIONS

**All Wireframes Include:**

✓ Semantic HTML5 structure (`<header>`, `<nav>`, `<main>`, `<article>`, `<aside>`, `<footer>`)
✓ ARIA landmarks (`role="navigation"`, `role="main"`, `role="complementary"`)
✓ Alt text for all images (decorative images: empty alt="")
✓ Form labels associated with inputs (`<label for="email">`)
✓ Keyboard navigation support (Tab order matches visual order)
✓ Focus indicators (2px teal outline on focused elements)
✓ Color contrast ≥ 4.5:1 (text), ≥ 3:1 (UI)
✓ Skip to main content link (hidden until focused)
✓ Descriptive link text (not "click here")
✓ Heading hierarchy (H1 → H2 → H3, no skipping)

---

## DESIGN HANDOFF NOTES FOR DEVELOPERS

**Assets Needed:**

1. **Images:**
   - Hero backgrounds (2000px width, WebP format)
   - Book cover (3D mockup, multiple angles)
   - Author photo (800px width)
   - Testimonial photos (300px width, circular crop)
   - Icon set (SVG format, 64px)
   - Social media icons (SVG, 32px)

2. **Fonts:**
   - Playfair Display (700 weight) - Google Fonts
   - Inter (400, 600 weights) - Google Fonts
   - Libre Baskerville (400 italic) - Google Fonts (testimonials)

3. **Color Palette:**
   - Teal: #008B8B
   - Gold: #DAA520
   - Gray Light: #F5F5F5
   - Gray Dark: #333333
   - White: #FAFAFA
   - Purple: #4B0082

4. **Animations:**
   - Fade-in on scroll (testimonials, benefit cards)
   - Hover effects (buttons: background darken 10%, subtle box-shadow)
   - Accordion expand/collapse (chevron rotation 180°, content slide down)
   - Carousel auto-rotate (5 seconds per slide, pause on hover)

5. **Plugins Required:**
   - MemberPress (free membership, content gating)
   - WooCommerce (e-commerce)
   - CartBouncy (cart abandonment)
   - ConvertKit (email integration)
   - WP Rocket (caching)
   - Wordfence (security)

---

**END OF WIREFRAMES_DETAILED_V2.md**

**Document Status:** ✅ Production-Ready for Development
**Total Pages:** 10 Complete Wireframes
**Last Updated:** November 3, 2025
**Next Steps:** Developer implementation, asset creation, QA testing
