from django.shortcuts import render, Http404, get_object_or_404, redirect
from django.http import HttpResponse
from dproject.forms import SearchForm, FormTest, LanguageModelChoiceField
from dproject.models import Vid, Transcript

# universal video_search bar
video_search = SearchForm().as_ul()

def index(request):
    """Home page AKA / AKA index"""
    context = {'video_search': video_search}
    return render(request, 'dproject/index.html', context)

def indexvids(request, vidId):
    """Find vidId from URL and show vid"""
    URLquery = request.GET.get('v')
    language_list = LanguageModelChoiceField()
    formtest = FormTest()
    context = {'video_search': video_search,
               'languages_array': language_list,
               'formtest': formtest}
    if URLquery and len(URLquery) == 11:
        return redirect('/%s/' % URLquery)
    elif len(vidId) == 11:
        v = Vid.objects.filter(vidId__contains=vidId)
        t = Transcript.objects.filter(vid__vidId__contains=vidId)
        context.update({'vidId': vidId, 'v': v, 't': t})
        return render(request, 'dproject/indexvids.html', context) 
    else:
        return notfound

def about(request):
    """About this website page"""
    context = {'video_search': video_search}
    return render(request, 'dproject/about.html', context)

def notfound(request):
    """
    Error message for unknown video ID or URL.
    Cannot recognize 11 digit missing vid errors or users/foo.
    """
    message = 'Video or URL not found.'
    context = {'message': message, 'video_search': video_search}
    return render(request, 'dproject/index.html', context)
