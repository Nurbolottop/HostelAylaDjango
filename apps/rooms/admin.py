from django.contrib import admin
from apps.rooms.models import Room,BackroundRoom, Comment
# Register your models here.
admin.site.register(Room)
admin.site.register(BackroundRoom)
admin.site.register(Comment)
