# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import FormMixin, FormView

from .forms import DriverForm, FarmerForm
from .models import Order, Driver, Farmer


class OrdersView(TemplateView):
    template_name = 'control_panel/orders.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        orders = Order.objects.all()
        context['orders'] = self.process_orders(orders)
        context['drivers'] = self.process_drivers(Driver.objects.all(), orders)

        return context

    def process_orders(self, orders):
        orders_new = []
        orders_in_progress = []
        orders_done = []
        for order in orders:
            order.pickup_address = f'{order.farmer.street} {order.farmer.house_nr} ' \
                f'{order.farmer.house_nr_extension}, {order.farmer.zipcode}'

            if order.arrival_time is None and order.driver is None:
                orders_new.append(order)
            elif order.arrival_time is None and order.driver is not None:
                orders_in_progress.append(order)
            elif order.arrival_time is not None:
                orders_done.append(order)

        return {
            'orders_new': orders_new,
            'orders_in_progress': orders_in_progress,
            'orders_done': orders_done
        }

    def process_drivers(self, drivers, orders):
        available_drivers = []
        for driver in drivers:
            found = False
            for order in orders:
                if driver == order.driver:
                    found = True
            if not found:
                available_drivers.append(driver)
        return available_drivers


class DriverView(FormView):
    template_name = 'control_panel/drivers.html'
    form_class = DriverForm
    success_url = reverse_lazy('control_panel:drivers')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['drivers'] = Driver.objects.all()

        return context

    def form_valid(self, form):
        data = form.cleaned_data
        Driver.objects.create(
            first_name=data['first_name'],
            last_name=data['last_name'],
            phone_number=data['phone_number']
        )
        return super().form_valid(form)


class FarmerView(FormView):
    template_name = 'control_panel/farmers.html'
    form_class = FarmerForm
    success_url = reverse_lazy('control_panel:farmers')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        farmers = Farmer.objects.all()
        for farmer in farmers:
            farmer.address = f'{farmer.street} {farmer.house_nr} ' \
                f'{farmer.house_nr_extension}, {farmer.zipcode}'

        context['farmers'] = farmers

        return context

    def form_valid(self, form, **kwargs):
        data = form.cleaned_data
        Farmer.objects.create(
            first_name=data['first_name'], last_name=data['last_name'],
            street=data['street'], house_nr=data['house_no'],
            house_nr_extension=data['house_suffix'], zipcode=data['zipcode'],
            phone_number=data['phone_number']
        )
        return super().form_valid(form)
