from django.shortcuts import render

from django.views.generic import ListView,DetailView,CreateView,TemplateView,UpdateView
# Create your views here.

from app.models import *

class SchoolList(ListView):
    model=School
    context_object_name='Schools'

class home(TemplateView):
    template_name='app/home.html'


class SchoolDetail(DetailView):
    model=School
    context_object_name='Schoolobject'

class SchoolCreate(CreateView):
    model=School
    fields='__all__'

class SchoolUpdate(UpdateView):
    model=School
    fields='__all__'