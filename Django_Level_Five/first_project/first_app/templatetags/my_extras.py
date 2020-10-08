from django import template

register = template.Library()

#@register.filter(name='cut')
def cut(value,arg):
    return value.replace(arg,'ba')

register.filter('cut1',cut)
