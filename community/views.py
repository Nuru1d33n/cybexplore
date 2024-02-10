from django.shortcuts import render

# Create your views here.
def CommunityView(request):
    context = {}
    return render(request, 'community.html', context=context)

