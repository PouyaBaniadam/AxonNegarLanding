from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, FormView

from root.forms import ContactForm
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
    paginate_by = 8


class WeblogDetail(DetailView):
    model = Weblog

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["related_weblogs"] = Weblog.objects.exclude(id=self.object.id)

        return context


class AboutUs(TemplateView):
    template_name = "root/about.html"


class ContactUs(FormView):
    template_name = "root/contact.html"
    form_class = ContactForm
    success_url = reverse_lazy('root:contact-us')

    def form_valid(self, form):
        form.save()

        messages.success(self.request, 'پیام شما با موفقیت ارسال شد.')

        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'لطفاً خطاهای فرم را برطرف کرده و دوباره تلاش کنید.')
        return super().form_invalid(form)


class Download(TemplateView):
    template_name = "root/download.html"