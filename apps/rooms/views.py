from django.shortcuts import render
from apps.settings.models import Setting
from apps.rooms.models import Room,BackroundRoom

from apps.contact.models import Contact
# Create your views here.

def rooms(request):
    contact = Contact.objects.latest('id')
    setting = Setting.objects.latest('id')
    room = Room.objects.all()
    backround = BackroundRoom.objects.latest('id')
    
    context = {
        'contact':contact,
        'setting' : setting,
        'room' : room,
        'backround' : backround,
    }
    
    return render(request, 'rooms.html', context)

def rooms_detail(request, id):
    contact = Contact.objects.latest('id')
    setting = Setting.objects.latest('id')
    room = Room.objects.get(id =id)
    backround = BackroundRoom.objects.latest('id')
    
    context = {
        'contact':contact,
        'setting' : setting,
        'room' : room,
        'backround' : backround,
    }
    
    return render(request, 'room-detail.html', context)