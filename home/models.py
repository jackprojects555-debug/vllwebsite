from django.db import models

from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField
from wagtail.models import Page


class HomePage(Page):
    subpage_types = ["home.AboutPage", "home.PracticeAreaPage", "home.AttorneysPage", "home.ContactPage"]
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
    parent_page_types = ["home.HomePage"]
    short_description = models.TextField(blank=True)
    full_description = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("short_description"),
        FieldPanel("full_description"),
    ]

class AttorneysPage(Page):
    subpage_types = ["home.AttorneyPage"]
    pass

class AttorneyPage(Page):
    parent_page_types = ["home.AttorneysPage"]
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=255, blank=True)
    bio = RichTextField(blank=True)
    email = models.EmailField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("name"),
        FieldPanel("role"),
        FieldPanel("bio"),
        FieldPanel("email"),
    ]

class ContactPage(Page):
    address = models.TextField(blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=100, blank=True)
    contact_form_enabled = models.BooleanField(default=True)

    content_panels = Page.content_panels + [
        FieldPanel("address"),
        FieldPanel("email"),
        FieldPanel("phone"),
        FieldPanel("contact_form_enabled"),
    ]
    