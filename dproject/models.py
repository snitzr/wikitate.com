# coding=utf-8

from django.db import models
from datetime import datetime

class Vid(models.Model):
    VIDSOURCE = (
        ('youtube','youtube'),
        ('vimeo','vimeo'),
    )
    vidSource = models.CharField(max_length=400, choices=VIDSOURCE)
    vidId = models.CharField(max_length=400)

    def __unicode__(self):  # Python 3: def __str__(self):
        return u'%s %s' % (self.vidSource, self.vidId)


class Transcript(models.Model):
    vid = models.ForeignKey(Vid) # Django adds _id to create vid_id for its database column name
    transcript = models.CharField(max_length=5000000)
    LANGUAGES = (
        # ('initial', 'Transcript language'),
        ('af', 'Afrikaans'),
        ('id', 'Bahasa Indonesia'),
        ('ms', 'Bahasa Malaysia'),
        ('ca', 'Català'),
        ('cs', 'Čeština'),
        ('da', 'Dansk'),
        ('de', 'Deutsch'),
        ('et', 'Eesti'),
        ('en_GB', 'English (UK)'),
        ('en', 'English (US)'),
        ('es', 'Español (España)'),
        ('es_419', 'Español (Latinoamérica)'),
        ('eu', 'Euskara'),
        ('fil', 'Filipino'),
        ('fr', 'Français'),
        ('fr_CA', 'Français (Canada)'),
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
        ('pt_PT', 'Português'),
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
        ('zh_CN', '中文 (简体)'),
        ('zh_TW', '中文 (繁體)'),
        ('zh_HK', '中文 (香港)'),
        ('ja', '日本語'),
        ('ko', '한국어'),
        ('ot', 'other'),
    )
    language = models.CharField(max_length=100, choices=LANGUAGES)
    user = models.CharField(max_length=50)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


    def __unicode__(self):  # Python 3: def __str__(self):
        return u'%s %s %s' % (self.transcript, self.language, self.user)
