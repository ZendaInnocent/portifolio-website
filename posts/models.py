from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

from mdeditor.fields import MDTextField


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Tag(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)


STATUS_CHOICES = (
    (0, 'Draft'),
    (1, 'Publish'),
)


class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    content = MDTextField()
    thumbnail = models.ImageField(upload_to='thumbnails/', blank=True, null=True)
    tags = models.ManyToManyField(Tag)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    featured = models.BooleanField(default=False)
    prev_post = models.ForeignKey('self', verbose_name='Previous Post', 
        related_name='previous_post', on_delete=models.SET_NULL, null=True, blank=True)
    nxt_post = models.ForeignKey('self', verbose_name='Next Post', 
        related_name='next_post', on_delete=models.SET_NULL, null=True, blank=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)

    class Meta:
        ordering = ['-created_on', 'title', ]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('posts:post-detail', kwargs={'slug': self.slug})
  
    def get_update_url(self):
        return reverse('posts:post-update', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('posts:post-delete', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_on', ]

    def __str__(self):
        return f'Comment {self.body} by {self.name}'

