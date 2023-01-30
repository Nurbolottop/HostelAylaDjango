from django.shortcuts import render
from apps.settings.models import Setting

from apps.contact.models import Contact,BackroundContact
# Create your views here.

def contact(request):
    contact = Contact.objects.latest('id')
    setting = Setting.objects.latest('id')
    backround = BackroundContact.objects.latest('id')
    
    context = {
        'contact':contact,
        'setting' : setting,
        'backround' : backround,
        
    }
    
    return render   (request, 'contact-1.html', context)