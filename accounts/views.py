from django.shortcuts import render
from django.contrib.auth.models import User

def profile(request):
    # I may not need view logic, templates might be enough
    # u = User.objects.get(all)
    context = u
    return render(request, 'accounts/', context)
