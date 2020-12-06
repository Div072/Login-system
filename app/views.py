from django.shortcuts import render, redirect

from django.http import HttpResponse
from .models import *
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages

# Create your views here.


def index(request):
    if request.method == "POST":
        pass

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
        try:
            q = User.objects.get(pk=request.POST["Email"])
            password = q.Password
            if password == request.POST["Password"]:

                return render(request, "app/login.html")

            else:

                messages.info(request, "Invalid Password")
                return redirect("/app")

        except ObjectDoesNotExist:
            messages.info(request, "Invalid Email")
            return redirect("/app")

    elif request.method == "GET":
        return redirect("/app")
