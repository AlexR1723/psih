from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.Main, name="Main"),
    url(r'^start_test/$', views.Start_test, name="Start_test"),
    # url(r'^(?P<page>[0-9]+)/$', views.Orders_history_page, name="Orders_history_page"),
    # url(r'^delivery_address/$', views.Delivery_address, name="Delivery_address"),
    # url(r'^contact_details/$', views.Contact_details, name="Contact_details"),
    # url(r'^logout/$', views.Logout, name="Logout"),
    url(r'get_level_1', views.get_level_1, name="get_level_1"),
    url(r'get_level_2', views.get_level_2, name="get_level_2"),
    url(r'get_level_3', views.get_level_3, name="get_level_3"),
    url(r'get_result', views.get_result, name="get_result"),
    url(r'get_file_result', views.get_file_result, name="get_file_result"),
    # url(r'change_address', views.change_address, name="change_address"),
]
