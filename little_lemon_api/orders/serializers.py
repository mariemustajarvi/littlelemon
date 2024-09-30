from rest_framework import serializers
from .models import FoodItem, Order, ItemOfTheDay, DeliveryCrew

class FoodItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodItem
        fields = '__all__'

class ItemOfTheDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemOfTheDay
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class DeliveryCrewSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryCrew
        fields = '__all__'