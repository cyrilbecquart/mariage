from django import forms
from django.core.exceptions import ValidationError
from django.forms.forms import BoundField
from django.utils.translation import ugettext_lazy as _
from app.mariage.models import Carpooling

""" utils """
class FieldStackLazy(object):
    def __init__(self, form, *fields, **attrs):
        self.form, self.fields = form, fields
        self.__dict__.update(attrs)

    def __iter__(self):
        for field in self.fields:
            yield BoundField(self.form, self.form.fields[field], field)


class FieldStack(object):
    '''
    Used to create form divisions in Django forms.
    http://djangosnippets.org/snippets/2040/
    '''
    def __init__(self, *fields, **attrs):
        self.fields, self.attrs = fields, attrs

    def __get__(self, form, objtype=None):
        return FieldStackLazy(form, *self.fields, **self.attrs)


""" froms """
class CarpoolingAddForm(forms.ModelForm):
    '''
    Add a carpooling
    '''
    PLACE_CHOICES = (
        (1, _(u'1 place')),
        (2, _(u'2 places')),
        (3, _(u'3 places')),
        (4, _(u'4 places')),
        (5, _(u'5 places')),
        (6, _(u'6 places')),
        (7, _(u'7 places')),
        (8, _(u'8 places')),
        (9, _(u'9 places')),
    )
    places = forms.ChoiceField(choices=PLACE_CHOICES, 
                               required=True)
    role = forms.ChoiceField(widget=forms.RadioSelect, choices=Carpooling.ROLE_CHOICES, 
                             required=True,
                             initial='DR')
    email = forms.EmailField(required=False)
    phone = forms.CharField(required=False)
    # FieldStacks - grouping of fields
    contact_group = FieldStack('name', 'email', 'phone')
    travel_group = FieldStack('role', 'departure', 'places')

    class Meta:
        model = Carpooling
        fields = ['name', 'email', 'phone', 'role', 'places', 'departure']

    def clean(self):
        # need at least email or phone.
        if ('email' not in self.cleaned_data or self.cleaned_data['email'] == '') and \
            ('phone' not in self.cleaned_data or self.cleaned_data['phone'] == ''):
            raise ValidationError(_('You must provide an email or a phone.'))
        
        return self.cleaned_data
