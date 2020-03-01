from django.test import SimpleTestCase
from django.urls import resolve, reverse

from main import views


class TestMainUrls(SimpleTestCase):
 
    def test_home_url_is_resolved(self):
        home_url = reverse('main:home')
        self.assertEquals(resolve(home_url).func, views.index_view)

    def test_root_url_is_resolved(self):
        root_url = '/'
        self.assertEquals(resolve(root_url).func, views.index_view)


        
