from django.urls import path
from community.views import CommunityView

urlpatterns = [
    path('community/', CommunityView, name='community'),
]
