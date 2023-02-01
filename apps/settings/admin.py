from django.contrib import admin

from apps.settings.models import Setting,Slide,Partners
# Register your models here.
admin.site.register(Setting)
admin.site.register(Slide)
admin.site.register(Partners)

