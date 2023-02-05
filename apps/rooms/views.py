from django.shortcuts import render,redirect
from apps.settings.models import Setting
from apps.rooms.models import Room,BackroundRoom,Comment, ImageRoom, Amenities

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
    
    return render(request, 'rooms/rooms.html', context)

def rooms_detail(request, id):
    contact = Contact.objects.latest('id')
    setting = Setting.objects.latest('id')
    room = Room.objects.get(id =id)
    backround = BackroundRoom.objects.latest('id')
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        comment = Comment.objects.create(name = name,email = email, message = message, post = room )
        
        return redirect('rooms_detail', room.id)
    
    context = {
        'contact':contact,
        'setting' : setting,
        'room' : room,
        'backround' : backround,
    }
    
    return render(request, 'rooms/room-detail.html', context)