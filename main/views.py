from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.conf import settings

from posts.models import Post
from portifolio.models import Project
from .forms import ContactForm


def index_view(request):
    context ={
        'featured_posts': Post.objects.filter(featured=True),
        'featured_projects': Project.objects.filter(featured=True),
        'form': ContactForm(),
    }

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data['message']
            from_email = form.cleaned_data['email']
            name = form.cleaned_data['name']

            send_mail(
                f'Mail from site. Sender: {from_email}',
                message,
                settings.EMAIL_HOST_USER,
                ['innocent@zendainnocent.com', ],
                fail_silently=False
            )
            messages.success(request, 'Your message sent successfully. I will respond within 48 hours.')
            return HttpResponseRedirect('/#contact', content='')

    return render(request, 'main/index.html', context)
