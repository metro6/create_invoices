"""create_invoices URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.static import serve


from .views import Login, logout, invoices, redirect_to_invoices, InvoiceDetail, get_invoice_word

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += [
    url(r'login', Login.as_view()),
    url(r'logout', logout),
    url(r'invoices$', invoices),
    url(r'invoices/(?P<invoice_id>\d+)', InvoiceDetail.as_view()),
    url(r'get_invoice_word/', get_invoice_word),
    url(r'^$', redirect_to_invoices),
]


if settings.DEBUG:
    urlpatterns = [
        url(r'^media/(?P<path>.*)$', serve,
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
        ] + staticfiles_urlpatterns() + urlpatterns