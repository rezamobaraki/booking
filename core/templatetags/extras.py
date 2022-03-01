import json

from django import template

register = template.Library()


@register.filter
def pretty_json(value):
    return json.load(value, indent=4)