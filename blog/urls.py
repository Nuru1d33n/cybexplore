from django.urls import path
from blog.views import blogview, blog_post_detail


urlpatterns = [
    path('blog', blogview, name="blogview"),
    # path('blog/<slug:slug>/', blog_post_detail, name='blog_post_detail'),
    path('blog/<slug:slug>/', blog_post_detail, name='blog_post_detail'),
    # path('blog/<uuid:post_id>/<slug:slug>/', blog_post_detail, name='blog_post_detail'),
]



