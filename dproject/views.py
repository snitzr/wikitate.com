from django.shortcuts import render, Http404, get_object_or_404, redirect
from django.http import HttpResponse

def index(request):
    return render(request, 'dproject/index.html')

def about(request):
    return render(request, 'dproject/about.html')

def indexvids(request, vidId):
    URLquery = request.GET.get('v')
    if URLquery:
        return render(request, 'dproject/indexvids.html', {'vidId': URLquery})
    else:
        return render(request, 'dproject/indexvids.html', {'vidId': vidId})
