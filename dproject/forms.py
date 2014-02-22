from django import forms

class ContactForm(forms.Form):
    # dup of models
    # https://docs.djangoproject.com/en/1.6/topics/forms/modelforms/
    transcript = forms.CharField(max_length=100)
