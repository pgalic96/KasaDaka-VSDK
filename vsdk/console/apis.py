import json
from datetime import datetime
from functools import wraps

from django.http import JsonResponse, HttpResponse, HttpResponseBadRequest
from django.views.generic.base import ContextMixin, View

from vsdk.console.models import Order, Driver

from .utils import process_orders, process_drivers


def ajax_request(func):
    """
    If view returned serializable dict, returns JsonResponse with this dict as content.

    example:

        @ajax_request
        def my_view(request):
            news = News.objects.all()
            news_titles = [entry.title for entry in news]
            return {'news_titles': news_titles}
    """

    @wraps(func)
    def wrapper(request, *args, **kwargs):
        response = func(request, *args, **kwargs)
        if isinstance(response, dict):
            return JsonResponse(response)
        else:
            return response

    return wrapper


class APIFetchOrdersEndpoint(View, ContextMixin):
    @ajax_request
    def get(self, request, **kwargs):
        orders = Order.objects.all()
        orders_processed = process_orders(orders)
        drivers = Driver.objects.all()
        drivers_processed = process_drivers(drivers, orders)

        return {
            'orders': orders_processed,
            'drivers': drivers_processed
        }


class APISaveOngoingOrdersEndpoint(View, ContextMixin):

    @ajax_request
    def post(self, request, **kwargs):
        payload = json.loads(request.body)
        orders = payload.get('orders')

        if not orders:
            return HttpResponseBadRequest()

        for order in orders:
            driver_id = order['driver_id']
            order_id = order['order_id']
            driver_db = Driver.objects.filter(id=int(driver_id)).first()
            db_order = Order.objects.filter(id=int(order_id)).first()
            db_order.driver = driver_db
            db_order.production_time = datetime.now()
            db_order.save()

        return HttpResponse()



class APISaveFinishedOrdersEndpoint(View, ContextMixin):

    @ajax_request
    def post(self, request, **kwargs):
        payload = json.loads(request.body)
        orders = payload.get('orders')

        if not orders:
            return HttpResponseBadRequest()

        for order_id in orders:
            db_order = Order.objects.filter(id=int(order_id)).first()
            db_order.arrival_time = datetime.now()
            db_order.save()

        return HttpResponse()

class APIDeleteDriverEndpoint(View, ContextMixin):
    @ajax_request
    def delete(self, request, **kwargs):
        driver_id = kwargs.get('driver_id')
        Driver.objects.get(id=driver_id).delete()
        return HttpResponse()