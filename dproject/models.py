from django.db import models

# Create your models here.
class Vid(models.Model):
    vidSource = models.CharField(max_length=200)
    vidId = models.CharField(max_length=200)

class Trans(models.Model):
    vid = models.ForeignKey(Vid)
    transcript = models.CharField(max_length=200)

# class TransIndividual(models.Model):
    # nessesary? not sure how to build a db model for each user submitted transcript.
    # trans_set

# class Languages(models.Model):
    # add all languges here and it can form a choice set that can become a
    # dropdown
