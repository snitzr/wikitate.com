from django.shortcuts import render, Http404, get_object_or_404, redirect
from django.http import HttpResponse
from dproject.forms import SearchForm
# users
from django.contrib.auth import authenticate, login

# universal video_search bar
video_search = SearchForm().as_ul()

def index(request):
    """Home page"""
    context = {'video_search': video_search}
    return render(request, 'dproject/index.html', context)

def about(request):
    """About page"""
    context = {'video_search': video_search}
    return render(request, 'dproject/about.html', context)

def indexvids(request, vidId):
    """Find vidId from URL"""
    testvar = 'testvar'
    URLquery = request.GET.get('v')
    context = {'video_search': video_search, 'testvar': testvar}
    if URLquery and len(URLquery) == 11:
        context.update({'vidId': URLquery})
        return render(request, 'dproject/indexvids.html', context)
    elif len(vidId) == 11:
        context.update({'vidId': vidId})
        return render(request, 'dproject/indexvids.html', context) 
    else:
        return notfound

def login(request):
    return render(request, 'dproject/login.html', {'video_search': video_search})

def notfound(request):
    """
    Error message for unknown video ID or URL.
    Cannot recognize 11 digit errors.
    """
    message = 'Video or URL not found.'
    context = {'message': message, 'video_search': video_search}
    return render(request, 'dproject/index.html', context)
