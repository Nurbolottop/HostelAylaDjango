from django.shortcuts import render
from apps.settings.models import Setting,Slide
from apps.contact.models import Contact
# from apps.rooms.models import Room

# Create your views here.
def index(request):
    setting = Setting.objects.latest('id')
    contact = Contact.objects.latest('id')
    slide = Slide.objects.all()
    context = {
        'setting' : setting,
        'contact' : contact,
        'slide': slide
        
    }
    return render(request, 'index.html', context)