# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=100)
    last = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    created_at= models.DateTimeField(auto_now=True)
    updated_at= models.DateTimeField(auto_now=True)
class Restaurant(models.Model):
    name= models.CharField(max_length=255, blank=True)
    created_at= models.DateTimeField(auto_now=True)
    updated_at= models.DateTimeField(auto_now=True)
class Category(models.Model):
    name= models.CharField(max_length=255, blank=True)
    created_at= models.DateTimeField(auto_now=True)
    updated_at= models.DateTimeField(auto_now=True)
    user_prefers = models.ManyToManyField(User, related_name = "user_prefered")   #join table between User/Categories (of food)
    restaurant_category = models.ManyToManyField(Restaurant, related_name = "restaurant_categorized")   #join table between User/Categories (of food)