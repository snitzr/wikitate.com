from django.shortcuts import render, Http404, get_object_or_404, redirect
from django.http import HttpResponse
from dproject.forms import ContactForm
#users
from django.contrib.auth import authenticate, login


def index(request):
    # form sandbox
    video_search = ContactForm()
    # form sandbox
    return render(request, 'dproject/index.html', {'video_search': video_search})

def about(request):
    return render(request, 'dproject/about.html')

def indexvids(request, vidId):
    URLquery = request.GET.get('v')
    if URLquery and len(URLquery) == 11:
        return render(request, 'dproject/indexvids.html', {'vidId': URLquery})
    elif len(vidId) == 11:
        return render(request, 'dproject/indexvids.html', {'vidId': vidId})
    else:
        return notfound

def notfound(request):
    message = '404: video or URL not found. Check if video is from YouTube.'
    return render(request, 'dproject/index.html', {'message': message})
