from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from .models import *
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.core.validators import re
from django.contrib.auth.hashers import check_password, make_password
from django.utils.html import escape

# Create your views here.


def index(request):
    if request.method == "POST":
        pass

    elif request.method == "GET":

        return render(request, "app/index.html")


def register(request):
    if request.method == "POST":
        email = request.POST["Email"]
        passowrd = escape(request.PSOT["Password"])
        name = escape(request.POST["Name"])

        if validate_email(email):
            email = escape(request.POST["Email"])

            q = User(
                Name=name,
                Email=email,
                Password=password,
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
            Password = escape(request.POST["Password"])
            print(Password)
            if Password == password:

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
