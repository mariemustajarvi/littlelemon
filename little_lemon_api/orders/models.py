from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class FoodItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    is_available = models.BooleanField(default=True)
    category = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class ItemOfTheDay(models.Model):
    food_item = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return f"{self.food_item.name} - {self.date}"

class Order(models.Model):
    PENDING = 'Pending'
    DELIVERED = 'Delivered'
    ORDER_STATUSES = [
        (PENDING, 'Pending'),
        (DELIVERED, 'Delivered')
    ]
    
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    food_items = models.ManyToManyField(FoodItem)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=ORDER_STATUSES, default=PENDING)
    delivery_assigned = models.ForeignKey('DeliveryCrew', on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return f"Order #{self.id} - {self.customer.username}"

class DeliveryCrew(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='delivery_crew')
    assigned_orders = models.ManyToManyField(Order, related_name='assigned_orders')
    
    def __str__(self):
        return self.user.username


