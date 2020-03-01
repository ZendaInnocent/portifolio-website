from django.test import TestCase
from django.urls import resolve, reverse
from django.contrib.auth.models import User

from posts import views
from posts.models import Post, Tag


class TestPostsViews(TestCase):

    def setUp(self):
        self.post = Post.objects.create(
            title = 'First Post',
            thumbnail = 'assets/banner/hero-image.svg',
        )
        self.staff_user = User.objects.create_user(username='Inno',
        password='adfshou94y840', is_staff=True)
        self.user = User.objects.create_user(username='user',
        password='foiafdyohfads', is_staff=False)
    
    # # to-do
    # def test_post_list_view(self):
    #     response = self.client.get(reverse('posts:post-list'))

    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'posts/post_list.html')

    
    def test_post_detail_view(self):
        response = self.client.get(reverse('posts:post-detail',
            kwargs={'slug':self.post.slug}))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'posts/post_detail.html')


    def test_post_create_view_redirect_with_anonymous_user(self):
        response = self.client.get(reverse('posts:post-create'))

        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, '/accounts/login/?next=/blog/post-create/')


    def test_post_update_view_redirect_with_anonymous_user(self):
        response = self.client.get(reverse('posts:post-update',
            kwargs={'slug': 'some-slug'}))

        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, '/accounts/login/?next=/blog/some-slug/update/')

    
    def test_post_delete_view_redirect_with_anonymous_user(self):
        response = self.client.get(reverse('posts:post-delete',
            kwargs={'slug': 'some-slug'}))

        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, '/accounts/login/?next=/blog/some-slug/delete/')


    def test_post_create_view_with_a_staff_user(self):
        self.client.login(username='Inno', password='adfshou94y840')
        response = self.client.get(reverse('posts:post-create'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'posts/post_form.html')


    def test_post_update_view_with_a_staff_user(self):
        self.client.login(username='Inno', password='adfshou94y840')
        response = self.client.get(reverse('posts:post-update',
            kwargs={'slug': self.post.slug}))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'posts/post_update.html')


    def test_post_delete_view_with_a_staff_user(self):
        self.client.login(username='Inno', password='adfshou94y840')
        response = self.client.get(reverse('posts:post-delete',
            kwargs={'slug': self.post.slug}))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'posts/post_confirm_delete.html')


    def test_post_create_view_with_non_staff_user(self):
        self.client.login(username='user', password='foiafdyohfads')
        response = self.client.get(reverse('posts:post-create'))

        self.assertEquals(response.status_code, 403)

    
    def test_post_update_view_with_non_staff_user(self):
        self.client.login(username='user', password='foiafdyohfads')
        response = self.client.get(reverse('posts:post-update', kwargs={'slug': 'some-slug'}))

        self.assertEquals(response.status_code, 403)


    def test_post_delete_view_with_non_staff_user(self):
        self.client.login(username='user', password='foiafdyohfads')
        response = self.client.get(reverse('posts:post-delete', kwargs={'slug': 'some-slug'}))

        self.assertEquals(response.status_code, 403)
        

    def test_tag_detail_view(self):
        tag = Tag.objects.create(name='Python')
        response = self.client.get(reverse('posts:tag-detail', kwargs={'slug':tag.slug}))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'posts/post_tag_detail.html')
