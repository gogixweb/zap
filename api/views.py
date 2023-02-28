from django.shortcuts import render
from django.http import HttpResponseRedirect
from .zap import Zap
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def index(request):
    if request.method == "GET":
        return render(request, "api/index.html")
    # if request.method == "GET" and request.GET['q'] is not None:
    #     number = request.GET['q']
    #     zap = Zap(number)
    #     return HttpResponseRedirect(f'https://wa.me/{zap.converted_number}')
    if request.method == "POST":
        number = request.POST["url_input"]
        print(request.POST)
        print(request)
        print(number)
        zap = Zap(number)
        return HttpResponseRedirect(f'https://wa.me/{zap.converted_number}')