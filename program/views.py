from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView

from django.contrib import messages

# Create your views here.
# views.py
from django.shortcuts import render, redirect
from program.forms import UserProgramForm

from program.models import UserProgram

def register_program(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST or None)
        if form.is_valid():
            # Handle pricing based on the selected program and duration
            program = form.cleaned_data['program']
            duration = form.cleaned_data['duration']

            if program == 'CEH':
                price = 30000 if duration == '1_month' else 60000
            elif program == 'WAPT':
                price = 50000 if duration == '1_month' else 100000
            elif program == 'FST':
                price = 60000 if duration == '1_month' else 120000
            elif program == 'FD':
                price = 60000 if duration == '1_month' else 120000
            elif program == 'BD':
                price = 50000 if duration == '1_month' else 100000
            elif program == 'HT':
                price = 60000 if duration == '1_month' else 120000

            # Process the registration or display a confirmation message
            return HttpResponse({
                'price': price,
                'program': program,
            })
            # return render(request, 'program/success.html', {'price': price})

    else:
        form = RegistrationForm()

    return render(request, 'program/register.html', {'form': form})

# class ProgramCreateView(CreateView):
#     model = UserProgram
#     form_class = UserProgramForm
#     # fields = "__all__"
#     template_name = 'program-reg.html'
    
def ProgramCreateView(request):
    if request.method == "POST":
        form = UserProgramForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Application Successful. \n We'll get in touch with you in short time.")
            return HttpResponse("UserProgram")
        else:
            messages.error(request, "Application Not Submitted due to invalid input")
    form = UserProgramForm()
    context = {
        'form': form,
    }
    template_name = 'program-reg.html'
    return render(request, template_name, context)

