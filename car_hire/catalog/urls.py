from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('carlist/', views.CarListView.as_view(), name='car_list'),
    path('hirelist/', views.HireListView.as_view(), name='hire_list'),
    path('customerlist/', views.CustomerView.as_view(), name='customer_list'),
]