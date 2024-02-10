from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views
from django.contrib.auth import get_user_model

from django.views import generic
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.http import HttpResponse

from program.models import UserProgram


from accounts.forms import LoginForm, RegisterForm

from program.models import UserProgram
from django.contrib import messages

User = get_user_model()

class LoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'accounts/login.html'


from accounts.forms import RegisterForm

from program.forms import UserProgramForm

from profiles.models import UserProfile
from django.core.mail import send_mail


def RegisterView(request):
    if request.method == "POST":
        # register_form = RegisterForm(request.POST)
        program_form = UserProgramForm(request.POST, request.FILES)
        if program_form.is_valid():
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            email = request.POST.get('email')
            program_form.save()

            user = User.objects.create_user(
                    email=email,
                    password=email,
                )
            print(first_name)
            print(last_name)
            print(email)

            print(user)
            send_mail(
                subject='A cool subject',
                message='A stunning message',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[settings.RECIPIENT_ADDRESS]
            )

            # user = register_form.save()
            user_profile = UserProfile(user=user)
            user_profile.save()
            return HttpResponse("Account Created")

    template_name = 'accounts/register.html'
    program_form = UserProgramForm()
    # register_form = RegisterForm()
    context = {
        'program_form': program_form,
        # 'register_form': register_form,
    }
    return render(request, template_name, context)

