"""
URL configuration for WAPT project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static



# def trigger_error(request):
#     a = 1
#     b = 0
#     division_by_zero = a/b
#     print(division_by_zero)

    
    
    

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('', include('base.urls')),
    path('', include('blog.urls')),
    path('', include('contact.urls')),
    path('', include('course.urls')),
    path('', include('community.urls')),
    path('', include('dashboard.urls')),
    path('', include('pricing.urls')),
    path('', include('review.urls')),
    path('program/', include('program.urls')),
    
    
    # path('sentry-debug/', trigger_error),
    
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


# Serve media files during development
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

