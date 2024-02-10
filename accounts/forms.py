from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms

from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser



class RegisterForm(UserCreationForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                # 'placeholder':'First Name',
                'class': 'form-control'
            }
        )
    )
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                # 'placeholder':'Last Name',
                'class': 'form-control'
            }
        )
    )
    email = forms.EmailField(
        required=True, 
        # label="", 
        widget = forms.TextInput(
            attrs={
                # 'placeholder':'Email Address',
                'class': 'form-control'
            }
        )
    )
    username = forms.CharField(
        required=True, 
        # label="", 
        widget=forms.TextInput(
            attrs={
                # 'placeholder':'Choose Username',
                'class': 'form-control'
            }
        )
    )
    password1 = forms.CharField(
        required = True,
        # label = None,
        widget = forms.PasswordInput(
            attrs={
                # 'placeholder':'Password',
                'class': 'no-show',
                'value': 'adminpasswrdiscorrect',
            }
        )
    )
    password2 = forms.CharField(
        required = True,
        # label = None,
        widget = forms.PasswordInput(
            attrs={
                # 'placeholder':'Password Confirmation',
                'class': 'no-show',
                'value': 'adminpasswrdiscorrect',
            }
        )
    )
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email')



class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ("email",)


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Email / Username')
