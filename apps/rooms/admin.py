from django.contrib import admin
from apps.rooms.models import Room, ImageRoom, BackroundRoom, Comment, ImageRoom, Amenities
# Register your models here.

class ImageRoomAdmin(admin.TabularInline):
    model = ImageRoom
    extra = 5

class RoomAdmin(admin.ModelAdmin):
    inlines = (ImageRoomAdmin, )
    list_filter = ('title', )
    list_display = ('title', 'descriptions', 'price')
    search_fields = ('title', 'descriptions', 'price')
    list_per_page = 20

class CommentAdmin(admin.ModelAdmin):
    list_filter = ('name', )
    list_display = ('name', 'email', 'message', 'post', 'created')
    search_fields = ('name', 'email', 'message', 'post', 'created')
    list_per_page = 20

# admin.site.register(ImageRoom)
admin.site.register(Room, RoomAdmin)
admin.site.register(BackroundRoom)
admin.site.register(Comment, CommentAdmin)
admin.site.register(ImageRoom)
admin.site.register(Amenities)

