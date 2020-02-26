from django.shortcuts import render
from django.views.generic import TemplateView

from posts.models import Post
from projects.models import Project
from .forms import ContactForm


def index_view(request):
    context ={
        'object_list': Post.objects.all(),
        'projects': Project.objects.all(),
        'form': ContactForm()
    }
    return render(request, 'main/index.html', context)
