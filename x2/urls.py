"""
URL configuration for x2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from y2.views import  StudentViewSet , customer_list , customer_create, customer_detail , customer_delete , customer_update , CustomerViewSet


urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/', StudentViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('student/<int:pk>',StudentViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),

    path('customers/',customer_list,name='customer_list'),
    path('customers/create/',customer_create,name='customer_create'),
    path('customers/<int:pk>',customer_detail,name='customer_detail'),
    path('customers/<int:pk>/delete',customer_delete,name='customer_delete'),
    path('customers/<int:pk>/update',customer_update,name='customer_update'),

    path('customer/', CustomerViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('customer/<int:pk>', CustomerViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),



]
