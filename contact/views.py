# views.py

from django.shortcuts import render, redirect
from django.core.mail import send_mail
from contact.forms import ContactForm
from django.contrib import messages
from contact.models import Contact



def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            # Save the contact message to the database
            message_model = Contact.objects.create(name=name, email=email, subject=subject, message=message)
            message_model.save()

            # Send email notification
            get = send_mail(
                subject,
                f"Name: {name}\nEmail: {email}\nMessage: {message}",
                email,  # Replace with your email address
                ['Nuruadebileje@gmail.com'],  # Replace with recipient email address
                fail_silently=False,
            )
            if get:
                messages.success(request, "Message Sent.")
            else:
                messages.error(request, "Message Not sent!!!.")

            # return redirect('contact_success')  # Redirect to a success page
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})
