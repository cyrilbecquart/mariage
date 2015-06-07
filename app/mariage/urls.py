from app.mariage.views import HomePageView
from django.conf.urls import url

urlpatterns = [
    # home page
    url(r'^$', HomePageView.as_view(), name='home'),

]