from django import forms
from django.core.mail import send_mail


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder':'Name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'Email'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Message'}))

    def send_the_email(self):
        message = "From: {0}\n{1}".format(
            self.cleaned_data["name"] - self.cleaned_data['email'],
            self.cleaned_data['message']
        )
        send_mail(
            "Site message",
            message,
            "site@domain.com",
            ["innocent@zendainnocent.com"],
            fail_silently=False,
        )


