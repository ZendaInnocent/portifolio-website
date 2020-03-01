from django.test import TestCase
from django.urls import reverse

from main.forms import ContactForm


class TestMainViews(TestCase):

    def test_index_view_GET(self):
        response = self.client.get(reverse('main:home'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/index.html')
    

    def test_index_view_POST(self):
        response = self.client.post(reverse('main:home'), data={
            'name':'Innocent', "email":'usr@me.com', 'message':'Hello'
        })

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/#contact')