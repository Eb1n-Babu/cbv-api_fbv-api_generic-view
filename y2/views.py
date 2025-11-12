from django.views.generic import ListView, DetailView , CreateView, UpdateView, DeleteView
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

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


