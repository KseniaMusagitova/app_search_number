from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='home'),
    path('search/', views.search_serial_number, name='search_serial_number'),
]