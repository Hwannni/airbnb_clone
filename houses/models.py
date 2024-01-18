from django.db import models

# Create your models here.
class House(models.Model):
    """Model Definition for Houses"""
    
    name = models.CharField(max_length=140)
    price = models.PositiveBigIntegerField()
    description = models.TextField()
    address = models.CharField(max_length=140)