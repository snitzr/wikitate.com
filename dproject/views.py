from django.shortcuts import render, Http404
from django.http import HttpResponse

def index(request):
    return render(request, 'dproject/index.html')

def vidResponse(request, vid_id):
    return render(request, 'dproject/index.html')
