from django.conf.urls import url

from app.mariage.views import HomePageView, ComingPageView, HousingPageView, TestPageView


urlpatterns = [
    # home page
    url(r'^$', HomePageView.as_view(), name='home'),
    
    url(r'^coming$', ComingPageView.as_view(), name='coming'),
    url(r'^housing$', HousingPageView.as_view(), name='housing'),
    url(r'^test$', TestPageView.as_view(), name='test'),

]