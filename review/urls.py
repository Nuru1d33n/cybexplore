from django.urls import path
from review import views
urlpatterns = [
    path('review/', views.RateView, name='review'),
]

