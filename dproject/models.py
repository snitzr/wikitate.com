from django.db import models

class Vid(models.Model):
    vidSource = models.CharField(max_length=400)

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.vidSource


class VidId(models.Model):
    vidId = models.CharField(max_length=400)

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.vidId


class Transcript(models.Model):
    vid = models.ForeignKey(Vid)
    transcript = models.CharField(max_length=50000000)

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.transcript


class User(models.Model):
    vid = models.ForeignKey(Vid)
    user = models.CharField(max_length=50)

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.user


class Language(models.Model):
    vid = models.ForeignKey(Transcript)
    language = models.CharField(max_length=400)

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.language 
