
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.db import models
class UserManager(models.Manager):
    def validate_user(self, postData):
        errors = {}
        # validate first and last name
        if len(postData['first_name']) < 2 and not postData['first_name'].isalpha():
            if len(postData['first_name']) < 2: 
                errors['first_len'] = "Your name needs to be 2 or more characters"
            if not postData['first_name'].isalpha():
                errors['first_alpha'] = "Your first name can only contain letters"
        if len(postData['last_name']) < 2 and not postData['last_name'].isalpha():
            if len(postData['last_name']) < 2: 
                errors['last_len'] = "Your name needs to be 2 or more characters"
            if not postData['last_name'].isalpha():
                errors['last_alpha'] = "Your first name can only contain letters"
        if postData['dob'] == "":
            errors['dob'] = "Your date of birth cannot be empty"
        # validate email
        try:
            validate_email(postData['email'])
        except ValidationError:
            errors['email'] = "Your email is not valid"
        else:
            if User.objects.filter(email=postData['email']):
                errors['email'] = "This email already exists"

        # validate password
        if len(postData['password']) < 8:
            errors['password'] = "Please enter a longer password, needs to be 8 or more characters"
        if postData['password'] != postData['confirm_pass']:
            errors['confirm_pass'] = "Passwords must match"
        return errors
            
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    dob = models.DateField()
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
    def __str__(self):
        return self.email

class ReviewManager(models.Manager):
    def validate_review(self, postData):
        errors = {}
        if len(postData['rating']) == 0:
            errors['rating'] = "You need to add a rating"
        if len(postData['content']) < 5:
            errors['content'] = "You need to add 5 or more characters for the review"
        return errors

class Review(models.Model):
    user = models.ForeignKey(User, related_name="review")
    rating = models.IntegerField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ReviewManager()
