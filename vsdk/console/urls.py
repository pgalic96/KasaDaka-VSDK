from django.urls import path

from . import views

app_name = 'control_panel'

urlpatterns = [
    path('', views.OrdersView.as_view(), name='orders'),
    path('drivers/', views.DriverView.as_view(), name='drivers'),
    path('farmers/', views.FarmerView.as_view(), name='farmers')
]