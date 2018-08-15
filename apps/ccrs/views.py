# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from .models import *
import bcrypt
import datetime
# Create your views here.
def index(request):
    return render(request, 'ccrs/index.html')

def login(request):
    email = request.POST['email']
    password = request.POST['password']
    user = User.objects.filter(email=email)
    if len(user) > 0:
        is_pass = bcrypt.checkpw(password.encode(), user[0].password.encode())
        if is_pass:
            request.session['id'] = user[0].id
            messages.success(request, 'Logged In!')
            return redirect('/reviews')
        else:
            messages.error(request, "Incorrect email and/or password")
            return redirect('/login-page')
    else:
        messages.error(request, "User does not exist")
    return redirect('/login-page')

def register(request):
    errors = User.objects.validate_user(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error)
        return redirect('/register-page')
    else:
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        dob = request.POST['dob']
        password = request.POST['password']
        hashed_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        User.objects.create(first_name=first_name, last_name=last_name, email=email, dob=dob, password=hashed_pw)
        messages.success(request, 'User Registered')
        return redirect('/login-page')

def logout(request):
    request.session.clear()
    return redirect('/')

def register_page(request):
    return render(request, 'ccrs/register.html')

def login_page(request):
    return render(request, 'ccrs/login.html')

def about(request):
    return render(request, 'ccrs/about.html')

def reviews(request):
    return render(request, 'ccrs/reviews.html')

def services(request):
    return render(request, 'ccrs/services.html')

def contact(request):
    return render(request, 'ccrs/contact.html')