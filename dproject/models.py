# coding=utf-8

from django.db import models

class Vid(models.Model):
    vidSource = models.CharField(max_length=400)
    vidId = models.CharField(max_length=400)

    def __unicode__(self):  # Python 3: def __str__(self):
        return u'%s %s' % (self.vidSource, self.vidId)


class Transcript(models.Model):
    vid = models.ForeignKey(Vid)
    transcript = models.CharField(max_length=50000000)
    LANGUAGES = (
            ('fr', 'French'),
            ('uk', 'Українська'),
    )
    language = models.CharField(max_length=100, choices=LANGUAGES)
    user = models.CharField(max_length=50)
    def __unicode__(self):  # Python 3: def __str__(self):
        return u'%s %s %s' % (self.transcript, self.language, self.user)
