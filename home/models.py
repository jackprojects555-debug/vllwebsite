from django.db import models

from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField
from wagtail.models import Page


class HomePage(Page):
    hero_title = models.CharField(max_length=255, blank=True)
    hero_subtitle = models.CharField(max_length=255, blank=True)
    intro_text = RichTextField(blank=True)
    contact_cta_text = models.CharField(max_length=255, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("hero_title"),
        FieldPanel("hero_subtitle"),
        FieldPanel("intro_text"),
        FieldPanel("contact_cta_text"),
    ]

class AboutPage(Page):
    intro = models.TextField(blank=True)
    body = RichTextField(blank=True)
    values_section = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("intro"),
        FieldPanel("body"),
        FieldPanel("values_section"),
    ]

class PracticeAreaPage(Page):
    short_description = models.TextField(blank=True)
    full_description = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("short_description"),
        FieldPanel("full_description"),
    ]

class AttorneysPage(Page):
    pass
    