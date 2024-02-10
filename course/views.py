from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.utils.safestring import mark_safe
from django.db.models import Q

from course.models import Course, Category

# Create your views here.

class CourseCategory(ListView):
    model = Category
    template_name = "courses_category.html"
    context_object_name = 'category'
    # queryset = Category.objects.filter(course__icontains='q')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["q"] = Category.objects.filter()
        return context
    
# class CourseByCategory(ListView):
#     model = Category
#     context_object_name = 'course_detail'
    

    
    

def CourseListView(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    categories = Category.objects.all()
    for cat in categories:
        print(cat)
    courses = Course.objects.filter(
        Q(category__slug__icontains=q) |
        Q(title__icontains=q) |
        Q(content__icontains=q)
    )
    template_name = "course.html"
    course_count = courses.count()
    dev_count = Category.objects.all().count()
    print(dev_count)
    print(course_count)
    context = {
        'categories': categories,
        'courses': courses,
        'course_count': course_count,
    }
    print(context)
    return render(request, template_name, context)


class CourseDetailView(DetailView):
    model = Course
    template_name = "course_detail.html"
    slug_field = 'slug'
    context_object_name = 'course_detail'
    


