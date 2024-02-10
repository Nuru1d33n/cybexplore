from django.shortcuts import render
from review import forms, models


# Create your views here.
def RateView(request):
    if request.method == "POST":
        form = forms.RateForm(request.POST)
    form = forms.RateForm
    revs = models.Rating.objects.all()
    context = {
        'form': form,
        'revs': revs,
    }
    for rev in revs:
        print(rev)
        print(rev.rate)
        print(rev.user.email)
        print(rev.profile.first_name)
    return render(request, "rate.html", context)
