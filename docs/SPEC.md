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
- PostgreSQL
- HTML / CSS
- Render deployment

## Languages
- Hebrew (primary, RTL)
- English (secondary)

## Main Pages
1. Home
2. About
3. Practice Areas
4. Individual Practice Area Page
5. Attorneys
6. Individual Attorney Page
7. Articles / Insights (infrastructure only)
8. Contact
9. Legal Information
10. Privacy Policy

## Design Direction
Luxury boutique law firm.  
Minimalist, clean, quiet, serious, elegant.  

No clutter  
No aggressive marketing  
No generic templates  

## CMS Structure (Strict)

The CMS must be structured, not flexible.

### Home Page
- hero_title
- hero_subtitle
- intro_text
- selected_practice_areas
- selected_attorneys
- contact_cta_text

### About Page
- title
- intro
- body
- values_section

### Practice Area Page
- title
- short_description
- full_description
- key_services

### Attorneys Page
- listing only

### Attorney Page
- name
- title
- image
- bio
- expertise
- languages
- email

### Contact Page
- address
- email
- phone
- contact_form_enabled

### Articles (Infrastructure)
- title
- date
- author
- body
- seo fields

## CMS Capabilities
- Edit all content (HE + EN)
- Add/edit attorneys
- Add/edit practice areas
- Upload images
- SEO per page
- Manage menus

## First Version Scope
- Full bilingual structure
- Homepage
- About
- Practice Areas
- Attorneys
- Contact
- CMS admin
- Basic SEO

No need to launch articles yet.

## Team
- Sagi Vardi
- Sagi Loboda

## Contact
vll@vll.co.il

## Development Principle
Cursor is used only for execution.  
All planning is done manually.  
Tasks must be small, isolated, and controlled.