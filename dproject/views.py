from django.shortcuts import render, Http404, get_object_or_404, redirect
from django.http import HttpResponse

def index(request):
    return render(request, 'dproject/index.html')

def about(request):
    return render(request, 'dproject/about.html')

def indexvids(request, vidId):
    URLquery = request.GET.get('v')
    if URLquery and len(URLquery) == 11:
        return render(request, 'dproject/indexvids.html', {'vidId': URLquery})
    elif len(vidId) == 11:
        return render(request, 'dproject/indexvids.html', {'vidId': vidId})
    else:
        #return HttpResponse('No Vid Found')
        return render(request, 'dproject/index.html', {'message': 'No video found.'})

def notfound(request):
    return render(request, 'dproject/index.html', {'message': 'No video found.'})
