from django.urls import path

from root import views

app_name = 'root'

urlpatterns = [
    path('', views.Home.as_view(), name='root'),
    path('faqs', views.FAQList.as_view(), name='faq-list'),
    path('weblogs', views.WeblogList.as_view(), name='weblog-list'),
    path('weblog/<str:slug>', views.WeblogDetail.as_view(), name='weblog-detail'),
    path('about-axonnegar', views.AboutUs.as_view(), name='about-axonnegar'),
    path('contact-us', views.ContactUs.as_view(), name='contact-us'),
    path('downloads', views.Download.as_view(), name='downloads'),
    path('download/<str:os_name>/', views.DownloadRelease.as_view(), name='download-release'),
    path('api/search/', views.WeblogAutocompleteView.as_view(), name='search-autocomplete'),
]