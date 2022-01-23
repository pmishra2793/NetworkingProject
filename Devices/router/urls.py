import imp
from unicodedata import name
from django.urls import path
from . import views


urlpatterns = [
    path('get_router_details', views.get_router_details, name='Get Router Details'),
    path('add_router_details', views.add_router_details, name='Add Router Details'),
    path('update_router_details/<loopback>', views.update_router_details, name='Update Router Details'),
    path('delete_router_details', views.delete_router_details, name='Delete Router Details'),
]
