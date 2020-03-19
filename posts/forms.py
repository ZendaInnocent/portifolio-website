from django import forms

from .models import Post, Comment


class PostCreateForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = '__all__'


class CommentForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': "Your Name"}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder': "Your Email"}))
    body = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': 'Your Comment', 'rows': 4}))

    class Meta:
        model = Comment
        fields = ['name', 'email', 'body', ]