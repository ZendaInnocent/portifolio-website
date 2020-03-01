from django.urls import path

from posts import views


app_name = 'posts'

urlpatterns = [
    path('', views.PostListView.as_view(), name='post-list'),
    path('post-create/', views.PostCreateView.as_view(), name='post-create'),
    path('<slug:slug>/', views.PostDetailView.as_view(), name='post-detail'),
    path('<slug:slug>/update/', views.PostUpdateView.as_view(), name='post-update'),
    path('<slug:slug>/delete/', views.PostDeleteView.as_view(), name='post-delete'),
    path('tag/<slug:slug>/', views.TagDetailView.as_view(), name='tag-detail'),
]