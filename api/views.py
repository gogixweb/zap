from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.

def index(request):
    if request.method == "GET":
        return JsonResponse({"message": "Hello World"})

# def check_number(request, number):
#     if request.method == "GET":
#         return J