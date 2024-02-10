from django.urls import path
from course.views import CourseListView, CourseDetailView, CourseCategory

urlpatterns = [
    path('course/category/', CourseCategory.as_view(), name="course_category"),
    path('course/', CourseListView, name="course_list"),
    path('course/<slug:slug>/', CourseDetailView.as_view(), name="course_detail"),
]
