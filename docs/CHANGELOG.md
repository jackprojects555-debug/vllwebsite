## 06.05.2026

- Added PracticeAreaPage model
- Fields: short_description, full_description
- Connected fields to Wagtail admin via content_panels
- Ran migrations and verified page type appears in admin
- Added AttorneysPage model
- Created basic page type for attorneys listing
- Ran migrations and verified page type appears in admin
- Added AttorneyPage model
- Fields: name, role, bio, email
- Connected fields to Wagtail admin via content_panels
- Ran migrations and verified page type appears in admin
- Added Wagtail page hierarchy rules
- HomePage can contain AboutPage, PracticeAreaPage, and AttorneysPage
- AttorneysPage can contain AttorneyPage
- AttorneyPage restricted to AttorneysPage parent
- PracticeAreaPage restricted to HomePage parent
- Verified hierarchy in Wagtail admin

## 05.05.2026

- Added structured HomePage model
- Fields: hero_title, hero_subtitle, intro_text, contact_cta_text
- Connected fields to Wagtail admin via content_panels
- Ran migrations and verified in admin
- Added AboutPage model
- Fields: intro, body, values_section
- Connected fields to Wagtail admin via content_panels
- Ran migrations and verified page type appears in admin