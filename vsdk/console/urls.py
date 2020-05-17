from django.urls import path

from . import views
from .apis import APIFetchOrdersEndpoint, APISaveOngoingOrdersEndpoint, \
    APISaveFinishedOrdersEndpoint, APIDeleteDriverEndpoint

app_name = 'control_panel'

urlpatterns = [
    path('', views.OrdersView.as_view(), name='orders'),
    path('drivers/', views.DriverView.as_view(), name='drivers'),
    path('farmers/', views.FarmerView.as_view(), name='farmers'),
    path('orders/refresh', APIFetchOrdersEndpoint.as_view(), name='refresh_orders'),
    path('orders/saveOngoing', APISaveOngoingOrdersEndpoint.as_view(), name='save_ongoing_orders'),
    path('orders/saveFinished', APISaveFinishedOrdersEndpoint.as_view(), name='save_finished_orders'),
    path('drivers/delete/<int:driver_id>', APIDeleteDriverEndpoint.as_view(), name='delete_driver')

]
