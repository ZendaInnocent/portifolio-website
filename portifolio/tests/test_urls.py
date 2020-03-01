from django.test import SimpleTestCase
from django.urls import resolve, reverse

from portifolio import views


class TestPortifolioUrls(SimpleTestCase):

    def test_project_list_url_is_resolved(self):
        list_url = reverse('portifolio:project-list')
        self.assertEquals(resolve(list_url).func.view_class, views.ProjectListView)


    def test_project_detail_url_is_resolved(self):
        detail_url = reverse('portifolio:project-detail', kwargs={'slug': 'some-slug'})
        self.assertEquals(resolve(detail_url).func.view_class, views.ProjectDetailView)


    def test_project_create_url_is_resolved(self):
        create_url = reverse('portifolio:project-create')
        self.assertEquals(resolve(create_url).func.view_class, views.ProjectCreateView)


    def test_project_update_url_is_resolved(self):
        update_url = reverse('portifolio:project-update', kwargs={'slug': 'some-slug'})
        self.assertEquals(resolve(update_url).func.view_class, views.ProjectUpdateView)


    def test_project_delete_url_is_resolved(self):
        delete_url = reverse('portifolio:project-delete', kwargs={'slug': 'some-slug'})
        self.assertEquals(resolve(delete_url).func.view_class, views.ProjectDeleteView)