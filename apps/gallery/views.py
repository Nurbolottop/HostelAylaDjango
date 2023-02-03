from django.shortcuts import render
from apps.settings.models import Setting
from apps.gallery.models import Gallery
from apps.contact.models import Contact
# Create your views here.

def gallery(request):
    contact = Contact.objects.latest('id')
    setting = Setting.objects.latest('id')
    # backround = BackroundContact.objects.latest('id')
    gallery = Gallery.objects.all()
    context = {
        'contact':contact,
        'setting' : setting,
        'gallery' : gallery,
        
        # 'backround' : backround,
        
    }
    
    return render   (request, 'gallery.html', context)