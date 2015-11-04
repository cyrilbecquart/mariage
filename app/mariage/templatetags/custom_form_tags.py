from django import template
from django.forms.widgets import CheckboxInput, RadioChoiceInput

register = template.Library()

@register.filter(name='is_checkbox')
def is_checkbox(field):
    """
    returns true if field is boolean. Use in template {{ field|is_checkbox }}
    from http://stackoverflow.com/questions/3927018/django-how-to-check-if-field-widget-is-checkbox-in-the-template
    """
    return field.field.widget.__class__.__name__ == CheckboxInput().__class__.__name__

@register.filter(name='is_radio')
def is_radio(field):
    """
    returns true if field is radio buttons. Use in template {{ field|is_radio }}
    """
    return field.field.widget.__class__.__name__ == RadioChoiceInput().__class__.__name__