from django import template
from django.contrib.staticfiles import finders

register = template.Library()

@register.simple_tag
def get_icon_bla_bla():
    icon_path = finders.find('static/srppayouts/icons/12015.png')

    #return icon_path
    return True

register.filter('get_icon_bla_bla', get_icon_bla_bla)