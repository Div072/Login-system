from django.shortcuts import render, redirect

from django.http import HttpResponse
from .models import *
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.


def index(request):
    if request.method == "POST":
        contex = {
            "error_email": "Invalid Email",
        }
        try:
            q = User.objects.get(pk=request.POST["Email"])
            password = q.Password
            if password == request.POST["Password"]:

                return redirect("/app/login", request)

            else:

                contex = {
                    "error_password": "Invalid Password",
                }
            return render(request, "app/index.html", contex)

        except ObjectDoesNotExist:

            return render(request, "app/index.html", contex)

        return render(request, "app/login.html")

    elif request.method == "GET":
        return render(request, "app/index.html")


def register(request):
    if request.method == "POST":
        q = User(
            Name=request.POST["Name"],
            Email=request.POST["Email"],
            Password=request.POST["Password"],
        )
        q.save()
        return redirect("/app/login")
    elif request.method == "GET":
        return render(request, "app/register.html")


def login(request):
    if request.method == "POST":
        pass
    elif request.method == "GET":

        return render(request, "app/login.html")
