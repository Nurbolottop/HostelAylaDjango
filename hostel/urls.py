"""hostel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from apps.settings.views import index
from apps.contact.views import contact
from apps.about.views import about
from apps.rooms.views import rooms, rooms_detail
from apps.teams.views import team
from apps.blog.views import blog, blog_detail
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path("contact/", contact, name='contact'),
    path("about/", about, name='about'),
    path("rooms/", rooms, name='rooms'),
    path('rooms_detail/<int:id>/', rooms_detail, name="rooms_detail"),
    path("team/", team, name='team'),
    path("blog/", blog, name='blog'),
    path('blog_detail/<int:id>/', blog_detail, name="blog_detail"),
    
    
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
