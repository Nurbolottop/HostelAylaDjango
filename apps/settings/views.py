from django.shortcuts import render
from apps.settings.models import Setting,Slide, Partners
from apps.contact.models import Contact
from apps.about.models import About
from apps.rooms.models import Room


# from apps.rooms.models import Room

# Create your views here.
def index(request):
    room = Room.objects.all()
    
    setting = Setting.objects.latest('id')
    contact = Contact.objects.latest('id')
    slide = Slide.objects.all()
    about = About.objects.latest('id')
    partners = Partners.objects.all()
    
    context = {
        'setting' : setting,
        'contact' : contact,
        'slide': slide,
        'about' : about,
        'room' : room,
        'partners' : partners,
        
        
        
    }
    return render(request, 'index.html', context)