from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import FoodItem, Order, ItemOfTheDay, DeliveryCrew
from .serializers import FoodItemSerializer, OrderSerializer, ItemOfTheDaySerializer, DeliveryCrewSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser

# Customer views
class FoodItemListView(generics.ListAPIView):
    queryset = FoodItem.objects.filter(is_available=True)
    serializer_class = FoodItemSerializer

class ItemOfTheDayView(generics.RetrieveAPIView):
    queryset = ItemOfTheDay.objects.all()
    serializer_class = ItemOfTheDaySerializer

class OrderCreateView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(customer=self.request.user)

# Manager views
class FoodItemManagementView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FoodItem.objects.all()
    serializer_class = FoodItemSerializer
    permission_classes = [IsAdminUser]

class UpdateItemOfTheDayView(generics.UpdateAPIView):
    queryset = ItemOfTheDay.objects.all()
    serializer_class = ItemOfTheDaySerializer
    permission_classes = [IsAdminUser]

class AssignDeliveryView(generics.UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAdminUser]

# Delivery crew views
class AssignedOrdersView(generics.ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(delivery_assigned=self.request.user.delivery_crew)

class UpdateOrderStatusView(generics.UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        if self.request.user.delivery_crew == serializer.instance.delivery_assigned:
            serializer.save(status=Order.DELIVERED)