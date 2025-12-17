from django.contrib import messages
from django.http import FileResponse, JsonResponse
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView, ListView, DetailView, FormView

from root.forms import ContactForm
from root.models import UseCase, Feature, FAQ, Weblog, Release, PremiumPlan


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


class WeblogAutocompleteView(View):
    def get(self, request, *args, **kwargs):
        query = request.GET.get('q', '')
        data = []

        if query:
            results = Weblog.objects.filter(title__icontains=query)[:5]

            for item in results:
                data.append({
                    'title': item.title,
                    'url': reverse('root:weblog-detail', kwargs={'slug': item.slug}),
                    'image': item.cover_image.url if item.cover_image else None
                })

        return JsonResponse({'results': data})


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


class DownloadRelease(View):
    def get(self, request, *args, **kwargs):
        os_name = self.kwargs.get('os_name')

        latest_release = Release.objects.filter(os=os_name).latest()

        file_to_serve = latest_release.release_file

        response = FileResponse(file_to_serve, as_attachment=True)
        return response


class PremiumPlans(TemplateView):
    template_name = "root/plans.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['plans'] = PremiumPlan.objects.filter(is_active=True).order_by('price')
        return context


@method_decorator(csrf_exempt, name='dispatch')
class PaymentBridgeView(TemplateView):
    template_name = 'root/payment_bridge.html'

    def post(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)