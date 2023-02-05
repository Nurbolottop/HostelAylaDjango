from django.contrib import admin
from apps.blog.models import BackroundBlog, Blog, Comment, ImageBlog
# Register your models here.x
admin.site.register(Blog)
admin.site.register(BackroundBlog)
admin.site.register(Comment)
admin.site.register(ImageBlog)


