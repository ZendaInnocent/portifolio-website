from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Project


class ProjectListView(ListView):
    model = Project
    template_name = 'portifolio/project_list.html'
    paginate_by = 1