from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.Main, name="Main"),
    # url(r'^(?P<page>[0-9]+)/$', views.Orders_history_page, name="Orders_history_page"),
    # url(r'^delivery_address/$', views.Delivery_address, name="Delivery_address"),
    # url(r'^contact_details/$', views.Contact_details, name="Contact_details"),
    # url(r'^logout/$', views.Logout, name="Logout"),
    # url(r'change_contact_details', views.change_contact_details, name="change_contact_details"),
    # url(r'change_address', views.change_address, name="change_address"),
]
