from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView

from .models import *

# Create your views here.
def index(request):
     return render(request, 'tasks/list.html')
   
   