from django import forms

class SearchForm(forms.Form):
    # dup of models
    # https://docs.djangoproject.com/en/1.6/topics/forms/modelforms/
    transcript = forms.CharField(max_length=50,
                                 label = '',
                                 widget=forms.TextInput(attrs={'placeholder': 'enter video link'}))

class FormTest(forms.Form):
    subject = forms.CharField(max_length=100)
