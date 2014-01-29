from django.shortcuts import render
from django.http import HttpResponse
# from django.template import RequestContext, loader

def index(request):
    return render(request, 'dproject/index.html')

def vidResponse(request, vid_id):
    return render(request, 'dproject/index.html')
    # return HttpResponse("You're voting on polls %s." % vid_id)
