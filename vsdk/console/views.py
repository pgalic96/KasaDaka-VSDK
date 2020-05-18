# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from .forms import DriverForm, FarmerForm
from .models import Order, Driver, Farmer
from .utils import process_orders, process_drivers


class OrdersView(TemplateView):
    template_name = 'control_panel/orders.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        orders = Order.objects.all().order_by('production_time')
        context['orders'] = process_orders(orders)
        context['drivers'] = process_drivers(Driver.objects.all(), orders)
        return context


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
