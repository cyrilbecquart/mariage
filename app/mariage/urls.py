from django.conf.urls import url
from django.contrib.auth.views import login, logout_then_login
from app.mariage.views import *


urlpatterns = [
    # required login
    url(r'^login$', login, name='login'),
    #url(r'^logout$', logout_then_login, name='logout'),
    
    # home page
    url(r'^$', HomePageView.as_view(), name='home'),
    
    # pages
    url(r'^coming$', ComingPageView.as_view(), name='coming'),
    url(r'^housing$', HousingPageView.as_view(), name='housing'),
    url(r'^planning$', PlanningPageView.as_view(), name='planning'),
    url(r'^ceremony$', CeremonyPageView.as_view(), name='ceremony'),
    
    # forms
    url(r'^coming/add-carpooling$', CarpoolingFormView.as_view(), name='add_carpooling'),
    
    url(r'^test$', TestPageView.as_view(), name='test'),

]