# -*- coding: utf-8 -*-
from django import template
from django.utils.safestring import mark_safe

import locale
register = template.Library()


@register.filter()
def isk(value):
    """format float value as ISK"""
    ## removed 'long' for python3 support rolled long -> int
    if not isinstance(value, (int, float, complex)):
        return '-'
    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
    result = '<span class="isk">{0}&nbsp;ISK</span>'.format(
        locale.format("%.2f", value, grouping=True)
    )
    return mark_safe(result)
