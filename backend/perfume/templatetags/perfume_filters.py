from django import template
from perfume.models import Perfume

register = template.Library()

TYPE_CHOICES_DICT = dict(Perfume.TYPE_CHOICES)

@register.filter
def type_description(value):
    return TYPE_CHOICES_DICT.get(value, 'Неизвестный тип')
