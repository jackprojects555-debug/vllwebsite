# VLL Website SPEC

## Project
A bilingual CMS website for Vardi, Lavie-Loboda & Co.  
Domain: vll.co.il

## Goal
Create a clean, luxurious, minimalist website for a boutique law firm, with structured CMS control over pages, attorneys, practice areas, and future articles.

## Firm Name
English: Vardi, Lavie-Loboda & Co.  
Hebrew: ורדי, לביא-לובודה ושות׳

## Stack
- Python 3.14.4
- Django 6.0.4
- Wagtail 7.3.1 CMS
- SQLite for local development
- PostgreSQL for production
- HTML / CSS
- Render deployment

## Languages
- Hebrew, primary, RTL
- English, secondary

## Design Direction
Luxury boutique law firm.

The design should be:
- minimalist
- clean
- elegant
- quiet
- serious
- spacious
- professional
- refined

Avoid:
- generic law firm look
- stock legal imagery
- noisy animations
- aggressive marketing
- visual clutter

Preferred visual direction:
- white or warm off-white background
- dark gray / black text
- subtle navy or muted gold accents
- generous whitespace
- simple top navigation
- elegant typography
- mobile responsive

## CMS Principle
The CMS must be structured, not a free page builder.

The goal is to preserve a consistent luxury design.  
Editors should change content, not redesign pages.

## Main Pages

### 1. Home Page
Purpose:
Present the firm clearly and elegantly.

Fields:
- hero_title
- hero_subtitle
- intro_text
- selected_practice_areas
- selected_attorneys
- contact_cta_text

### 2. About Page
Purpose:
Present the firm, its approach, and professional character.

Fields:
- title
- intro
- body
- values_section

### 3. Practice Areas Index
Purpose:
List the firm’s main legal practice areas.

Initial practice areas:
- Tax
- International Tax
- Trusts
- Commercial Law
- Commercial Litigation
- Real Estate

### 4. Practice Area Page
Purpose:
Dedicated page for each practice area.

Fields:
- title
- short_description
- full_description
- key_services

### 5. Attorneys Index
Purpose:
List the firm’s attorneys.

Initial attorneys:
- Sagi Vardi
- Sagi Loboda

### 6. Attorney Page
Purpose:
Dedicated profile page for each attorney.

Fields:
- name
- title
- image
- bio
- expertise
- languages
- email

### 7. Contact Page
Purpose:
Allow users to contact the firm.

Fields:
- address
- email
- phone
- contact_form_enabled

Primary email:
vll@vll.co.il

### 8. Articles / Insights
Purpose:
Infrastructure only in first version.

Fields:
- title
- date
- author
- body
- seo_title
- meta_description

Do not emphasize articles in the first launch.

### 9. Legal Information
Purpose:
Basic legal disclaimer page.

### 10. Privacy Policy
Purpose:
Basic privacy policy page.

## First Version Scope
The first version should include:
- working Wagtail CMS
- structured Home Page
- About Page
- Practice Areas structure
- Attorney profiles structure
- Contact Page
- Hebrew and English structure
- clean responsive templates
- basic SEO fields
- simple navigation
- footer with contact details

## Out of Scope for First Version
Do not include yet:
- full article publishing UI
- complex blog design
- advanced search
- advanced permissions
- animations
- newsletter
- CRM integration
- complex menu builder
- payment features
- client portal

## Development Principle
Cursor is used only for execution.

All planning is done manually.

Tasks must be:
- small
- isolated
- testable
- committed after completion

Do not ask Cursor to build the whole website at once.