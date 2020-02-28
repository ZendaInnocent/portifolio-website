from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy, reverse

from .models import Project
from .forms import ProjectCreateForm


class ProjectListView(ListView):
    model = Project
    template_name = 'portifolio/project_list.html'
    paginate_by = 9

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'portifolio/project_detail.html'
    template_object_name = 'project'


class ProjectCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Project
    form_class = ProjectCreateForm
    template_name = 'portifolio/project_create.html'

    def test_func(self):
        if self.request.user.is_authenticated and self.request.user.is_staff:
            return True
        return False

class ProjectUpdateView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    model = Project
    form_class = ProjectCreateForm
    template_name = 'portifolio/project_update.html'
    success_message = 'Project updated successful.'

    def test_func(self):
        if self.request.user.is_authenticated and self.request.user.is_staff:
            return True
        return False

class ProjectDeleteView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, DeleteView):
    model = Project
    success_message = 'Project deleted successful.'
    success_url = reverse_lazy('portifolio:project-list')

    def test_func(self):
        if self.request.user.is_authenticated and self.request.user.is_staff:
            return True
        return False
