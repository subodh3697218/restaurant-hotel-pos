
from django.shortcuts import render
from django.http import JsonResponse
from .models import *

def home(request):
    return JsonResponse({"message": "Welcome to Restaurant & Hotel POS System!"})
