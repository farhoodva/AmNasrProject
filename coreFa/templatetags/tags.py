from django import template
from django.core.exceptions import ObjectDoesNotExist

register = template.Library()


@register.filter()
def persian_int(string):
    persian = dict(zip("0123456789", '۰۱۲۳۴۵۶۷۸۹'))
    price = ''.join(persian.get(digit, digit) for digit in str(string))
    price = ','.join(price[::-1][i:i + 3] for i in range(0, len(price), 3))
    return price[::-1]


@register.filter()
def persian_int_not_cs(string):
    persian = dict(zip("0123456789", '۰۱۲۳۴۵۶۷۸۹'))
    converted = ''.join(persian.get(digit, digit) for digit in str(string))
    return converted
