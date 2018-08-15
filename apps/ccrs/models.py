# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

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
                
        if len(postData['alias']) < 3:
            errors['alias'] = "Your alias needs to be 3 or more characters"
        if len(postData['dob']) == 0:
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
        if len(postData['password']) < 4:
            errors['password'] = "Please enter a longer password, needs to be four or more characters"
        if postData['password'] != postData['confirm_pass']:
            errors['confirm_pass'] = "Passwords must match"
        return errors
            
class User(models.Model):
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    dob = models.DateField()
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
    def __str__(self):
        return alias
