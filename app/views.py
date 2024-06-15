from django.shortcuts import render

from django.views.generic import DeleteView,ListView,DetailView,CreateView,TemplateView,UpdateView
# Create your views here.

from app.models import *

from django.urls import reverse_lazy
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


class SchoolDelete(DeleteView):
    model=School
    context_object_name='schoolobj'
    success_url=reverse_lazy('SchoolList')