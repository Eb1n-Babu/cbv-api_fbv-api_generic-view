from django.shortcuts import render
from django.views.generic import ListView, DetailView , CreateView, UpdateView, DeleteView
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .form import CustomerForm
from .models import Student, Customer
from .serializers import studentSerializer, customerSerializer


# Create your views here.
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = studentSerializer

class StudentsView(ListView):
    model = Student
    template_name = 'students.html'
    context_object_name = 'students'

@api_view(['GET'])
def customer_list(request):
    try:
        queryset = Customer.objects.all()
        serializer = customerSerializer(queryset, many=True)
        return Response(serializer.data)
    except Customer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
@api_view(['GET'])
def customer_detail(request, pk):
    try:
        queryset = Customer.objects.get(id=pk)
        serializer = customerSerializer(queryset)
        return Response(serializer.data)
    except Customer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
@api_view(['POST'])
def customer_create(request):
    serializer = customerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['PUT'])
def customer_update(request, pk):
    try:
        queryset = Customer.objects.get(id=pk)
        serializer = customerSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Customer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
@api_view(['DELETE'])
def customer_delete(request, pk):
    try:
        queryset = Customer.objects.get(id=pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Customer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = customerSerializer

class CustomerListView(ListView):
    model = Customer
    template_name = 'customers_list.html'
    context_object_name = 'customers'
    fields = '__all__'
class CustomerDetailView(DetailView):
    model = Customer
    template_name = 'customers_details.html'
    context_object_name = 'customer'
class CustomerCreateView(CreateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'customers_create.html'
    context_object_name = 'customer'
    success_url = "/cus"
class CustomerUpdateView(UpdateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'customers_update.html'
    context_object_name = 'customer'
    success_url = '/cus'
class CustomerDeleteView(DeleteView):
    model = Customer
    template_name = 'customers_delete.html'
    context_object_name = 'customer'
    success_url = "/cus"

def cus_view(request):
    customer =  Customer.objects.all()
    return render(request, 'cus_view.html', {'customer': customer})

