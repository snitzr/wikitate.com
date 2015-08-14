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
        if Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='af'):
            page_af = Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='af').latest('modified')
        else:
            page_af = 'No transcript for af.'

        if Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='id'):
            page_id = Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='id').latest('modified')
        else:
            page_id = 'No transcript for id'

        if Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='ms'):
            page_ms = Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='ms').latest('modified')
        else:
            page_ms = 'No transcript for ms.'

        if Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='ca'):
            page_ca = Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='ca').latest('modified')
        else:
            page_ca = 'No transcript for ca.'

        if Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='cs'):
            page_cs = Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='cs').latest('modified')
        else:
            page_cs = 'No transcript for cs.'

        if Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='da'):
            page_da = Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='da').latest('modified')
        else:
            page_da = 'No transcript for da.'


        if Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='de'):
            page_de = Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='de').latest('modified')
        else:
            page_de = 'No transcript for de.'


        if Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='et'):
            page_et = Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='et').latest('modified')
        else:
            page_et = 'No transcript for et.'


        if Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='en-GB'):
            page_en_GB = Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='en-GB').latest('modified')
        else:
            page_en_GB = 'No transcript for en-GB.'


        if Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='en'):
            page_en = Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='en').latest('modified')
        else:
            page_en = 'No transcript for en.'


        if Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='es'):
            page_es = Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='es').latest('modified')
        else:
            page_es = 'No transcript for es.'


        if Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='es-419'):
            page_es_419 = Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='es-419').latest('modified')
        else:
            page_es_419 = 'No transcript for es-419.'


        if Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='eu'):
            page_eu = Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='eu').latest('modified')
        else:
            page_eu = 'No transcript for eu.'


        if Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='fil'):
            page_fil = Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='fil').latest('modified')
        else:
            page_fil = 'No transcript for fil.'


        if Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='fr'):
            page_fr = Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='fr').latest('modified')
        else:
            page_fr = 'No transcript for fr.'


        if Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='fr-CA'):
            page_fr_CA = Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='fr-CA').latest('modified')
        else:
            page_fr_CA = 'No transcript for fr-CA.'


        if Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='gl'):
            page_gl = Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='gl').latest('modified')
        else:
            page_gl = 'No transcript for gl.'


        if Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='hr'):
            page_hr = Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='hr').latest('modified')
        else:
            page_hr = 'No transcript for hr.'


        if Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='zu'):
            page_zu = Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='zu').latest('modified')
        else:
            page_zu = 'No transcript for zu.'


        if Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='is'):
            page_is = Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='is').latest('modified')
        else:
            page_is = 'No transcript for is.'


        if Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='it'):
            page_it = Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='it').latest('modified')
        else:
            page_it = 'No transcript for it.'


        if Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='sw'):
            page_sw = Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='sw').latest('modified')
        else:
            page_sw = 'No transcript for sw.'


        if Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='lv'):
            page_lv = Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='lv').latest('modified')
        else:
            page_lv = 'No transcript for lv.'


        if Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='lt'):
            page_lt = Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='lt').latest('modified')
        else:
            page_lt = 'No transcript for lt.'


        if Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='hu'):
            page_hu = Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='hu').latest('modified')
        else:
            page_hu = 'No transcript for hu.'


        if Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='nl'):
            page_nl = Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='nl').latest('modified')
        else:
            page_nl = 'No transcript for nl.'


        if Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='no'):
            page_no = Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='no').latest('modified')
        else:
            page_no = 'No transcript for no.'


        if Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='pl'):
            page_pl = Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='pl').latest('modified')
        else:
            page_pl = 'No transcript for pl.'


        if Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='pt-PT'):
            page_pt_PT = Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='pt-PT').latest('modified')
        else:
            page_pt_PT = 'No transcript for pt-PT.'


        if Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='pt'):
            page_pt = Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='pt').latest('modified')
        else:
            page_pt = 'No transcript for pt.'


        if Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='ro'):
            page_ro = Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='ro').latest('modified')
        else:
            page_ro = 'No transcript for ro.'


        if Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='sk'):
            page_sk = Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='sk').latest('modified')
        else:
            page_sk = 'No transcript for sk.'


        if Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='sl'):
            page_sl = Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='sl').latest('modified')
        else:
            page_sl = 'No transcript for sl.'


        if Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='fi'):
            page_fi = Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='fi').latest('modified')
        else:
            page_fi = 'No transcript for fi.'


        if Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='sv'):
            page_sv = Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='sv').latest('modified')
        else:
            page_sv = 'No transcript for sv.'


        if Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='vi'):
            page_vi = Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='vi').latest('modified')
        else:
            page_vi = 'No transcript for vi.'


        if Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='tr'):
            page_tr = Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='tr').latest('modified')
        else:
            page_tr = 'No transcript for tr.'


        if Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='bg'):
            page_bg = Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='bg').latest('modified')
        else:
            page_bg = 'No transcript for bg.'


        if Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='ru'):
            page_ru = Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='ru').latest('modified')
        else:
            page_ru = 'No transcript for ru.'


        if Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='sr'):
            page_sr = Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='sr').latest('modified')
        else:
            page_sr = 'No transcript for sr.'


        if Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='uk'):
            page_uk = Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='uk').latest('modified')
        else:
            page_uk = 'No transcript for uk.'


        if Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='el'):
            page_el = Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='el').latest('modified')
        else:
            page_el = 'No transcript for el.'


        if Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='iw'):
            page_iw = Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='iw').latest('modified')
        else:
            page_iw = 'No transcript for iw.'


        if Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='ur'):
            page_ur = Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='ur').latest('modified')
        else:
            page_ur = 'No transcript for ur.'


        if Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='ar'):
            page_ar = Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='ar').latest('modified')
        else:
            page_ar = 'No transcript for ar.'


        if Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='fa'):
            page_fa = Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='fa').latest('modified')
        else:
            page_fa = 'No transcript for fa.'


        if Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='mr'):
            page_mr = Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='mr').latest('modified')
        else:
            page_mr = 'No transcript for mr.'


        if Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='hi'):
            page_hi = Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='hi').latest('modified')
        else:
            page_hi = 'No transcript for hi.'


        if Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='bn'):
            page_bn = Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='bn').latest('modified')
        else:
            page_bn = 'No transcript for bn.'


        if Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='gu'):
            page_gu = Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='gu').latest('modified')
        else:
            page_gu = 'No transcript for gu.'


        if Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='ta'):
            page_ta = Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='ta').latest('modified')
        else:
            page_ta = 'No transcript for ta.'


        if Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='te'):
            page_te = Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='te').latest('modified')
        else:
            page_te = 'No transcript for te.'


        if Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='kn'):
            page_kn = Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='kn').latest('modified')
        else:
            page_kn = 'No transcript for kn.'


        if Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='ml'):
            page_ml = Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='ml').latest('modified')
        else:
            page_ml = 'No transcript for ml.'


        if Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='th'):
            page_th = Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='th').latest('modified')
        else:
            page_th = 'No transcript for th.'


        if Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='am'):
            page_am = Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='am').latest('modified')
        else:
            page_am = 'No transcript for am.'


        if Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='zh-CN'):
            page_zh_CN = Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='zh-CN').latest('modified')
        else:
            page_zh_CN = 'No transcript for zh-CN.'


        if Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='zh-TW'):
            page_zh_TW = Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='zh-TW').latest('modified')
        else:
            page_zh_TW = 'No transcript for zh-TW.'


        if Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='zh-HK'):
            page_zh_HK = Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='zh-HK').latest('modified')
        else:
            page_zh_HK = 'No transcript for zh-HK.'


        if Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='ja'):
            page_ja = Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='ja').latest('modified')
        else:
            page_ja = 'No transcript for ja.'


        if Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='ko'):
            page_ko = Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='ko').latest('modified')
        else:
            page_ko = 'No transcript for ko.'


        if Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='ot'):
            page_ot = Transcript.objects.filter(vid__vidId__contains=vidId, language__contains='ot').latest('modified')
        else:
            page_ot = 'No transcript for ot.'


        latest_transcripts = [page_af, page_id, page_ms, page_ca, page_cs, page_da, page_de, page_et, page_en_GB, page_en, page_es, page_es_419, page_eu, page_fil, page_fr, page_fr_CA, page_gl, page_hr, page_zu, page_is, page_it, page_sw, page_lv, page_lt, page_hu, page_nl, page_no, page_pl, page_pt_PT, page_pt, page_ro, page_sk, page_sl, page_fi, page_sv, page_vi, page_tr, page_bg, page_ru, page_sr, page_uk, page_el, page_iw, page_ur, page_ar, page_fa, page_mr, page_hi, page_bn, page_gu, page_ta, page_te, page_kn, page_ml, page_th, page_am, page_zh_CN, page_zh_TW, page_zh_HK, page_ja, page_ko, page_ot] # TODO: how to add only the variables that exist to latest_transcripts?
        context.update({'latest_transcripts': latest_transcripts})
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
