"""
URL configuration for little_lemon_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from .views import FoodItemListView, ItemOfTheDayView, OrderCreateView, \
    FoodItemManagementView, UpdateItemOfTheDayView, AssignDeliveryView, \
    AssignedOrdersView, UpdateOrderStatusView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('food-items/', FoodItemListView.as_view(), name='food-items'),
    path('item-of-the-day/', ItemOfTheDayView.as_view(), name='item-of-the-day'),
    path('create-order/', OrderCreateView.as_view(), name='create-order'),
    
    # Manager endpoints
    path('manage-food-item/<int:pk>/', FoodItemManagementView.as_view(), name='manage-food-item'),
    path('update-item-of-the-day/<int:pk>/', UpdateItemOfTheDayView.as_view(), name='update-item-of-the-day'),
    path('assign-delivery/<int:pk>/', AssignDeliveryView.as_view(), name='assign-delivery'),
    
    # Delivery crew endpoints
    path('assigned-orders/', AssignedOrdersView.as_view(), name='assigned-orders'),
    path('update-order-status/<int:pk>/', UpdateOrderStatusView.as_view(), name='update-order-status'),
]
