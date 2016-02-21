#from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from app.mariage.models import Hotel, Carpooling, Song
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
        context['hotels'] = Hotel.objects.all().order_by('order')
        return context


class CeremonyPageView(LoginRequiredMixin, TemplateView):

    template_name = "pages/ceremony.html"

    def get_context_data(self, **kwargs):
        context = super(CeremonyPageView, self).get_context_data(**kwargs)
        context['songs'] = Song.objects.all().order_by('order')
        return context


class VoyagePageView(LoginRequiredMixin, TemplateView):

    template_name = "pages/voyage.html"


class VisitPageView(LoginRequiredMixin, TemplateView):

    template_name = "pages/visit.html"



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
