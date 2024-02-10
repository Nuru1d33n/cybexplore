from django.shortcuts import render, redirect
from program.forms import UserProgramForm
from course.forms import CourseForm
from django.http import HttpResponse

from profiles.models import UserProfile
from django.contrib.auth.models import User
from django.contrib import messages
from review.models import Rating

# Create your views here.


def home(request):
    if request.method == "POST":
        program_form = UserProgramForm(request.POST, request.FILES)
        if program_form.is_valid():
            program_form.save()

            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            email = request.POST.get('email')
            image = request.POST.get('image')
            facebook_url = request.POST.get('facebook_url')
            twitter_url = request.POST.get('facebook_url')
            instagram_url = request.POST.get('facebook_url')

            user = User.objects.create_user(email=email,password=email)

            # users = user.save()
            user.save()
            
            profile = UserProfile.objects.create(user=user)
            profile.first_name = first_name
            profile.last_name = last_name
            profile.facebook_url = facebook_url
            profile.twitter_url = twitter_url
            profile.instagram_url = instagram_url
            profile.save()

            messages.success(request, "Application successful.")
        else:
            messages.error(request, "Application Error!!.")
    else:
        revs = Rating.objects.all()
        program_form = UserProgramForm()
    return render(request, "index.html", {
        'program_form': program_form,
        'revs': revs,
    })


