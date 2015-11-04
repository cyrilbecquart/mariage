# -*- coding: utf-8 -*-
from contextlib import contextmanager

from django.contrib.auth.models import User, UserManager
from django.core.exceptions import PermissionDenied
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.timezone import now


class AuditedModel(models.Model):
    '''
    Abstract Model that adds in audit / UID fields.
    
    Note that since this is abstract the UID is not globally unique; it is unique
    only for the concrete model where it is used (and on any children)
    '''
    created_by = models.ForeignKey(User, blank=True, null=True, related_name='%(class)s_creator')
    created_date = models.DateTimeField(_('created on'), editable=False)
    modified_by = models.ForeignKey(User, blank=True, null=True, related_name='%(class)s_modifier')
    modified_date = models.DateTimeField(_('modified on'), editable=False)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        # Some child implementations (like VersionedModel) want to persist the created_date
        # of the oldest ancestor.  This check thus allows that.
        if not self.id and not self.created_date:
            self.created_date = now()
        self.modified_date = now()
        super(AuditedModel, self).save(*args, **kwargs)

    def can_be_modified_by_user(self, user):
        '''
        Whether this model can be modified by a given user. This is used by
        the `modify_by_user` method, and by default it just returns True. Any
        subclasses should override this if they want specific permission checks.
        '''
        return True

    @contextmanager
    def modify_by_user(self, user):
        '''
        Context manager to modify an Audited Model. When called, it checks
        if the specified user is allowed to modify the model, and if so, it
        yields and sets the modified_by to the specified user.
        Raises a PermissionDenied exception if the user is not allowed to.
        '''

        if not self.can_be_modified_by_user(user):
            raise PermissionDenied(_(u'The specified user is not allowed to modify this model.'))

        self.modified_by = user
        yield
    
    @property
    def pretty_duration_since_creation(self):
        '''
        Return a human readable string of the elapsed duration since this object was created.
        '''
        if self.created_date:
            return format_duration(start_or_td=self.created_date, end=now(),
                                   format_type='long')
        return ''
    
    @property
    def last_event_date(self):
        
        if self.modified_date is None or self.modified_date == '':
            return self.created_date
        else:
            return self.modified_date


class UserProfile(AuditedModel):
    # Turn the settings LANGUAGES into a translatable list
    #LANGUAGES = map(lambda t: (t[0], _(t[1])), list(settings.LANGUAGES))

    # Latest rec from Django:
    # http://docs.djangoproject.com/en/dev/topics/auth/#storing-additional-information-about-users
    ''' Primary info '''
    user = models.OneToOneField(User, related_name='%(class)s_user')
    
    
    
# Create your models here.
class Hotel(AuditedModel):

    ''' General info '''
    name = models.CharField(_(u'name'), null=True, max_length=100)
    email = models.EmailField(_(u'email'), null=True, blank=True, max_length=100)
    phone = models.CharField(_(u'phone'), null=True, blank=True, max_length=100)
    description = models.CharField(_(u'description'), null=True, blank=True, max_length=2048)
    website = models.URLField(_(u'website'), null=True, blank=True, max_length=1024)
    price_range = models.CharField(_(u'price range'), null=True, blank=True, max_length=100)
    address = models.CharField(_(u'address'), null=True, blank=True, max_length=1024)
    latitude = models.FloatField(_(u'latitude'), blank=True, null=True)
    longitude = models.FloatField(_(u'longitude'), blank=True, null=True)
    
    def __unicode__(self):
        return "%(name)s" % self.__dict__
    
class Carpooling(AuditedModel):

    ROLE_CHOICES = (
        ('DR',_(u'driver')), 
        ('PA', _(u'passenger'))
    )
    
    name = models.CharField(_(u'name'), null=True, max_length=100)
    email = models.EmailField(_(u'email'), null=True, blank=True, max_length=100)
    phone = models.CharField(_(u'phone'), null=True, blank=True, max_length=100)
    role = models.CharField(_(u'role'), null=True, max_length=2,
                            choices=ROLE_CHOICES,
                            default='DR',
                            help_text=_(u'Do you have a car or are you looking for one?'))
    places = models.IntegerField(_(u'places'), null=True, blank=True, 
                                 validators=[MaxValueValidator(9), MinValueValidator(1)],
                                 help_text=_(u'Number of places available or number of seats you or looking for.'))
    departure = models.CharField(_(u'departure town'), null=True, blank=True, max_length=100)
    
    def __unicode__(self):
        return _(u"covoiturage avec %(name)s depuis %(departure)s") % self.__dict__
         