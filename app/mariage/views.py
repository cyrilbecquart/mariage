from django.conf import settings
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.utils.translation import ugettext_lazy as _
from django.views.generic.base import TemplateView, TemplateResponseMixin
from django.views.generic.edit import FormView
from app.mariage.models import Hotel, Carpooling
from app.mariage.forms import CarpoolingAddForm



class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)


""" pages views """
class HomePageView(LoginRequiredMixin, TemplateView):

    template_name = "pages/home.html"


class TestPageView(LoginRequiredMixin, TemplateView):

    template_name = "test.html"


class PlanningPageView(LoginRequiredMixin, TemplateView):

    template_name = "pages/planning.html"


class ComingPageView(LoginRequiredMixin, TemplateView):

    template_name = "pages/coming.html"

    def get_context_data(self, **kwargs):
        context = super(ComingPageView, self).get_context_data(**kwargs)
        context['carpoolings'] = Carpooling.objects.all()
        return context    


class HousingPageView(LoginRequiredMixin, TemplateView):

    template_name = "pages/housing.html"
    
    def get_context_data(self, **kwargs):
        context = super(HousingPageView, self).get_context_data(**kwargs)
        context['hotels'] = Hotel.objects.all()
        return context


class CeremonyPageView(LoginRequiredMixin, TemplateView):

    template_name = "pages/ceremony.html"



""" forms views """

class CarpoolingFormView(LoginRequiredMixin, FormView):
    template_name = 'forms/carpooling.html'
    form_class = CarpoolingAddForm
    success_url = reverse_lazy('coming')

    def get_initial(self):
        """
        Returns the initial data to use for forms on this view.
        """
        initial = super(CarpoolingFormView, self).get_initial()
        print initial
        initial['role'] = self.request.GET['role']
    
        return initial

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.clean()
        form.save()
        return super(CarpoolingFormView, self).form_valid(form)
