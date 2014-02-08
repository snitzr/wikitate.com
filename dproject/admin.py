from django.contrib import admin
from dproject.models import Vid, VidId,  Transcript, User, Language

# Register your models here.
admin.site.register(Vid)
admin.site.register(VidId)
admin.site.register(Transcript)
admin.site.register(User)
admin.site.register(Language)
