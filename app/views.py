from django.shortcuts import render

from django.views.generic import ListView
# Create your views here.

from app.models import *

class SchoolList(ListView):
    model=School
    context_object_name='Schools'