# TECHNICAL SPECIFICATIONS
## Curls & Contemplation Author Launch Website

**Document Version:** 1.0
**Date:** October 14, 2025
**Status:** Complete - Ready for Implementation

---

## TABLE OF CONTENTS

1. [Technical Stack Recommendation](#technical-stack-recommendation)
2. [Platform & Hosting](#platform--hosting)
3. [Plugin & Extension Matrix](#plugin--extension-matrix)
4. [E-Commerce Configuration](#e-commerce-configuration)
5. [Payment Gateway Setup](#payment-gateway-setup)
6. [Email & Automation Integration](#email--automation-integration)
7. [Community Platform Integration](#community-platform-integration)
8. [Analytics & Tracking](#analytics--tracking)
9. [SEO Technical Implementation](#seo-technical-implementation)
10. [Security & Performance](#security--performance)
11. [Accessibility Compliance](#accessibility-compliance)
12. [Third-Party Integrations](#third-party-integrations)
13. [Development Environment Setup](#development-environment-setup)

---

## TECHNICAL STACK RECOMMENDATION

### Recommended Primary Stack: **WordPress + WooCommerce**

**Rationale:**
- **Ease of Use:** Non-technical client can manage content updates independently
- **E-Commerce Maturity:** WooCommerce is battle-tested for digital + physical product sales
- **Plugin Ecosystem:** Extensive marketplace for membership, email, SEO, analytics
- **Community Support:** Massive developer community, abundant documentation
- **Cost-Effective:** Open-source core, affordable hosting, lower development costs vs. custom builds
- **Scalability:** Can handle traffic spikes during book launch and ongoing growth

**Alternative Stack: Custom Build (Next.js + Shopify + Headless CMS)**

**Use This If:**
- Client has ongoing developer support / technical team
- Budget allows for higher upfront investment ($15K-$25K vs. $5K-$10K for WordPress)
- Performance and customization are absolute priorities
- Client wants cutting-edge tech stack

**For this project, WordPress + WooCommerce is recommended** given the balance of functionality, cost, and maintainability.

---

## PLATFORM & HOSTING

### Hosting Provider Recommendation

**Tier 1 (Recommended): Kinsta or WP Engine**

| Feature | Kinsta | WP Engine |
|---------|--------|-----------|
| **Managed WordPress** | Yes | Yes |
| **Performance** | Google Cloud infrastructure, CDN included | AWS infrastructure, CDN included |
| **Security** | Daily backups, malware scanning, free SSL | Daily backups, malware scanning, free SSL |
| **Support** | 24/7 expert support | 24/7 expert support |
| **Staging Environment** | 1-click staging | 1-click staging |
| **Pricing** | Starts ~$35/month | Starts ~$30/month |
| **Best For** | Performance-focused, fast support | Enterprise features, developer tools |

**Tier 2 (Budget Option): Siteground or Cloudways**

- More affordable ($10-$25/month)
- Adequate performance for most use cases
- Less hand-holding, more self-service

**Recommendation for This Project:** **Kinsta Starter Plan** ($35/month)

**Hosting Specs:**
- **Storage:** 10GB SSD (sufficient for website + digital assets)
- **Bandwidth:** 50GB/month (supports ~25,000 visitors/month)
- **CDN:** Cloudflare integration (free, automatic)
- **PHP Version:** 8.2+
- **MySQL Version:** 8.0+
- **SSL Certificate:** Free Let's Encrypt (auto-renew)

---

### Domain & DNS Configuration

**Domain Registrar:** Namecheap, Google Domains, or Cloudflare Registrar

**DNS Records to Configure:**

```
A Record:
  @ (root) → Kinsta server IP

CNAME Records:
  www → root domain
  email → ESP sending domain (e.g., email.curlsandcontemplation.com)

MX Records:
  (if using custom email) → Email provider (Google Workspace / Microsoft 365)

TXT Records:
  SPF: v=spf1 include:_spf.google.com ~all (or ESP's SPF)
  DKIM: [provided by ESP]
  DMARC: v=DMARC1; p=quarantine; rua=mailto:[email]
```

---

## PLUGIN & EXTENSION MATRIX

### Core Plugins (Required)

| Plugin Name | Purpose | License | Cost |
|-------------|---------|---------|------|
| **WooCommerce** | E-commerce platform | Free (GPL) | Free |
| **WooCommerce Pre-Orders** | Pre-order functionality | Premium | $249/year |
| **Paid Memberships Pro** or **MemberPress** | Curl Collective membership | Premium | $297/year |
| **ConvertKit for WP** or **ActiveCampaign** | Email marketing integration | Free (requires ESP account) | ESP cost separate |
| **Yoast SEO Premium** or **Rank Math Pro** | SEO optimization | Premium | $99/year |
| **WP Rocket** | Caching & performance | Premium | $59/year |
| **UpdraftPlus Premium** | Automated backups | Premium | $70/year |
| **Wordfence Security** or **Sucuri** | Security & firewall | Premium | $119/year |
| **WPForms Pro** | Advanced forms (lead capture, surveys) | Premium | $199/year |

**Total Est. Annual Plugin Cost:** ~$1,200-$1,500/year

---

### Recommended Optional Plugins

| Plugin Name | Purpose | Cost |
|-------------|---------|------|
| **OptinMonster** | Exit-intent popups, A/B testing | $108/year |
| **Pretty Links** | Link cloaking & tracking (affiliate/referral) | $99/year |
| **AffiliateWP** | If building affiliate program in-house | $199/year |
| **Advanced Custom Fields (ACF Pro)** | Custom content types, flexible layouts | $49/year |
| **Gravity Forms** | Alternative to WPForms (more powerful) | $59/year |
| **MonsterInsights Pro** | Google Analytics dashboard integration | $199/year |

---

### Community Platform Integration Options

**Option 1: Discord (Recommended for This Project)**

**Pros:**
- Free to use
- Familiar to most users
- Voice channels, events, robust moderation
- Easy onboarding (most people already have accounts)

**Cons:**
- Less "branded" experience
- Limited customization
- Less control over data

**Integration Method:** Use Zapier or Integromat to auto-invite members when they purchase Curl Collective membership

**Cost:** Free (Discord) + $20/month (Zapier automation)

---

**Option 2: Circle.so**

**Pros:**
- Beautiful, branded community platform
- Built-in courses, events, member directories
- More professional appearance
- Full data control

**Cons:**
- Costs $89-$219/month
- Another platform for members to learn
- Requires manual onboarding or API integration

**Cost:** $89/month (Basic) to $219/month (Professional)

---

**Option 3: BuddyPress (WordPress Plugin)**

**Pros:**
- Fully integrated with WordPress
- Complete control and customization
- No recurring platform fees

**Cons:**
- Requires significant development work
- Less modern UX out-of-the-box
- More maintenance overhead

**Cost:** Free (plugin) + development time (~$2,000-$5,000)

---

**Recommendation:** **Discord** for launch (free, easy onboarding), with potential migration to Circle.so if community grows beyond 1,000 members and budget allows.

---

## E-COMMERCE CONFIGURATION

### WooCommerce Settings

**General Settings:**
- **Base Location:** United States (or primary business location)
- **Currency:** USD ($)
- **Tax:** Enable tax calculation (configure based on nexus states)

**Product Settings:**
- **Shop Page:** /shop or /book (redirect to main book page)
- **Add to Cart Behavior:** Redirect to checkout (reduce friction)
- **Enable Reviews:** Yes (for book testimonials)

**Shipping Settings:**
- **Shipping Zones:** Domestic (US), International (rest of world)
- **Shipping Methods:**
  - Domestic: Free shipping (pre-order promotion)
  - International: Flat rate ($9.99) or calculated (if using ShipStation integration)
- **Shipping Classes:** Standard (book), Digital (bonuses - no shipping)

**Payment Settings:**
- **Accepted Gateways:** Stripe, PayPal, Apple Pay, Google Pay
- **Checkout Fields:** Minimize friction (email, name, address only)

**Tax Settings:**
- **Enable Tax:** Yes
- **Prices Entered With Tax:** No (tax added at checkout)
- **Calculate Tax Based On:** Customer shipping address
- **Tax Rates:** Configure for nexus states (use TaxJar plugin for automation if selling in multiple states)

---

### Pre-Order Product Configuration

**Product Type:** Pre-order (using WooCommerce Pre-Orders plugin)

**Product Settings:**
- **Product Name:** Curls & Contemplation: A Stylist's Interactive Journey Journal
- **Pre-Order Price:** $19.99
- **Regular Price (After Launch):** $29.99
- **Availability Date:** May 27, 2025
- **SKU:** CURLS-CONTEMP-001
- **Stock Status:** Pre-order available
- **Manage Stock:** Yes (track against 500 bonus limit)

**Virtual Products (Bonuses):**
Each bonus should be a separate downloadable product automatically added to cart when pre-order is purchased, or bundled into one "Bonus Stack" download.

---

### Cart Abandonment Setup

**Plugin:** Cartflows or CartBounty

**Features:**
- Track when users add to cart but don't complete checkout
- Trigger email sequence (see FunnelAutomation.md) at 1 hour, 24 hours, 72 hours
- Include "Complete Your Order" link with cart pre-populated

**Integration:** Connect to ConvertKit/ActiveCampaign to send recovery emails

---

## PAYMENT GATEWAY SETUP

### Stripe Configuration (Primary Gateway)

**Account Setup:**
1. Create Stripe account at stripe.com
2. Complete business verification (required for payouts)
3. Connect bank account for deposits

**WordPress Integration:**
- Install **WooCommerce Stripe Payment Gateway** (official plugin)
- Enter API keys (test mode for dev, live mode for production)
- Enable payment methods:
  - ✅ Credit/Debit Cards
  - ✅ Apple Pay
  - ✅ Google Pay
  - ✅ Link (Stripe's 1-click checkout)

**Stripe Settings:**
- **Statement Descriptor:** "CURLSBOOK" (shows on customer's credit card statement)
- **Capture Charges:** Immediately (charge at time of purchase, not pre-auth)
- **3D Secure:** Enable (required for Strong Customer Authentication in EU)
- **Saved Payment Methods:** Enable (for subscriptions and repeat customers)

**Stripe Dashboard Settings:**
- Enable **Customer Portal** (allows customers to manage subscriptions)
- Set up **Webhook Endpoints** (for order status updates):
  - `https://yourdomain.com/wc-api/stripe/`
- Configure **Email Receipts:** Disable (WooCommerce handles this)

**Fees:**
- 2.9% + $0.30 per successful card charge
- No monthly fees
- Payouts: 2-day rolling (funds available in 2 business days)

---

### PayPal Configuration (Secondary Gateway)

**Account Setup:**
1. Create PayPal Business account
2. Verify email and bank account

**WordPress Integration:**
- Use **WooCommerce PayPal Checkout Payment Gateway**
- Enter PayPal Client ID and Secret Key
- Enable **PayPal Smart Payment Buttons** (modern checkout experience)

**PayPal Settings:**
- **Payment Action:** Capture immediately
- **Enable Express Checkout:** Yes (1-click for PayPal users)
- **Brand Name:** "Curls & Contemplation"

**Fees:**
- 2.99% + $0.49 per transaction (slightly higher than Stripe)
- No monthly fees

---

### Tax Automation (Optional but Recommended)

**Plugin:** TaxJar for WooCommerce

**Purpose:** Automatically calculate sales tax for all US states (required if you have nexus in multiple states)

**Setup:**
1. Create TaxJar account (free for <200 transactions/month)
2. Install TaxJar plugin
3. Enter API token
4. Enable auto-filing (TaxJar files sales tax returns for you)

**Cost:**
- Free tier: 0-200 transactions/month
- Basic: $19/month for 201-500 transactions
- Plus: Auto-filing starts at $29/month

**Recommendation:** Start with free tier, upgrade if volume increases

---

## EMAIL & AUTOMATION INTEGRATION

### Email Service Provider Setup

**Recommended ESP: ConvertKit**

**Pricing:**
- 0-1,000 subscribers: $29/month
- 1,001-3,000 subscribers: $49/month
- 3,001-5,000 subscribers: $79/month

**Features Needed:**
- Email automation (sequences, triggers)
- Tagging and segmentation
- Landing page builder
- Forms and popups
- Integrations (WooCommerce, Zapier)

**Setup Steps:**
1. Create ConvertKit account
2. Verify sending domain (email.curlsandcontemplation.com)
3. Configure DNS records (SPF, DKIM, DMARC)
4. Warm up domain (gradual sending volume increase over 2 weeks)

**WordPress Integration:**
- Install **ConvertKit for WordPress** plugin
- Enter API key and secret
- Map WooCommerce events to ConvertKit tags:
  - Purchase → Tag: `customer_preorder`
  - Membership signup → Tag: `member_active`
  - Subscription canceled → Tag: `member_inactive`

---

### Automation Workflow Setup

**Reference:** See `FunnelAutomation.md` for all email sequences

**ConvertKit Automations to Build:**
1. **Welcome Sequence** (5 emails)
2. **Post-Purchase Sequence** (7 emails)
3. **Cart Abandonment** (3 emails)
4. **Membership Onboarding** (2 emails)
5. **Win-Back Campaign** (1 email, triggered 60 days post-cancel)

**Integration with WooCommerce:**
Use **Zapier** or **ConvertKit native WooCommerce integration** to:
- Add customer to email list on purchase
- Tag customers based on product purchased
- Remove from nurture sequence when they become customers
- Trigger abandoned cart emails

---

### Transactional Email Configuration

**WooCommerce Emails (Order Confirmations, Shipping Notifications):**

**Plugin:** WooCommerce Email Customizer (or native WooCommerce templates)

**Customize These Emails:**
- ✅ Order Received (confirmation)
- ✅ Order Shipped (with tracking)
- ✅ Order Completed (post-delivery)
- ✅ Failed Payment (payment issue alert)
- ✅ Subscription Renewal Reminder (for Curl Collective)

**Design:**
- Match website branding (colors, fonts, logo)
- Mobile-responsive templates
- Clear CTAs ("Track Your Order," "Access Your Bonuses")

**Delivery:**
Use **SendGrid** or **Amazon SES** for reliable transactional email delivery (better than default WordPress mail)

**Plugin:** WP Mail SMTP (configure with SendGrid or SES)

**SendGrid Setup:**
1. Create free SendGrid account (100 emails/day free, then $15/month for 40K emails)
2. Create API key
3. Install WP Mail SMTP plugin
4. Enter SendGrid API key
5. Test email delivery

---

## COMMUNITY PLATFORM INTEGRATION

### Discord Integration (Recommended)

**Setup:**
1. Create Discord server for "Curl Collective"
2. Set up channels:
   - #welcome
   - #introductions
   - #wins
   - #help
   - #business-strategy
   - #technical-skills
   - #wellness-and-balance
   - #faith-and-craft
   - #accountability-partners
   - #resources
   - #events
   - #announcements (read-only)

**Roles:**
- **Admin** (Michael + moderators)
- **Active Member** (paid members)
- **Pre-Order Customer** (free month access)
- **VIP** (annual members, top referrers)

**Automation:**
Use **Zapier** to auto-invite new members:

**Zap Flow:**
1. Trigger: New WooCommerce subscription for "Curl Collective Membership"
2. Action: Send Discord invite link via email
3. Action: Add customer to ConvertKit "member_active" tag

**Cost:** $20/month (Zapier Starter plan)

**Alternative:** Use **MemberPress Discord Add-On** (if using MemberPress plugin) - $0 extra cost

---

### Circle.so Integration (If Chosen)

**Setup:**
1. Create Circle community
2. Set up Spaces (equivalent to Discord channels)
3. Configure membership tiers (match WooCommerce products)

**Integration:**
Use Circle's **Zapier integration** or **native WooCommerce integration** (if available):

**Workflow:**
1. Customer purchases Curl Collective membership on WordPress
2. Zapier creates Circle account and sends invite
3. Customer completes profile on Circle

**Cost:** $89/month (Circle) + $20/month (Zapier if needed)

---

## ANALYTICS & TRACKING

### Google Analytics 4 (GA4) Setup

**Setup Steps:**
1. Create Google Analytics 4 property
2. Install tracking code via plugin: **MonsterInsights Pro** or **Site Kit by Google**
3. Enable Enhanced E-Commerce tracking
4. Set up conversion events

**Key Events to Track:**
- `page_view` (automatic)
- `add_to_cart` (WooCommerce auto-tracks if configured)
- `begin_checkout`
- `purchase` (e-commerce transaction)
- `email_signup` (form submission)
- `link_click` (outbound links, downloads)
- `scroll` (user engagement)

**Goals & Conversions:**
- Pre-order purchases
- Email signups
- Membership purchases
- Referral link clicks
- Bonus downloads

**Custom Dimensions:**
- User Type (subscriber, customer, member)
- Traffic Source (organic, social, email, referral)
- Customer Lifetime Value (CLV)

---

### Facebook Pixel & Meta Conversions API

**Purpose:** Track website visitors for retargeting ads and measuring ad performance

**Setup:**
1. Create Facebook Business Manager account
2. Generate Pixel ID
3. Install via **PixelYourSite Pro** plugin (supports both Pixel and Conversions API)
4. Configure standard events:
   - `PageView`
   - `ViewContent` (book page)
   - `AddToCart`
   - `InitiateCheckout`
   - `Purchase`
   - `Lead` (email signup)

**Conversions API:**
- More reliable than pixel alone (not blocked by ad blockers or iOS privacy features)
- PixelYourSite Pro handles server-side event tracking automatically

**Cost:** PixelYourSite Pro plugin - $99/year

---

### Hotjar (Heatmaps & Session Recordings)

**Purpose:** Understand user behavior (where they click, scroll, drop off)

**Setup:**
1. Create Hotjar account (free for <35 daily sessions)
2. Install tracking code via plugin or Google Tag Manager
3. Set up heatmaps for:
   - Homepage
   - Book Page
   - Pre-Order Checkout
4. Enable session recordings (watch user interactions)
5. Set up feedback polls ("Why didn't you purchase today?")

**Cost:**
- Free: 35 daily sessions
- Plus: $39/month for 100 daily sessions

**Recommendation:** Start with free tier, upgrade if needed

---

### Google Tag Manager (GTM)

**Purpose:** Centralized tag management (easier to add/remove tracking codes without editing site)

**Setup:**
1. Create GTM account and container
2. Install via **GTM4WP** plugin
3. Add tags through GTM dashboard:
   - GA4
   - Facebook Pixel
   - Hotjar
   - LinkedIn Insight
   - Pinterest Tag
4. Configure triggers (page views, clicks, form submissions)

**Benefits:**
- No code changes needed to add new tracking
- A/B test different tracking configurations
- Faster page load (async tag loading)

---

## SEO TECHNICAL IMPLEMENTATION

### On-Page SEO Configuration

**Plugin:** Yoast SEO Premium or Rank Math Pro

**Site-Wide Settings:**
- **Site Title:** Curls & Contemplation | Transform Your Hairstyling Career
- **Meta Description:** (155 chars max) "Design a hairstyling career on your own terms. Learn pricing, freelancing, conscious beauty, and business strategies for sustainable success."
- **Canonical URLs:** Enabled (prevent duplicate content)
- **XML Sitemap:** Auto-generated and submitted to Google Search Console
- **Robots.txt:** Configured to allow search engines

**Per-Page SEO:**
Each page has custom:
- Title tag (optimized for target keyword)
- Meta description
- Focus keyword
- Internal links (see ContentMatrix.csv for linking structure)

---

### Schema Markup (Structured Data)

**Implement Schema for:**

1. **Book (Product Schema)**
```json
{
  "@context": "https://schema.org/",
  "@type": "Book",
  "name": "Curls & Contemplation: A Stylist's Interactive Journey Journal",
  "author": {
    "@type": "Person",
    "name": "Michael David Warren Jr."
  },
  "isbn": "[ISBN when available]",
  "bookFormat": "Paperback",
  "datePublished": "2025-05-27",
  "offers": {
    "@type": "Offer",
    "price": "19.99",
    "priceCurrency": "USD",
    "availability": "https://schema.org/PreOrder"
  }
}
```

2. **Author (Person Schema)**
```json
{
  "@context": "https://schema.org/",
  "@type": "Person",
  "name": "Michael David Warren Jr.",
  "jobTitle": "Hairstylist, Author, Educator",
  "url": "https://curlsandcontemplation.com/author",
  "sameAs": [
    "https://instagram.com/michaeldavidwarrenjr",
    "https://linkedin.com/in/michaeldavidwarrenjr"
  ]
}
```

3. **Organization Schema**
```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "Curls & Contemplation",
  "url": "https://curlsandcontemplation.com",
  "logo": "https://curlsandcontemplation.com/logo.png",
  "sameAs": [
    "https://instagram.com/michaeldavidwarrenjr",
    "https://linkedin.com/in/michaeldavidwarrenjr",
    "https://youtube.com/@michaeldavidwarrenjr"
  ]
}
```

4. **FAQ Schema (for Book Page FAQ Section)**
```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "When does the book ship?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Curls & Contemplation ships on May 27, 2025."
      }
    }
    // ... more FAQs
  ]
}
```

**Implementation Method:**
Use **Yoast SEO Premium Schema Blocks** or **Rank Math Pro Schema Generator** to automatically generate and inject schema markup.

---

### XML Sitemap

**Auto-generated by Yoast/Rank Math**

**Included in Sitemap:**
- ✅ All public pages
- ✅ Blog posts
- ✅ Product pages
- ❌ Excluded: Admin pages, login, checkout, thank you pages

**Submit to:**
- Google Search Console
- Bing Webmaster Tools

---

### Robots.txt Configuration

**File Location:** `https://curlsandcontemplation.com/robots.txt`

**Contents:**
```
User-agent: *
Disallow: /cart/
Disallow: /checkout/
Disallow: /my-account/
Disallow: /wp-admin/
Disallow: /wp-includes/
Allow: /wp-content/uploads/

Sitemap: https://curlsandcontemplation.com/sitemap.xml
```

---

### Google Search Console Setup

1. Verify site ownership (via DNS, HTML file, or Google Tag Manager)
2. Submit XML sitemap
3. Monitor:
   - Indexing status
   - Search performance (impressions, clicks, CTR)
   - Core Web Vitals
   - Mobile usability
   - Manual actions / penalties

---

### Page Speed Optimization

**Target Metrics (Core Web Vitals):**
- **LCP (Largest Contentful Paint):** < 2.5 seconds
- **FID (First Input Delay):** < 100ms
- **CLS (Cumulative Layout Shift):** < 0.1

**Optimization Tactics:**

**1. Caching**
- Plugin: **WP Rocket** (premium) or **LiteSpeed Cache** (free)
- Enable page caching, browser caching, object caching

**2. Image Optimization**
- Plugin: **ShortPixel** or **Imagify**
- Compress all images (lossy compression)
- Convert to WebP format
- Lazy load images (below the fold)

**3. Minification**
- Minify HTML, CSS, JavaScript (WP Rocket handles this)
- Combine CSS/JS files (reduce HTTP requests)

**4. CDN (Content Delivery Network)**
- Use **Cloudflare** (free tier)
- Caches static assets globally (faster load times worldwide)

**5. Database Optimization**
- Plugin: **WP-Optimize**
- Clean up post revisions, spam comments, transients
- Optimize database tables weekly

**6. Hosting**
- Kinsta includes server-level caching (Redis/Memcached)
- HTTP/2 and HTTP/3 enabled by default

**Target Result:** 90+ on Google PageSpeed Insights (mobile and desktop)

---

## SECURITY & PERFORMANCE

### Security Best Practices

**1. Firewall & Malware Scanning**
- Plugin: **Wordfence Security Premium** ($119/year)
- Features:
  - Web Application Firewall (WAF)
  - Real-time malware scanning
  - Login attempt limiting (brute force protection)
  - Two-factor authentication (2FA)
  - Country blocking (block traffic from high-risk countries)

**2. SSL Certificate**
- Included free with Kinsta (Let's Encrypt auto-renewal)
- Force HTTPS site-wide (redirect HTTP → HTTPS)
- HSTS header enabled

**3. Regular Backups**
- Plugin: **UpdraftPlus Premium**
- Schedule:
  - **Daily:** Database backups (lightweight)
  - **Weekly:** Full site backups (files + database)
- Storage: Google Drive, Dropbox, or Amazon S3 (offsite)
- Retention: Keep last 30 days of backups

**4. Security Headers**
Use **Really Simple SSL Pro** plugin to add:
- `X-Frame-Options: SAMEORIGIN` (prevent clickjacking)
- `X-Content-Type-Options: nosniff`
- `Referrer-Policy: strict-origin-when-cross-origin`
- `Content-Security-Policy` (prevent XSS attacks)

**5. Login Security**
- Change default WordPress login URL (from `/wp-admin` to custom URL)
- Enable 2FA for admin accounts
- Limit login attempts (block after 5 failed attempts)
- Use strong passwords (20+ characters, alphanumeric + symbols)

**6. User Permissions**
- Admin role: Only for Michael + lead developer
- Editor role: For content managers (if applicable)
- Customer role: Automated for purchasers (no backend access)

---

### Performance Monitoring

**Tools:**
1. **Google PageSpeed Insights** (free)
2. **GTmetrix** (free, detailed waterfall reports)
3. **Pingdom** (uptime monitoring - $10/month)
4. **New Relic** (APM - free tier available)

**Set Alerts:**
- Downtime alert (site goes offline)
- Slow page load (>3 seconds)
- High server CPU usage

---

## ACCESSIBILITY COMPLIANCE

### WCAG 2.1 Level AA Standards

**Target:** Full compliance with Web Content Accessibility Guidelines 2.1 Level AA

**Key Requirements:**

**1. Perceivable**
- ✅ Alt text for all images
- ✅ Captions for videos
- ✅ Color contrast ratio ≥ 4.5:1 (text) and ≥ 3:1 (UI components)
- ✅ Text resizable up to 200% without loss of functionality

**2. Operable**
- ✅ Keyboard navigation (all interactive elements accessible via keyboard)
- ✅ No keyboard traps
- ✅ Skip to main content link
- ✅ Sufficient time to read and interact with content

**3. Understandable**
- ✅ Consistent navigation across pages
- ✅ Clear error messages on forms
- ✅ Labels for all form inputs
- ✅ Language declared in HTML (`lang="en"`)

**4. Robust**
- ✅ Valid HTML (passes W3C validator)
- ✅ ARIA landmarks (`role="main"`, `role="navigation"`, etc.)
- ✅ Semantic HTML5 (proper heading hierarchy, list elements, etc.)

---

### Accessibility Testing Tools

**Automated Testing:**
- **WAVE Browser Extension** (free)
- **axe DevTools** (free browser extension)
- **Lighthouse Accessibility Audit** (built into Chrome DevTools)

**Manual Testing:**
- Keyboard-only navigation test
- Screen reader test (NVDA on Windows, VoiceOver on Mac)
- Color contrast checker (WebAIM Contrast Checker)

**Plugin:** **WP Accessibility** (free) - Adds accessibility features automatically

---

### Accessibility Statement Page

**Location:** `/accessibility`

**Content:** See `SiteCopy_Full_NoTruncation.md` Page 7 - Legal Pages

**Include:**
- Commitment to accessibility
- Current compliance level (WCAG 2.1 AA)
- Known limitations
- Contact method for accessibility issues

---

## THIRD-PARTY INTEGRATIONS

### Integration Summary Table

| Service | Purpose | Integration Method | Cost |
|---------|---------|-------------------|------|
| **Stripe** | Payment processing | WooCommerce plugin | 2.9% + $0.30/transaction |
| **PayPal** | Payment processing | WooCommerce plugin | 2.99% + $0.49/transaction |
| **ConvertKit** | Email marketing | WordPress plugin + Zapier | $29-$79/month |
| **Discord** | Community platform | Zapier automation | Free |
| **Google Analytics 4** | Website analytics | MonsterInsights plugin | Free |
| **Facebook Pixel** | Ad tracking & retargeting | PixelYourSite plugin | Free (ad spend separate) |
| **Hotjar** | Heatmaps & session recordings | Script tag or GTM | Free - $39/month |
| **Zapier** | Automation workflows | API connections | $20/month |
| **TaxJar** | Sales tax automation | WordPress plugin | Free - $29/month |
| **Cloudflare** | CDN & DDoS protection | DNS configuration | Free |
| **Google Search Console** | SEO monitoring | Site verification | Free |
| **Amazon S3** | Offsite backup storage | UpdraftPlus integration | ~$1-$5/month |

---

### API Keys & Credentials Management

**Storage:** Use **environment variables** or WordPress `wp-config.php` (never hardcode in plugins)

**Required API Keys:**
- Stripe (Publishable Key, Secret Key)
- PayPal (Client ID, Secret)
- ConvertKit (API Key, API Secret)
- Google Analytics (Measurement ID)
- Facebook Pixel (Pixel ID)
- Hotjar (Site ID)
- Zapier (Webhook URLs)
- TaxJar (API Token)
- SendGrid/SES (API Key)

**Security:**
- Rotate keys every 90 days
- Use separate keys for dev/staging/production environments
- Store in password manager (1Password, LastPass, Bitwarden)

---

## DEVELOPMENT ENVIRONMENT SETUP

### Local Development Stack

**Recommended:** **Local by Flywheel** (free, easy WordPress local dev)

**Alternative:** **Docker + DDEV** (more advanced, fully customizable)

**Local Environment Specs:**
- PHP 8.2
- MySQL 8.0
- WordPress 6.4+
- Same plugins as production (or staging copies)

**Workflow:**
1. Develop locally on `localhost`
2. Push changes to **Staging** (Kinsta staging environment)
3. Test on staging (QA, client review)
4. Deploy to **Production** when approved

---

### Version Control (Git)

**Repository:** GitHub (private repo)

**.gitignore File:**
```
# WordPress core files
/wp-admin/
/wp-includes/
/wp-content/uploads/
wp-config.php

# Plugins (track only custom/premium plugins)
/wp-content/plugins/akismet/
/wp-content/plugins/hello.php

# Themes (track only active theme)
/wp-content/themes/twenty*/

# Environment files
.env
.htaccess

# Build artifacts
node_modules/
*.log
```

**Commit Strategy:**
- Feature branches for new work (`feature/email-automation`)
- Pull requests for code review
- Main branch always deployable

---

### Deployment Pipeline

**Option 1: Manual (Kinsta)**
- Export database from local
- Upload files via SFTP or Kinsta dashboard
- Import database on production
- Find/replace URLs (local → production)

**Option 2: Automated (GitHub Actions + Kinsta API)**
- Commit to `main` branch
- GitHub Actions runs tests
- Auto-deploys to Kinsta production environment

**Recommended for Launch:** Manual deployment with full QA checklist

**Recommended Post-Launch:** Automated deployment for content updates

---

### Staging Environment

**Kinsta Staging:**
- 1-click staging environment creation
- Identical to production (same plugins, theme, settings)
- Test all changes here before production push

**Staging URL:** `https://staging-curlsandcontemplation.kinsta.cloud`

**Access Control:**
- Password-protected (HTTP auth)
- Not indexed by search engines (`noindex` meta tag)

---

## DEVELOPMENT TIMELINE ESTIMATE

### Phase 1: Setup & Configuration (Week 1)
- [ ] Domain registration & DNS setup
- [ ] Hosting account setup (Kinsta)
- [ ] WordPress installation
- [ ] SSL certificate activation
- [ ] Email service provider setup (ConvertKit)
- [ ] Payment gateway accounts (Stripe, PayPal)

### Phase 2: Theme & Design (Weeks 2-3)
- [ ] Purchase/install WordPress theme (or custom build)
- [ ] Configure design system (colors, fonts, spacing)
- [ ] Build homepage
- [ ] Build book page
- [ ] Build author page
- [ ] Build community page
- [ ] Build blog layout

### Phase 3: E-Commerce Setup (Week 4)
- [ ] Install & configure WooCommerce
- [ ] Set up pre-order product
- [ ] Configure payment gateways
- [ ] Set up shipping rules
- [ ] Configure tax settings
- [ ] Test checkout flow end-to-end

### Phase 4: Membership & Community (Week 5)
- [ ] Install membership plugin
- [ ] Create membership tiers (monthly/annual)
- [ ] Set up Discord server
- [ ] Configure automation (purchase → community invite)
- [ ] Test membership signup flow

### Phase 5: Email Automation (Week 6)
- [ ] Build all email sequences in ConvertKit
- [ ] Set up automation triggers
- [ ] Design email templates
- [ ] Test all workflows end-to-end

### Phase 6: Content Population (Week 7)
- [ ] Import all website copy from SiteCopy document
- [ ] Upload images and visual assets
- [ ] Create blog post outlines (placeholder or published)
- [ ] Add legal pages (privacy, terms, refund, accessibility)

### Phase 7: SEO & Analytics (Week 8)
- [ ] Configure Yoast/Rank Math
- [ ] Add schema markup
- [ ] Submit sitemap to Search Console
- [ ] Set up Google Analytics 4
- [ ] Set up Facebook Pixel
- [ ] Set up Hotjar

### Phase 8: Testing & QA (Week 9)
- [ ] Cross-browser testing (Chrome, Firefox, Safari, Edge)
- [ ] Mobile responsiveness testing
- [ ] Accessibility audit (WAVE, axe, screen reader)
- [ ] Performance testing (PageSpeed, GTmetrix)
- [ ] Security audit (Wordfence scan)
- [ ] User flow testing (visitor → customer → member)
- [ ] Payment testing (test transactions)

### Phase 9: Pre-Launch (Week 10)
- [ ] Client training (how to manage site)
- [ ] Backup & disaster recovery test
- [ ] Final content review
- [ ] Final design review
- [ ] DNS cutover (if migrating from temp domain)
- [ ] Launch checklist completion

### Phase 10: Launch & Monitor (Week 11+)
- [ ] Go live!
- [ ] Monitor analytics, errors, performance
- [ ] Address any bugs or issues
- [ ] Begin ongoing optimization

**Total Timeline:** 10-11 weeks (2.5-3 months)

---

## ONGOING MAINTENANCE CHECKLIST

### Daily
- [ ] Monitor website uptime (Pingdom alerts)
- [ ] Check for critical errors (Wordfence security alerts)

### Weekly
- [ ] Review Google Analytics (traffic, conversions)
- [ ] Review email campaign performance (open rates, click rates)
- [ ] Check for WordPress/plugin updates (test on staging first)

### Monthly
- [ ] Full security scan (Wordfence)
- [ ] Database optimization (WP-Optimize)
- [ ] Backup verification (test restore)
- [ ] Performance audit (PageSpeed, GTmetrix)
- [ ] Review Core Web Vitals (Google Search Console)

### Quarterly
- [ ] Plugin audit (remove unused plugins)
- [ ] Content audit (update outdated content)
- [ ] SEO audit (keyword rankings, backlink profile)
- [ ] Accessibility audit (WAVE, manual testing)
- [ ] Competitor analysis

---

## COST SUMMARY

### One-Time Setup Costs

| Item | Cost |
|------|------|
| Domain registration (1 year) | $15 |
| WordPress theme (premium) | $59-$150 |
| Plugin licenses (annual, prorated) | $1,200-$1,500 |
| Development labor (10 weeks @ $50-$100/hr) | $5,000-$10,000 |
| **Total One-Time** | **$6,274-$11,665** |

### Recurring Monthly Costs

| Item | Monthly Cost | Annual Cost |
|------|--------------|-------------|
| Hosting (Kinsta) | $35 | $420 |
| Email marketing (ConvertKit) | $49 | $588 |
| Community platform (Discord + Zapier) | $20 | $240 |
| Plugin licenses (averaged) | $100 | $1,200 |
| Backup storage (S3) | $3 | $36 |
| Uptime monitoring (Pingdom) | $10 | $120 |
| Security (Wordfence Premium) | $10 | $120 |
| **Total Recurring** | **$227/month** | **$2,724/year** |

### Variable Costs

| Item | Cost Structure |
|------|----------------|
| Stripe transaction fees | 2.9% + $0.30 per transaction |
| PayPal transaction fees | 2.99% + $0.49 per transaction |
| Tax filing (TaxJar, if used) | $0-$29/month based on volume |
| Facebook Ads (if running) | Variable (budget-dependent) |

---

**This technical specifications document is complete and ready for developer implementation.**

---

**END OF TECHNICAL SPECIFICATIONS**
