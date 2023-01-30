from django.shortcuts import render
from apps.settings.models import Setting, Slide
# from apps.contact.models import Contact
# from apps.rooms.models import Room

# Create your views here.
def index(request):
    setting = Setting.objects.latest('id')
    slide = Slide.objects.latest('id')
    # contact = Contact.objects.latest('id')
    
    context = {
        'setting' : setting,
        'slide' : slide,
        # 'contact' : contact,
        
    }
    return render(request, 'index.html', context)