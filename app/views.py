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

                request.session["login"] = True
            else:
                request.session["login"] = False
                messages.info(request, "Invalid Password")
                return redirect("/app")

        except ObjectDoesNotExist:
            messages.info(request, "Invalid Email")
            request.session["login"] = False
            return redirect("/app")

        return redirect("/app/login")

    elif request.method == "GET":
        try:
            if request.session["login"] == True:
                print(request.session["login"])
                return render(request, "app/login.html")
            else:
                return redirect("/app")
        except:
            return redirect("/app")


def logout(request):
    del request.session["login"]
    return redirect("/app")


def validate_email(Email):

    if re.match("^[a-zA-Z0-9_.-]+@[a-zA-Z0-9-]+[.][a-zA-Z0-9]+", Email) != None:
        return 1
    else:
        return 0
