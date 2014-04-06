# coding=utf-8
from django import forms
from django.forms import ModelChoiceField
from dproject import models

class SearchForm(forms.Form):
    # dup of models
    # https://docs.djangoproject.com/en/1.6/topics/forms/modelforms/
    Transcript = forms.CharField(max_length=50,
                                 label = '',
                                 widget=forms.TextInput(attrs={'placeholder': 'enter video link'}))

class FormTest(forms.Form):
    Transcript = forms.CharField(widget=forms.Textarea(attrs={'placeholder':
                                                              'Add transcript'}))

class LanguageModelChoiceField(forms.Form):
    Language = forms.ChoiceField(choices = models.Transcript.LANGUAGES,
                                 initial={'Galego'})
