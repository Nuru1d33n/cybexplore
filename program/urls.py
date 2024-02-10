# urls.py
from django.urls import path
from program.views import register_program, ProgramCreateView

urlpatterns = [
    path('register/', register_program, name='register_program'),
    path('apply/', ProgramCreateView, name='reg_program'),
    # Add other URLs as needed
]
