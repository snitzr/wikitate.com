from django.shortcuts import render, Http404, get_object_or_404, redirect
from django.http import HttpResponse
from dproject.forms import SearchForm
from dproject.models import Vid, Transcript

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
    URLquery = request.GET.get('v')
    context = {'video_search': video_search}
    if URLquery and len(URLquery) == 11:
        return redirect('/%s/' % URLquery)
    elif len(vidId) == 11:
        v = Vid.objects.filter(vidId__contains=vidId)
        t = Transcript.objects.filter(vid__vidId__contains=vidId)
        context.update({'vidId': vidId, 'v': v, 't': t})
        return render(request, 'dproject/indexvids.html', context) 
    else:
        return notfound

def notfound(request):
    """
    Error message for unknown video ID or URL.
    Cannot recognize 11 digit errors.
    """
    message = 'Video or URL not found.'
    context = {'message': message, 'video_search': video_search}
    return render(request, 'dproject/index.html', context)
