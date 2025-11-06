from django.urls import path

from root import views

app_name = 'root'

urlpatterns = [
    path('', views.Home.as_view(), name='root'),
    path('faqs', views.FAQList.as_view(), name='faq-list'),
    path('weblogs', views.WeblogList.as_view(), name='weblog-list'),
    path('weblog/<str:slug>', views.WeblogDetail.as_view(), name='weblog-detail'),
]