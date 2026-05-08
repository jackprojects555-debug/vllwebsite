from django import template
from django.utils.translation import get_language

from wagtail.models import Locale, Site

from home.models import NavigationMenu

register = template.Library()


@register.simple_tag(takes_context=True)
def language_switch_url(context, page, target_language_code):
    request = context.get("request")
    if request is None:
        return "/"

    current_language = get_language()
    if current_language == target_language_code:
        return request.get_full_path()

    try:
        target_locale = Locale.objects.get(language_code=target_language_code)
    except Locale.DoesNotExist:
        return "/"

    try:
        translated = page.get_translation_or_none(target_locale)
    except Exception:
        translated = None

    if translated is not None:
        return translated.get_url(request=request)

    site = Site.find_for_request(request)
    if site is None:
        return f"/{target_language_code}/"

    translated_root = site.root_page.get_translation_or_none(target_locale)
    if translated_root is not None:
        return translated_root.get_url(request=request)

    return f"/{target_language_code}/"


@register.simple_tag(takes_context=True)
def language_switch_url_or_none(context, page, target_language_code):
    request = context.get("request")
    if request is None:
        return None

    try:
        target_locale = Locale.objects.get(language_code=target_language_code)
    except Locale.DoesNotExist:
        return None

    try:
        translated = page.get_translation_or_none(target_locale)
    except Exception:
        translated = None

    if translated is None:
        return None

    return translated.get_url(request=request)


@register.simple_tag(takes_context=True)
def cms_navigation(context, slug="main"):
    request = context.get("request")
    if request is None:
        return None

    try:
        locale = Locale.objects.get(language_code=get_language())
    except Locale.DoesNotExist:
        locale = None

    if locale is not None:
        menu = NavigationMenu.objects.filter(slug=slug, locale=locale).first()
        if menu is not None:
            return menu

    return NavigationMenu.objects.filter(slug=slug).first()

