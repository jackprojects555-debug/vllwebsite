## Task 1: HomePage Model

Modify only home/models.py.

Do not inspect other files.

Task:
Update HomePage.

Add:
hero_title = models.CharField(max_length=255, blank=True)
hero_subtitle = models.CharField(max_length=255, blank=True)
intro_text = RichTextField(blank=True)
contact_cta_text = models.CharField(max_length=255, blank=True)

Add content_panels with FieldPanel for each new field.

Constraints:
Add only required imports:
- FieldPanel
- RichTextField

Do not change anything else.

Output:
Return full updated file.

## Task 2: AboutPage Model

Modify only home/models.py.

Do not inspect other files.

Task:
Add a new AboutPage model.

Fields:
title = models.CharField(max_length=255)
intro = models.TextField(blank=True)
body = RichTextField(blank=True)
values_section = RichTextField(blank=True)

Add content_panels for all fields.

Constraints:
Add only required imports if missing.
Do not modify HomePage.
Do not refactor.
Do not change anything else.

Output:
Return only diff.