from django.shortcuts import render, Http404, get_object_or_404
from django.http import HttpResponse

#def index(request):
def index(request):
    return render(request, 'dproject/index.html')

def about(request):
    return render(request, 'dproject/about.html')

def indexvids(request, vidId):
    return render(request, 'dproject/sub.html', {'vidId': vidId})
