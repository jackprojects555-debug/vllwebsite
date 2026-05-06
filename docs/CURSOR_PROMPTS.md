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
Append this class at the end of the file:

class AboutPage(Page):
    title = models.CharField(max_length=255)
    intro = models.TextField(blank=True)
    body = RichTextField(blank=True)
    values_section = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("title"),
        FieldPanel("intro"),
        FieldPanel("body"),
        FieldPanel("values_section"),
    ]

Do not change anything else.

Output:
Return only diff. No explanation.