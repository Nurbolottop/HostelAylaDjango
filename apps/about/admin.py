from django.contrib import admin
from apps.about.models import About,BackroundAbout, ImageAbout, History
# Register your models here.
admin.site.register(About)
admin.site.register(BackroundAbout)
admin.site.register(ImageAbout)
admin.site.register(History)

