from .views import *
from .form import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView



class CustomerListView(ListView):
    model = Customer
    context_object_name = 'customers'
    queryset = Customer.objects.all()
    template_name = 'customers_list.html'

class CustomerDetailView(DetailView):
    model = Customer
    context_object_name = 'customer'
    queryset = Customer.objects.all()
    template_name = 'customers_details.html'

class CustomerCreateView(CreateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'customers_create.html'
    success_url = '/'

class CustomerUpdateView(UpdateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'customers_create.html'
    success_url = '/'

class CustomerDeleteView(DeleteView):
    model = Customer
    context_object_name = 'customer'
    queryset = Customer.objects.all()
    template_name = 'customers_delete.html'
    success_url = '/'

