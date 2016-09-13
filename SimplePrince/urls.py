"""SimplePrince URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from contact.views import contact
from django.views.generic.base import TemplateView



urlpatterns = [

    url(r'^$', TemplateView.as_view(template_name='visitor/landing-index.html'), name='landing_index'),
    url(r'^about$', TemplateView.as_view(template_name='visitor/landing-about.html'), name='landing_about'),
    url(r'^gallery/$', TemplateView.as_view(template_name='visitor/gallery.html'), name='gallery_pics'),
    url(r'^quote/$', TemplateView.as_view(template_name='visitor/quote.html'), name='quote'),
    url(r'^Infinity-Box/$', TemplateView.as_view(template_name='visitor/boxinfo.html'), name='box' ),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^contact/', contact, name='contact' )
]
