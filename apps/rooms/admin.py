from django.contrib import admin
from apps.rooms.models import Room,BackroundRoom, Comment, ImageRoom, Amenities
# Register your models here.
admin.site.register(Room)
admin.site.register(BackroundRoom)
admin.site.register(Comment)
admin.site.register(ImageRoom)
admin.site.register(Amenities)

