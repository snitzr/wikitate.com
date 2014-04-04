# coding=utf-8
from django import forms

LANGUAGE_CHOICES = (
                    ('af', 'Afrikaans'),
                    ('id', 'Bahasa Indonesia'),
                    ('ms', 'Bahasa Malaysia'),
                    ('ca', 'Català'),
                    ('cs', 'Čeština'),
                    ('da', 'Dansk'),
                    ('de', 'Deutsch'),
                    ('et', 'Eesti'),
                    ('en-GB', 'English (UK)'),
                    ('en', 'English (US)'),
                    ('es', 'Español (España)'),
                    ('es-419', 'Español (Latinoamérica)'),
                    ('eu', 'Euskara'),
                    ('fil', 'Filipino'),
                    ('fr', 'Français'),
                    ('fr-CA', 'Français (Canada)'),
                    ('gl', 'Galego'),
                    ('hr', 'Hrvatski'),
                    ('zu', 'IsiZulu'),
                    ('is', 'Íslenska'),
                    ('it', 'Italiano'),
                    ('sw', 'Kiswahili'),
                    ('lv', 'Latviešu valoda'),
                    ('lt', 'Lietuvių'),
                    ('hu', 'Magyar'),
                    ('nl', 'Nederlands'),
                    ('no', 'Norsk'),
                    ('pl', 'Polski'),
                    ('pt-PT', 'Português'),
                    ('pt', 'Português (Brasil)'),
                    ('ro', 'Română'),
                    ('sk', 'Slovenčina'),
                    ('sl', 'Slovenščina'),
                    ('fi', 'Suomi'),
                    ('sv', 'Svenska'),
                    ('vi', 'Tiếng Việt'),
                    ('tr', 'Türkçe'),
                    ('bg', 'Български'),
                    ('ru', 'Русский'),
                    ('sr', 'Српски'),
                    ('uk', 'Українська'),
                    ('el', 'Ελληνικά'),
                    ('iw', 'עברית'),
                    ('ur', 'اردو'),
                    ('ar', 'العربية'),
                    ('fa', 'فارسی'),
                    ('mr', 'मराठी'),
                    ('hi', 'हिन्दी'),
                    ('bn', 'বাংলা'),
                    ('gu', 'ગુજરાતી'),
                    ('ta', 'தமிழ்'),
                    ('te', 'తెలుగు'),
                    ('kn', 'ಕನ್ನಡ'),
                    ('ml', 'മലയാളം '),
                    ('th', 'ภาษาไทย'),
                    ('am', 'አማርኛ'),
                    ('zh-CN', '中文 (简体)'),
                    ('zh-TW', '中文 (繁體)'),
                    ('zh-HK', '中文 (香港)'),
                    ('ja', '日本語'),
                    ('ko', '한국어'),
                )
                
class SearchForm(forms.Form):
    # dup of models
    # https://docs.djangoproject.com/en/1.6/topics/forms/modelforms/
    transcript = forms.CharField(max_length=50,
                                 label = '',
                                 widget=forms.TextInput(attrs={'placeholder': 'enter video link'}))

class LanguageDeclaration(forms.Form):
    langauge = forms.MultipleChoiceField(required=True,
                                         widget=forms.CheckboxSelectMultiple,
                                         choices=LANGUAGE_CHOICES)

class FormTest(forms.Form):
    subject = forms.CharField(widget=forms.Textarea)
