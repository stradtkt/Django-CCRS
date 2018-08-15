# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from .models import User, Review
import bcrypt
import datetime
# Create your views here.
def index(request):
    user = User.objects.get(id=request.session['id'])
    context = {
        "user": user
    }
    return render(request, 'ccrs/index.html', context)

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
    user = User.objects.get(id=request.session['id'])
    context = {
        "user": user
    }
    return render(request, 'ccrs/register.html', context)

def login_page(request):
    user = User.objects.get(id=request.session['id'])
    context = {
        "user": user
    }
    return render(request, 'ccrs/login.html', context)

def about(request):
    user = User.objects.get(id=request.session['id'])
    context = {
        "user": user
    }
    return render(request, 'ccrs/about.html', context)

def review(request):
    errors = Review.objects.validate_review(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error)
        return redirect('/reviews')
    else:
        user = User.objects.get(id=request.session['id'])
        rating = request.POST['rating']
        content = request.POST['content']
        Review.objects.create(user=user, rating=rating, content=content)
        messages.success(request, 'Review Added')
        return redirect("/reviews")


def reviews(request):
    user = User.objects.get(id=request.session['id'])
    reviews = Review.objects.all()
    context = {
        "user": user,
        "reviews": reviews,
    }
    return render(request, 'ccrs/reviews.html', context)

def services(request):
    user = User.objects.get(id=request.session['id'])
    context = {
        "user": user
    }
    return render(request, 'ccrs/services.html', context)

def contact(request):
    user = User.objects.get(id=request.session['id'])
    context = {
        "user": user
    }
    return render(request, 'ccrs/contact.html', context)