from django.db import models

class Vid(models.Model):
    vidSource = models.CharField(max_length=400)
    vidId = models.CharField(max_length=400)

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.question

class Transcript(models.Model):
    vid = models.ForeignKey(Vid)
    user = models.CharField(max_length=50)
    transcript = models.CharField(max_length=50000000)
    language = models.CharField(max_length=400)

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.question

# class User(models.Model):
    # user = models.CharField(max_length=200)

    # def __unicode__(self):  # Python 3: def __str__(self):
        # return self.question
