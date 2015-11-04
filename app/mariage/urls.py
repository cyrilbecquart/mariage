from django.conf.urls import url

from app.mariage.views import HomePageView, ComingPageView, HousingPageView, TestPageView, CarpoolingFormView


urlpatterns = [
    # home page
    url(r'^$', HomePageView.as_view(), name='home'),
    
    # pages
    url(r'^coming$', ComingPageView.as_view(), name='coming'),
    url(r'^housing$', HousingPageView.as_view(), name='housing'),
    
    # forms
    url(r'^coming/add-carpooling$', CarpoolingFormView.as_view(), name='add_carpooling'),
    
    url(r'^test$', TestPageView.as_view(), name='test'),

]