from django.shortcuts import render

from django.http import HttpResponse
from .models import *
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.


def index(request):
    if request.method == "POST":
        try:
            q = User.objects.get(pk=request.POST["Email"])

        except ObjectDoesNotExist:
            contex = {"error": "Invalid Email"}
            print(contex)
            return render(request, "app/index.html", contex)
        return render(request, "app/loging")

    elif request.method == "GET":
        return render(request, "app/index.html")


def register(request):
    if request.method == "POST":
        q = User(
            Name="Div", Email=request.POST["Email"], Password=request.POST["Password"]
        )
        q.save()
        return HttpResponse("POST")
    elif request.method == "GET":
        return render(request, "app/register.html")
