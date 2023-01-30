from django.shortcuts import render
from apps.settings.models import Setting

from apps.contact.models import Contact
# Create your views here.

def contact(request):
    contact = Contact.objects.latest('id')
    setting = Setting.objects.latest('id')
    
    context = {
        'contact':contact,
        'setting' : setting,
        
    }
    
    return render   (request, 'contacts-1.html', context)