from multiprocessing import context
from turtle import title
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.list import ListView
from numpy import empty
from requests import request
from .models import Task
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class TaskList(ListView):
    model = Task
    context_object_name = 'tasks'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(complete=False).count()
        ordering = ['-time_posted']
        search_input = self.request.GET.get('search-area') or ''

        if search_input:
            context['tasks'] = context['tasks'].filter(title__icontains=search_input)
        
        context['search_input'] = search_input    
    
        return context

class TaskDetail(DetailView):
    model = Task
    context_object_name= 'task'
    template_name = 'todo_list/task.html'


class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields= ['title','description','complete']
    success_url= reverse_lazy('tasks')

    def form_valid(self,form):
        form.instance.user = self.request.user
        return super(TaskCreate,self).form_valid(form)

class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields= ['title','description','complete']
    success_url= reverse_lazy('tasks')

class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name= 'task'
    success_url= reverse_lazy('tasks')
