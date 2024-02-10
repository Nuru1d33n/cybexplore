
import uuid
from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

from django.utils.text import slugify
from django.urls import reverse

User = get_user_model()

# Create your models here.

class Tutor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    linkedin_profile = models.URLField(blank=True)
    
    def __str__(self):
        return self.linkedin_profile
    
    


class Category(models.Model):
    '''Model definition for Category.'''
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='static/categories/', null=True, blank=True)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True, max_length=255, null=False, blank=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)
        
    class Meta:
        '''Meta definition for Category.'''

        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        # ordering = ('created_at', 'updated',)

    def __str__(self):
        return self.name
    


class Course(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    DURATION_CHOICES = [
        ('3 Months', '3 months'),
        ('6 Months', '6 months'),
    ]


    title = models.CharField(max_length=255)
    content = models.CharField(max_length=500)
    duration = models.CharField(max_length=22, choices=DURATION_CHOICES, default='3 Months')
    language = models.CharField(max_length=100)
    image = models.ImageField(upload_to='static/course_image/', null=True, blank=True)
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    what_you_will_learn = models.TextField()
    requirements = models.TextField()
    description = models.TextField()
    who_is_this_for = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True, editable=False, blank=True)

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.title)
        # super().save(*args, **kwargs)
        
    def save(self, *args, **kwargs):
        # Auto-generate slug from the title if not provided
        if not self.slug:
            self.slug = slugify(self.title)
        super(Course, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog_post_detail', args=[str(self.id), self.slug])

    def calculate_price(self):
        base_price = 30000
        if self.category.name != "Development":
            base_price *= 1.5
        return base_price * (2 if self.duration == '6 Months' else 1)

    @property
    def price(self):
        return self.calculate_price()
        
    class Meta:
        '''Meta definition for Category.'''

        verbose_name = 'Course'
        verbose_name_plural = 'Courses'
        ordering = ('created_date', 'updated_date',)


    def __str__(self):
        return self.title
    
    
