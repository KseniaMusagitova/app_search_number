from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='home'),
    path('search/', views.search_work_order, name='search_work_order'),
]