from django.shortcuts import render
from django.http import HttpResponseRedirect
from .zap import Zap
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def index(request):
    if request.method == "GET":
        if 'url_input' in request.GET:
            number = request.GET["url_input"]
            zap = Zap(number)
            return HttpResponseRedirect(f'https://wa.me/{zap.converted_number}')

        return render(request, "api/index.html")
    if request.method == "POST":
        number = request.POST["url_input"]
        zap = Zap(number)
        return HttpResponseRedirect(f'https://wa.me/{zap.converted_number}')