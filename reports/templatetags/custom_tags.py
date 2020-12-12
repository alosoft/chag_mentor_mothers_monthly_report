

from django import template

register = template.Library()

@register.inclusion_tag('login.html', takes_context=False)
def generate_table():
    return {
        'report': 'report'
    }

@register.filter
def get_first_name(value):
    splitted = value.split(' ')
    return splitted[0]