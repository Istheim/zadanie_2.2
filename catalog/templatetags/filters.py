from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
def split(text):
    """Обрезает переданный текст до 100 символов"""
    result = text[0:100]
    return mark_safe(result)


@register.simple_tag
def mediapath(val):
    if val:
        return f'/media/{val}'
    return '/media/no_photo.jpg'
