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
from django.urls import path , include
from views.views import CustomerListView , CustomerDetailView , CustomerCreateView , CustomerUpdateView , CustomerDeleteView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',CustomerListView.as_view(),name='home'),
    path('/<int:pk>/',CustomerDetailView.as_view(),name='customers_details'),
    path('create/',CustomerCreateView.as_view(),name='customers_create'),
    path('/<int:pk>/update/',CustomerUpdateView.as_view(),name='customers_update'),
    path('/<int:pk>/delete/',CustomerDeleteView.as_view(),name='customers_delete'),
]

