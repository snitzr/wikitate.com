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
    video_search = ContactForm()
    return render(request, 'dproject/about.html', {'video_search': video_search})

def indexvids(request, vidId):
    # form sandbox
    video_search = ContactForm()
    # find vidId from URL
    URLquery = request.GET.get('v')
    if URLquery and len(URLquery) == 11:
        return render(request, 'dproject/indexvids.html', {'vidId': URLquery, 'video_search': video_search})
    elif len(vidId) == 11:
        return render(request, 'dproject/indexvids.html', {'vidId': vidId, 'video_search': video_search})
    else:
        return notfound

def notfound(request):
    video_search = ContactForm()
    message = 'Video or URL not found.'
    return render(request, 'dproject/index.html', {'message': message,
                                                   'video_search': video_search})
