# coding=utf-8
from django.shortcuts import render, Http404, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from dproject.forms import SearchForm, AddTranscript, LanguageModelChoiceField
from django.forms.formsets import formset_factory
from dproject.models import Vid, Transcript
from django.core.urlresolvers import reverse
import re


# universal video_search bar
video_search = SearchForm()
def video_serch_submit(request, searchInput):
    if request.method == 'POST' and videoSearch.is_valid():
        # videoSearch = SearchForm(request.POST)
        return HttpResponseRedirect('/%s/' % searchInput)
        # return HttpResponseRedirect('/%s/' % 'http://127.0.0.1:8000/3BJ9YXy6zQk/')


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
        # start latest transcripts queries

        page = {}

        if Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='af'):
            page['page_af'] = Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='af').latest('modified')

        if Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='id'):
            page_id = Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='id').latest('modified')

        if Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='ms'):
            page['page_ms'] = Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='ms').latest('modified')

        if Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='ca'):
            page['page_ca'] = Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='ca').latest('modified')

        if Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='cs'):
            page['page_cs'] = Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='cs').latest('modified')

        if Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='da'):
            page['page_da'] = Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='da').latest('modified')

        if Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='de'):
            page['page_de'] = Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='de').latest('modified')

        if Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='et'):
            page['page_et'] = Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='et').latest('modified')

        if Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='en-GB'):
            page['page_en_GB'] = Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='en-GB').latest('modified')

        if Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='en'):
            page['page_en'] = Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='en').latest('modified')

        if Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='es'):
            page['page_es'] = Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='es').latest('modified')

        if Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='es-419'):
            page['page_es_419'] = Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='es-419').latest('modified')

        if Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='eu'):
            page['page_eu'] = Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='eu').latest('modified')

        if Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='fil'):
            page['page_fil'] = Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='fil').latest('modified')

        if Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='fr'):
            page['page_fr'] = Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='fr').latest('modified')

        if Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='fr-CA'):
            page['page_fr_CA'] = Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='fr-CA').latest('modified')

        if Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='gl'):
            page['page_gl'] = Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='gl').latest('modified')

        if Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='hr'):
            page['page_hr'] = Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='hr').latest('modified')

        if Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='zu'):
            page['page_zu'] = Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='zu').latest('modified')

        if Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='is'):
            page['page_is'] = Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='is').latest('modified')

        if Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='it'):
            page['page_it'] = Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='it').latest('modified')

        if Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='sw'):
            page['page_sw'] = Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='sw').latest('modified')

        if Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='lv'):
            page['page_lv'] = Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='lv').latest('modified')

        if Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='lt'):
            page['page_lt'] = Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='lt').latest('modified')

        if Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='hu'):
            page['page_hu'] = Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='hu').latest('modified')

        if Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='nl'):
            page['page_nl'] = Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='nl').latest('modified')

        if Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='no'):
            page['page_no'] = Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='no').latest('modified')

        if Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='pl'):
            page['page_pl'] = Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='pl').latest('modified')

        if Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='pt-PT'):
            page['page_pt_PT'] = Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='pt-PT').latest('modified')

        if Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='pt'):
            page['page_pt'] = Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='pt').latest('modified')

        if Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='ro'):
            page['page_ro'] = Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='ro').latest('modified')

        if Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='sk'):
            page['page_sk'] = Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='sk').latest('modified')

        if Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='sl'):
            page['page_sl'] = Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='sl').latest('modified')

        if Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='fi'):
            page['page_fi'] = Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='fi').latest('modified')

        if Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='sv'):
            page['page_sv'] = Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='sv').latest('modified')

        if Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='vi'):
            page['page_vi'] = Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='vi').latest('modified')

        if Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='tr'):
            page['page_tr'] = Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='tr').latest('modified')

        if Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='bg'):
            page['page_bg'] = Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='bg').latest('modified')

        if Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='ru'):
            page['page_ru'] = Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='ru').latest('modified')

        if Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='sr'):
            page['page_sr'] = Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='sr').latest('modified')

        if Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='uk'):
            page['page_uk'] = Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='uk').latest('modified')

        if Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='el'):
            page['page_el'] = Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='el').latest('modified')

        if Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='iw'):
            page['page_iw'] = Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='iw').latest('modified')

        if Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='ur'):
            page['page_ur'] = Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='ur').latest('modified')

        if Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='ar'):
            page['page_ar'] = Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='ar').latest('modified')

        if Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='fa'):
            page['page_fa'] = Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='fa').latest('modified')

        if Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='mr'):
            page['page_mr'] = Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='mr').latest('modified')

        if Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='hi'):
            page['page_hi'] = Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='hi').latest('modified')

        if Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='bn'):
            page['page_bn'] = Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='bn').latest('modified')

        if Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='gu'):
            page['page_gu'] = Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='gu').latest('modified')

        if Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='ta'):
            page['page_ta'] = Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='ta').latest('modified')

        if Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='te'):
            page['page_te'] = Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='te').latest('modified')

        if Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='kn'):
            page['page_kn'] = Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='kn').latest('modified')

        if Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='ml'):
            page['page_ml'] = Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='ml').latest('modified')

        if Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='th'):
            page['page_th'] = Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='th').latest('modified')

        if Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='am'):
            page['page_am'] = Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='am').latest('modified')

        if Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='zh-CN'):
            page['page_zh_CN'] = Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='zh-CN').latest('modified')

        if Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='zh-TW'):
            page['page_zh_TW'] = Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='zh-TW').latest('modified')

        if Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='zh-HK'):
            page['page_zh_HK'] = Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='zh-HK').latest('modified')

        if Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='ja'):
            page['page_ja'] = Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='ja').latest('modified')

        if Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='ko'):
            page['page_ko'] = Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='ko').latest('modified')

        if Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='ot'):
            page['page_ot'] = Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='ot').latest('modified')



        context.update(page)
        # end latest transcripts queries
    v = Vid.objects.filter(vidId__contains=vidId)
    context.update({'vidId': vidId, 'v': v})
    if len(vidId) != 11:
        return notfound
    else:
        return render(request, 'dproject/indexvids.html', context) 

"""
TODO: Refactor to prevent bogus data being written for nonexistentent 11 char
string URLs
"""
def transcript_submit(request, vidId):
    """Handle POST data submit from transcript field"""
    if request.method == 'POST': # If the form has been submitted...
        languageForm = LanguageModelChoiceField(request.POST) # A form.py function bound to POST data
        transcriptForm = AddTranscript(request.POST) # A form.py function bound to POST data
        try:
            Vid.objects.get(vidId=vidId).pk
        except:
            # determine if youtube or vimeo source
            # TODO: refactor RegEx for edge cases
            if re.search('[a-zA-Z]', vidId): #check for characters in vidId. only YT has characters
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
            # todo: add value scrub here
            TranscriptData = Transcript(
                            transcript=transcript,
                            language=languageForm.cleaned_data['language'],
                            # TODO: write vid object if nonexistent.
                            # what if vidID nonexistent? Primary key would not link. It's not added in the try / except above?
                            vid_id=Vid.objects.get(vidId=vidId).pk
                            # need user here, too?
                )
            TranscriptData.save()
            # need a success or fail message here
            # best case scenario, go to next screen
            return HttpResponseRedirect('/%s/' % vidId)
        else:
            #return # TODO: add redirect code either way and message
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
    """About this website static page"""
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
