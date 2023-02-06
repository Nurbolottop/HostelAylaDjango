from django.shortcuts import render
from apps.settings.models import Setting
from apps.about.models import About,BackroundAbout,History

from apps.contact.models import Contact
# Create your views here.

def about(request):
    contact = Contact.objects.latest('id')
    setting = Setting.objects.latest('id')
    about = About.objects.latest('id')
    backround = BackroundAbout.objects.latest('id')
    history = History.objects.all()
    context = {
        'contact':contact,
        'setting' : setting,
        'about' : about,
        'backround' : backround,
        'history' : history,
        
        
        
        
    }
    
    return render   (request, 'website/about-1.html', context)