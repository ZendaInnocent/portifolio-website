from django.test import TestCase
from django.core import mail
from main import forms


class TestForm(TestCase):
    
    def test_valid_contact_form_sends_email(self):
        form = forms.ContactForm({
            'name': "Innocent Zenda",
            'email': 'zendainnocent@gmail.com',
            'message': 'Hi there',
        })

        self.assertTrue(form.is_valid())
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'Site message')


    def test_invalid_contact_form(self):
        form = forms.ContactForm({
            'message': "Hi there"
        })
        self.assertFalse(form.is_valid())