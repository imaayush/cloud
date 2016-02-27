from django.conf.urls import patterns, url
from api import views



urlpatterns = patterns('',
    url(r'^invoices/$', views.invoice_list, name='invoice_list'),
    url(r'^invoices/(?P<pk>[0-9]+)/$', views.invoice_detail, name='invoice_detail'),
    )