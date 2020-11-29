from django.shortcuts import render, get_list_or_404, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
<<<<<<< HEAD
from django.http import HttpResponseRedirect
=======
>>>>>>> 976608b211e8bfb508bc4200d409bea05876e3ee

from posts.models import Post, Tag, Comment
from posts.forms import PostCreateForm, CommentForm


class PostListView(ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'posts/post_list.html'
    paginate_by = 9


class PostDetailView(DetailView):
    model = Post
    template_object_name = 'post'
    template_name = 'posts/post_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['comment_form'] = CommentForm()
        return context\

    def post(self, request, slug):
        post = self.get_object()
        if self.request.method == 'POST':
            form = CommentForm(self.request.POST)
            if form.is_valid():
                form.instance.post_id = post.id
                form.save()
            else:
                form = CommentForm()
        return HttpResponseRedirect(reverse('posts:post-detail', kwargs={'slug': post.slug}))


class PostCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    form_class = PostCreateForm
    template_name = 'posts/post_form.html'

    def test_func(self):
        if self.request.user.is_authenticated and self.request.user.is_staff:
            return True
        return False


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    model = Post
    form_class = PostCreateForm
    template_name = 'posts/post_update.html'
    success_message = 'Post updated successful.'

    def test_func(self):
        if self.request.user.is_authenticated and self.request.user.is_staff:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('posts:post-list')
    success_message = 'Post deleted successful.'

    def test_func(self):
        if self.request.user.is_authenticated and self.request.user.is_staff:
            return True
        return False


class TagDetailView(DetailView):
    model = Tag
    template_name = 'posts/post_tag_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tag = Tag.objects.get(slug=self.kwargs['slug'])
<<<<<<< HEAD
        context['object_list'] = tag.post_set.filter(status=1)
=======
        context['object_list'] = tag.post_set.all()
>>>>>>> 976608b211e8bfb508bc4200d409bea05876e3ee
        return context