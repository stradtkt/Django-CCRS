# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

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
            return redirect('/')
        else:
            messages.error(request, "Incorrect email and/or password")
            return redirect('/')
    else:
        messages.error(request, "User does not exist")
    return redirect('/')

def register(request):
    errors = User.objects.validate_user(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error)
        return redirect('/')
    else:
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        dob = request.POST['dob']
        password = request.POST['password']
        hashed_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        User.objects.create(name=name, alias=alias, email=email, dob=dob, password=hashed_pw)
        messages.success(request, 'User Registered')
        return redirect('/')

def logout(request):
    request.session.clear()
    return redirect('/')

def reqister_page(request):
    return render(request, 'ccrs/register.html')

def login_page(request):
    return render(request, 'ccrs/login.html')