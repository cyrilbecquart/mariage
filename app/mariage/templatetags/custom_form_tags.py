from django import template
from django.forms.widgets import CheckboxInput, RadioSelect

register = template.Library()

@register.filter(name='is_checkbox')
def is_checkbox(field):
    """
    returns true if field is boolean. Use in template {{ field|is_checkbox }}
    based on http://stackoverflow.com/questions/3927018/django-how-to-check-if-field-widget-is-checkbox-in-the-template
    """
    return isinstance(field.field.widget, CheckboxInput)

@register.filter(name='is_radio')
def is_radio(field):
    """
    returns true if field is radio buttons. Use in template {{ field|is_radio }}
    """
    return isinstance(field.field.widget, RadioSelect)