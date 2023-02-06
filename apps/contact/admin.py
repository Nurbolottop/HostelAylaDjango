from django.contrib import admin
from  apps.contact.models import Contact,BackroundContact,Comment
# Register your models here.

admin.site.register(Contact)
admin.site.register(BackroundContact)
admin.site.register(Comment)


