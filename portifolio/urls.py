from django.urls import path

from . import views

app_name = 'portifolio'

urlpatterns = [
    path('', views.ProjectListView.as_view(), name='project-list'),
    path('project-create/', views.ProjectCreateView.as_view(), name='project-create'),
    path('<slug:slug>/', views.ProjectDetailView.as_view(), name='project-detail'),
    path('<slug:slug>/update/', views.ProjectUpdateView.as_view(), name='project-update'),
    path('<slug:slug>/delete/', views.ProjectDeleteView.as_view(), name='project-delete'),
]