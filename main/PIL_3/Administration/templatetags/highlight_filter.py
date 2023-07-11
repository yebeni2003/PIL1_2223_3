import re
from django import template
from django.utils.html import mark_safe

register = template.Library()

@register.filter
def highlight(text, search_query):
    highlighted = text
    if search_query:
        regex = re.compile(re.escape(search_query), re.IGNORECASE)
        highlighted = regex.sub(
            lambda match: f'<span class="highlight" style="background-color:red">{match.group(0)}</span>',
            highlighted
        )
    return mark_safe(highlighted)
