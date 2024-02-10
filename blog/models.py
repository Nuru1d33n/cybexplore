# models.py

import uuid
from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

from django.utils.text import slugify
from django.urls import reverse

User = get_user_model()

class BlogPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='static/blog_images/', null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True, editable=False, default=uuid.uuid4)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog_post_detail', args=[str(self.id), self.slug])

    def __str__(self):
        return self.title

