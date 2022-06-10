from django.db import models 
from django.urls import path
from django.contrib.auth.models import User
from collections import defaultdict
from django.apps import apps

# Create your models here.
class universities(models.Model):
	institution=models.TextField(max_length=500)
	city=models.TextField(max_length=500)
	province=models.TextField(max_length=500)



class fields(models.Model):
	Agricultural=models.CharField(max_length=500)
	Art=models.CharField(max_length=500)
	Biological=models.CharField(max_length=500)
	Chemical=models.CharField(max_length=500)
	Commerce=models.CharField(max_length=500)
	Computer=models.CharField(max_length=500)
	Earth=models.CharField(max_length=500)
	Engineering=models.CharField(max_length=500)
	Management=models.CharField(max_length=500)
	Media=models.CharField(max_length=500)
	Medical=models.CharField(max_length=500)
	Physics=models.CharField(max_length=500)
	Religious=models.CharField(max_length=500)
	Social=models.CharField(max_length=500)
	Technical=models.CharField(max_length=500)





	