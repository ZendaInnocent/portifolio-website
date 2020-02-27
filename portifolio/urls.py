from django.urls import path

from . import views

app_name = 'portifolio'

urlpatterns = [
    path('', views.ProjectListView.as_view(), name='project-list'),
]