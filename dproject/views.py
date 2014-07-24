from django.shortcuts import render, Http404, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from dproject.forms import SearchForm, AddTranscript, LanguageModelChoiceField
from dproject.models import Vid, Transcript
from django.core.urlresolvers import reverse
import re


# universal video_search bar
video_search = SearchForm()
def video_serch_submit(request, searchInput):
    if request.method == 'POST' and videoSearch.is_valid():
        # videoSearch = SearchForm(request.POST)
            return HttpResponseRedirect('%s/' % searchInput)


# drafting universal video_search functionality
# need page or url.py for this function
# check template action
def video_search_submit(request):
    if request.method == 'POST' and searchForm.is_valid():
        searchForm = SearchForm(request.POST)
        return HttpResponseRedirect('/%s/' % searchForm.cleaned_data)
    else:
        return


def index(request):
    """Home page AKA / AKA index"""
    context = {'video_search': video_search}
    return render(request, 'dproject/index.html', context)

def indexvidsurl(request, vidId):
    """Find vidId from URL and show vid else redirect"""
    URLquery = request.GET.get('v')
    if URLquery and len(URLquery) == 11:
        return HttpResponseRedirect('/%s/' % URLquery)
    elif len(vidId) != 11:
        return notfound

def indexvids(request, vidId):
    URLquery = request.GET.get('v')
    language_list = LanguageModelChoiceField()
    addtranscript = AddTranscript()
    context = {'video_search': video_search,
               'languages_array': language_list,
               'addtranscript': addtranscript}
    if Vid.objects.filter(vidId__contains=vidId):
        t = Transcript.objects.filter(vid__vidId__contains=vidId)
        context.update({'t': t})
    v = Vid.objects.filter(vidId__contains=vidId)
    context.update({'vidId': vidId, 'v': v})
    if len(vidId) != 11:
        return notfound
    else:
        return render(request, 'dproject/indexvids.html', context) 

"""
Refactor to prevent bogus data being written for nonexistant 11 char
string URLs
"""
def transcript_submit(request, vidId):
    """Handle post data submit from transcript field"""
    if request.method == 'POST': # If the form has been submitted...
        languageForm = LanguageModelChoiceField(request.POST) # A form.py function bound to POST data
        transcriptForm = AddTranscript(request.POST) # A form.py function bound to POST data
        try:
            Vid.objects.get(vidId=vidId).pk
        except:
            # determine if youtube or vimeo source
            if re.search('[a-zA-Z]', vidId):
                vidSource='youtube'
            else:
                vidSource='vimeo'
            # assign source and vidId
            VidData = Vid(
                vidSource=vidSource,
                vidId=vidId)
            VidData.save()
        if transcriptForm.is_valid() and languageForm.is_valid(): # All validation rules pass
            # Get primary key and save the data from .cleaned_data
            transcript=transcriptForm.cleaned_data['transcript']
            # add braces. need check if braces exist in POST data
            # commenting out for now for two step transcript and timing design
            # transcript = '{ ' + transcript + ' }'
            # .5 does not work as timestamp. 0.5, does
            TranscriptData = Transcript(
                            transcript=transcript,
                            language=languageForm.cleaned_data['language'],
                            vid_id=Vid.objects.get(vidId=vidId).pk)
                            # need user here, too
            TranscriptData.save()
            # need a success or fail message here
            # best case scenario, go to next screen
            return HttpResponseRedirect('/%s/' % vidId)
            # return HttpResponseRedirect('/%s/blagh' % vidId)
        else:
            #return # add redirect code either way and message
            return HttpResponseRedirect('/%s/' % vidId)
    else:
        #return # add redirect code either way and message
        return HttpResponseRedirect('/%s/' % vidId)

# second step for creating transcript, the timing page.
# currently unimplemented
def set_vid_timing(request):
    context = 'test'
    return render(request, '', context)

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
