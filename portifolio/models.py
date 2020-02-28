from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify

from mdeditor.fields import MDTextField


class Project(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    overview = models.CharField(max_length=140, blank=True, null=True)
    description = MDTextField()
    thumbnail = models.ImageField(upload_to='project-thumbnails')
    repo = models.URLField()
    website = models.URLField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    featured = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_on', 'title', ]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('portifolio:project-detail', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('portifolio:project-update', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('portifolio:project-delete', kwargs={'slug': self.slug})
