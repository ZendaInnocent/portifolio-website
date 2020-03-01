from django.test import TestCase
from django.urls import resolve, reverse
from django.contrib.auth.models import User

from portifolio import views
from portifolio.models import Project


class TestPortifolioViews(TestCase):

    def setUp(self):
        self.project = Project.objects.create(
            title = 'First Project',
            thumbnail = 'assets/banner/hero-image.svg',
        )
        self.staff_user = User.objects.create_user(username='Inno',
        password='adfshou94y840', is_staff=True)
        self.user = User.objects.create_user(username='user',
        password='foiafdyohfads', is_staff=False)
    
    def test_project_list_view(self):
        response = self.client.get(reverse('portifolio:project-list'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'portifolio/project_list.html')

    
    def test_project_detail_view(self):
        response = self.client.get(reverse('portifolio:project-detail',
            kwargs={'slug':self.project.slug}))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'portifolio/project_detail.html')


    def test_project_create_view_redirect_with_anonymous_user(self):
        response = self.client.get(reverse('portifolio:project-create'))

        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, '/accounts/login/?next=/portifolio/project-create/')


    def test_project_update_view_redirect_with_anonymous_user(self):
        response = self.client.get(reverse('portifolio:project-update',
            kwargs={'slug': 'some-slug'}))

        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, '/accounts/login/?next=/portifolio/some-slug/update/')

    
    def test_project_delete_view_redirect_with_anonymous_user(self):
        response = self.client.get(reverse('portifolio:project-delete',
            kwargs={'slug': 'some-slug'}))

        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, '/accounts/login/?next=/portifolio/some-slug/delete/')


    def test_project_create_view_with_a_staff_user(self):
        self.client.login(username='Inno', password='adfshou94y840')
        response = self.client.get(reverse('portifolio:project-create'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'portifolio/project_create.html')


    def test_project_update_view_with_a_staff_user(self):
        self.client.login(username='Inno', password='adfshou94y840')
        response = self.client.get(reverse('portifolio:project-update',
            kwargs={'slug': self.project.slug}))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'portifolio/project_update.html')


    def test_project_delete_view_with_a_staff_user(self):
        self.client.login(username='Inno', password='adfshou94y840')
        response = self.client.get(reverse('portifolio:project-delete',
            kwargs={'slug': self.project.slug}))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'portifolio/project_confirm_delete.html')


    def test_project_create_view_with_non_staff_user(self):
        self.client.login(username='user', password='foiafdyohfads')
        response = self.client.get(reverse('portifolio:project-create'))

        self.assertEquals(response.status_code, 403)

    
    def test_project_update_view_with_non_staff_user(self):
        self.client.login(username='user', password='foiafdyohfads')
        response = self.client.get(reverse('portifolio:project-update', kwargs={'slug': 'some-slug'}))

        self.assertEquals(response.status_code, 403)


    def test_project_delete_view_with_non_staff_user(self):
        self.client.login(username='user', password='foiafdyohfads')
        response = self.client.get(reverse('portifolio:project-delete', kwargs={'slug': 'some-slug'}))

        self.assertEquals(response.status_code, 403)
