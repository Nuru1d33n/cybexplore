from django.contrib import admin
from course.models import Course, Category, Tutor

# Register your models here.

admin.site.register(Course)
admin.site.register(Category)
admin.site.register(Tutor)