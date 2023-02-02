from django.contrib import admin
from apps.blog.models import BackroundBlog, Blog
# Register your models here.x
admin.site.register(Blog)
admin.site.register(BackroundBlog)
