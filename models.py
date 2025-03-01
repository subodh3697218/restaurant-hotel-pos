from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('manager', 'Manager'),
        ('staff', 'Staff'),
        ('cashier', 'Cashier'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='staff')


# ✅ Menu Item Model with Predefined Categories
class MenuItem(models.Model):
    CATEGORY_CHOICES = [
        ('food', 'Food'),
        ('beverage', 'Beverage'),
        ('dessert', 'Dessert'),
    ]
    
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)

    def __str__(self):
        return f"{self.name} ({self.category}) - NPR {self.price}"
from django.db import models
from accounts.models import CustomUser

class MenuItem(models.Model):
    CATEGORY_CHOICES = [
        ('food', 'Food'),
        ('beverage', 'Beverage'),
        ('dessert', 'Dessert'),
    ]
    
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)

    def __str__(self):
        return f"{self.name} ({self.category}) - NPR {self.price}"

class Order(models.Model):
    table_number = models.IntegerField()
    items = models.ManyToManyField(MenuItem)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('completed', 'Completed')], default='pending')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  # Tracks who placed the order

    def __str__(self):
        return f"Order {self.id} - Table {self.table_number} ({self.status})"

class Billing(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)  # Link to order
    invoice_number = models.CharField(max_length=50, unique=True)
    payment_method = models.CharField(max_length=50, choices=[('cash', 'Cash'), ('card', 'Card'), ('online', 'Online')])
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)  # Auto-add timestamp

    def __str__(self):
        return f"Invoice {self.invoice_number} - NPR {self.total_amount}"


from django.db import models

class InventoryItem(models.Model):
    name = models.CharField(max_length=255)
    quantity = models.IntegerField()
    supplier = models.CharField(max_length=255)
    reorder_level = models.IntegerField(default=5)  # Minimum stock before reordering
    last_restocked = models.DateTimeField(auto_now_add=True)  # Track when last restocked

    def __str__(self):
        return f"{self.name} - {self.quantity} left (Reorder at {self.reorder_level})"


from django.db import models

class InventoryItem(models.Model):
    name = models.CharField(max_length=255)
    quantity = models.IntegerField()
    supplier = models.CharField(max_length=255)
    reorder_level = models.IntegerField(default=5)  # Minimum stock before reordering
    last_restocked = models.DateTimeField(auto_now_add=True)  # Track when last restocked

    def __str__(self):
        return f"{self.name} - {self.quantity} left (Reorder at {self.reorder_level})"
