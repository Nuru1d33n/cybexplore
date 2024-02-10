# admin.py

from django.contrib import admin
from blog.models import BlogPost

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'created_date', 'updated_date')
    search_fields = ['title', 'content']

admin.site.register(BlogPost, BlogPostAdmin)
