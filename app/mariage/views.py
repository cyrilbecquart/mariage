from django.shortcuts import render
from django.views.generic.base import TemplateView, TemplateResponseMixin
from app.mariage.models import Hotel

class HomePageView(TemplateView):

    template_name = "pages/home.html"

class TestPageView(TemplateView):

    template_name = "test.html"

class WherePageView(TemplateView):

    template_name = "pages/where.html"

class HousingPageView(TemplateView):

    template_name = "pages/housing.html"
    
    def get_context_data(self, **kwargs):
        context = super(HousingPageView, self).get_context_data(**kwargs)
        context['hotels'] = Hotel.objects.all()
        return context
