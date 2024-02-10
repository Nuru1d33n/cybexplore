from django.urls import path
from pricing.views import PriceView

urlpatterns = [
    path('training-price/', PriceView, name='price'),
]
