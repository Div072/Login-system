from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from .models import *
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.core.validators import re

# Create your views here.


def index(request):
    if request.method == "POST":
        pass

    elif request.method == "GET":

        return render(request, "app/index.html")


def register(request):
    if request.method == "POST":
        Email = request.POST["Email"]
        if validate_email(Email):

            q = User(
                Name=request.POST["Name"],
                Email=request.POST["Email"],
                Password=request.POST["Password"],
            )
            q.save()
            return redirect("/app/login")
        else:
            messages.info(request, "Invalidate Email")
            return redirect("/app/register")

    elif request.method == "GET":
        return render(request, "app/register.html")


def login(request):
    if request.method == "POST":
        try:

            q = User.objects.get(pk=request.POST["Email"])
            Email = q.Email
            password = q.Password
            if password == request.POST["Password"]:

                pass

            else:

                messages.info(request, "Invalid Password")
                return redirect("/app")

        except ObjectDoesNotExist:
            messages.info(request, "Invalid Email")
            return redirect("/app")

        return render(request, "app/login.html")

    elif request.method == "GET":
        return redirect("/app")


def validate_email(Email):

    if re.match("^[a-zA-Z0-9_.-]+@[a-zA-Z0-9-]+[.][a-zA-Z0-9]+", Email) != None:
        print("validate")

        return 1
    else:
        return 0
