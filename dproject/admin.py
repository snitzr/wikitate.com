from django.contrib import admin
from dproject.models import Vid, Transcript

class TranscriptAdmin(admin.ModelAdmin):
        fields = ['vid', 'user', 'language', 'transcript']
        list_display = ['vid', 'user', 'language', 'transcript', 'created', 'modified']
        search_fields = ['transcript']


# Register your models here.
admin.site.register(Vid)
admin.site.register(Transcript, TranscriptAdmin)