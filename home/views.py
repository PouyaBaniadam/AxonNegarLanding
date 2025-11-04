from django.shortcuts import render
from django.views.generic import TemplateView

from home.models import UseCase, Feature, FAQ


# Create your views here.
class Home(TemplateView):
    template_name = "home/index.html"

    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)

        use_cases = UseCase.objects.all()
        features = Feature.objects.all()
        faqs = FAQ.objects.all()[:6]

        self.kwargs["use_cases"] = use_cases
        self.kwargs["features"] = features
        self.kwargs["faqs"] = faqs

        return self.kwargs