# coding=utf-8
from django import forms
from django.forms import ModelChoiceField
from dproject import models

class SearchForm(forms.Form):
    transcript_search = forms.CharField(max_length=100,
                                 label = '',
                                 widget=forms.TextInput(attrs=
                                                        {'placeholder': 'Enter video link'}
                                                       ))

class AddTranscript(forms.Form):
    transcript = forms.CharField(widget=forms.Textarea(attrs=
                                                       {'placeholder': 'Add new transcript'}
                                                      ))

class LanguageModelChoiceField(forms.Form):
    language = forms.ChoiceField(choices = models.Transcript.LANGUAGES,
                                 #initial = 'initial'
                                )
