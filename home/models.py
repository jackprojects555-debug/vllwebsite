from django.db import models

from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel
from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.fields import RichTextField
from wagtail.models import Orderable, Page, TranslatableMixin
from wagtail.snippets.models import register_snippet
from wagtail.admin.panels import PageChooserPanel


class HomePage(Page):
    subpage_types = ["home.AboutPage", "home.PracticeAreasPage", "home.AttorneysPage", "home.ContactPage"]
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

class PracticeAreasPage(Page):
    subpage_types = ["home.PracticeAreaPage"]

    intro = models.TextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("intro"),
    ]


class PracticeAreaPage(Page):
    parent_page_types = ["home.PracticeAreasPage"]
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


@register_snippet
class NavigationMenu(TranslatableMixin, ClusterableModel):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)

    panels = [
        FieldPanel("title"),
        FieldPanel("slug"),
        InlinePanel("links", label="Links"),
    ]

    def __str__(self):
        return self.title

    class Meta(TranslatableMixin.Meta):
        constraints = [
            models.UniqueConstraint(fields=["locale", "slug"], name="navigationmenu_locale_slug_uniq"),
        ]


class NavigationMenuLink(Orderable):
    menu = ParentalKey(NavigationMenu, related_name="links", on_delete=models.CASCADE)
    label = models.CharField(max_length=255)
    page = models.ForeignKey(Page, null=True, blank=True, on_delete=models.SET_NULL, related_name="+")
    external_url = models.URLField(blank=True)

    panels = [
        FieldPanel("label"),
        PageChooserPanel("page"),
        FieldPanel("external_url"),
    ]

    @property
    def url(self):
        if self.page_id:
            return self.page.url
        return self.external_url
    