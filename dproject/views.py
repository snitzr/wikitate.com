from django.shortcuts import render, Http404, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from dproject.forms import SearchForm, FormTest, LanguageModelChoiceField
from dproject.models import Vid, Transcript

#begin generic editing views test
from django.views.generic.edit import UpdateView
from dproject.models import Vid, Transcript

class TranscriptUpdate(UpdateView):
    model = Transcript
    fields = ['transcript']
    template_name_suffix = '_update_form'
#end generic editing views test


# universal video_search bar
video_search = SearchForm().as_ul()

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
    formtest = FormTest()
    context = {'video_search': video_search,
               'languages_array': language_list,
               'formtest': formtest}
    if Vid.objects.filter(vidId__contains=vidId):
        t = Transcript.objects.filter(vid__vidId__contains=vidId)
        context.update({'t': t})
    v = Vid.objects.filter(vidId__contains=vidId)
    context.update({'vidId': vidId, 'v': v})
    if len(vidId) != 11:
        return notfound
    else:
        return render(request, 'dproject/indexvids.html', context) 

def transcript_submit(request):
    return # placeholder to not break site while commented out
    #"""Handle post data submit from trancript field"""
    #if request.method == 'POST': # If the form has been submitted...
        ## ContactForm was defined in the previous section
        #form = FormTest(request.POST) # A form bound to the POST data
        #if form.is_valid(): # All validation rules pass
            ## Process the data in form.cleaned_data
            ## ...
            #return HttpResponseRedirect('/thanks/') # Redirect after POST
    #else:
        #form = FormTest() # An unbound form
    #return render(request, 'contact.html', {
        #'form': form,
    #})

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
