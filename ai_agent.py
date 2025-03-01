import os
import subprocess

# GitHub Configuration
GITHUB_USERNAME = "subodh3697218"
GITHUB_REPO = "restaurant-hotel-pos"
GITHUB_PAT = os.getenv("GITHUB_PAT")  # Uses an environment variable

# Set up the local repository path
REPO_PATH = r"C:\Users\DELL\Desktop\ai-agent\restaurant-hotel-pos"

def generate_code(user_prompt):
    """Generate code based on user input and save it to the correct file."""
    code_snippets = {
        "Generate Django models": ("models.py", """
from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('manager', 'Manager'),
        ('staff', 'Staff'),
        ('cashier', 'Cashier'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=255)

class Order(models.Model):
    table_number = models.IntegerField()
    items = models.ManyToManyField(MenuItem)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('completed', 'Completed')])

class Billing(models.Model):
    invoice_number = models.CharField(max_length=50, unique=True)
    payment_method = models.CharField(max_length=50)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

class HotelRoom(models.Model):
    room_number = models.CharField(max_length=10, unique=True)
    room_type = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=[('available', 'Available'), ('booked', 'Booked')])

class Booking(models.Model):
    customer_name = models.CharField(max_length=255)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()
    room = models.ForeignKey(HotelRoom, on_delete=models.CASCADE)

class InventoryItem(models.Model):
    name = models.CharField(max_length=255)
    quantity = models.IntegerField()
    supplier = models.CharField(max_length=255)
"""),
        "Generate Django views": ("views.py", """
from django.shortcuts import render
from django.http import JsonResponse
from .models import *

def home(request):
    return JsonResponse({"message": "Welcome to Restaurant & Hotel POS System!"})
""")
    }

    for key, (filename, content) in code_snippets.items():
        if key in user_prompt:
            file_path = os.path.join(REPO_PATH, filename)
            with open(file_path, 'w') as file:
                file.write(content)
            print(f"✅ {filename} generated and saved locally.")
            return

    print("⚠️ Invalid request. Please enter a valid command.")

def git_commit_push():
    """Automatically commit and push code to GitHub if there are changes."""
    os.chdir(REPO_PATH)

    # Add only if there are changes
    subprocess.run(["git", "add", "."], check=True)

    # Check if there is anything new to commit
    result = subprocess.run(["git", "status"], capture_output=True, text=True)
    if "nothing to commit" in result.stdout:
        print("✅ No changes detected. Skipping Git push.")
        return

    # Commit and push
    subprocess.run(["git", "commit", "-m", "AI generated code update"], check=True)
    subprocess.run(["git", "push", "origin", "main"], check=True)
    print("🚀 Code successfully pushed to GitHub.")

if __name__ == "__main__":
    while True:
        user_prompt = input("\n💬 Ask the AI Agent (or type 'exit' to quit): ")
        if user_prompt.lower() == "exit":
            print("👋 Exiting AI Agent.")
            break
        generate_code(user_prompt)
        git_commit_push()
