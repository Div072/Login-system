from django.shortcuts import render

from django.http import HttpResponse
from .models import *
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.


def index(request):
    return render(request, "app/index.html")


def login(request):
    if request.method == "POST":
        try:
            q = User.objects.get(pk=request.POST["Email"])

        except ObjectDoesNotExist:
            return HttpResponse("Null")
        return HttpResponse(q.Email)
    else:
        return HttpResponse("GET")
