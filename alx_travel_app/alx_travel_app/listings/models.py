"""
Models for the listings app.
"""
from django.db import models
from django.contrib.auth.models import User

class Listing(models.Model):
    """
    Model for travel listings
    """
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title