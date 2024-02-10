from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from blog.models import BlogPost


# Create your views here.
def blogview(request):
    # if request.user.is_autheticated:
    #     return HttpResponse("Authen")
    # else:
    blog = BlogPost.objects.all()
    content = {'blog': blog}
    return render(request, "blog.html", content)
    
    
# def blog_post_detail(request, post_id, slug):
#     if request.user.is_autheticated:
#         return HttpResponse("Authen")
#     else:
#         post = get_object_or_404(BlogPost, id=post_id, slug=slug)
#         context = {'post': post}
#         return render(request, 'blog/post_detail.html', context)
    
def blog_post_detail(request, slug):
    # if request.user.is_autheticated:
    #     return HttpResponse("Authen")
    # else:
    post = get_object_or_404(BlogPost, slug=slug)
    context = {'post': post}
    return render(request, 'post_detail.html', context)
    