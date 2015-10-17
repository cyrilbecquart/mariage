from django.conf.urls import url

from app.mariage.views import HomePageView, WherePageView, HousingPageView


urlpatterns = [
    # home page
    url(r'^$', HomePageView.as_view(), name='home'),
    
    url(r'^where$', WherePageView.as_view(), name='where'),
    url(r'^housing$', HousingPageView.as_view(), name='housing'),

]