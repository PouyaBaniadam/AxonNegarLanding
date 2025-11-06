from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

from root.models import UseCase, Feature, FAQ, Weblog


# Create your views here.
class Home(TemplateView):
    template_name = "root/index.html"

    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)

        use_cases = UseCase.objects.all()
        features = Feature.objects.all()
        faqs = FAQ.objects.all()[:6]

        self.kwargs["use_cases"] = use_cases
        self.kwargs["features"] = features
        self.kwargs["faq_list"] = faqs

        return self.kwargs


class FAQList(ListView):
    model = FAQ


class WeblogList(ListView):
    model = Weblog


class WeblogDetail(DetailView):
    model = Weblog

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["weblogs"] = Weblog.objects.all()

        return context