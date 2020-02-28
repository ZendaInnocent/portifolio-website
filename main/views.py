from django.shortcuts import render
from django.views.generic import TemplateView

from posts.models import Post
from portifolio.models import Project
from .forms import ContactForm


def index_view(request):
    context ={
        'featured_posts': Post.objects.filter(featured=True),
        'featured_projects': Project.objects.filter(featured=True),
        'form': ContactForm()
    }
    return render(request, 'main/index.html', context)
