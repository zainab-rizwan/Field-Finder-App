from django.shortcuts import render
from django.core.files import File
from django.http import HttpResponse
from .models import *
import csv, io


def home(request):
	return render(request, 'finder/home.html')

def quiz(request):
	return render(request, 'finder/quiz.html')

def majors(request):
	data=fields.objects.all()
	context={
	"obj1":data
	}
	return render(request, 'finder/majors.html',context)

def institutions(request):
	data= universities.objects.all()
	context= {
	"obj2":data
	}
	return render(request, 'finder/institutions.html', context)

def merit(request):
	return render(request, 'finder/merit.html')

def new(request):
	data=fields.objects.all()
	context={
	"obj1":data
	}
	return render(request, 'finder/new.html',context)