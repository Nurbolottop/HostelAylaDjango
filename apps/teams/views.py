from django.shortcuts import render
from apps.settings.models import Setting
from apps.teams.models import Team, BackroundTeam
from apps.contact.models import Contact
# Create your views here.

def team(request):
    contact = Contact.objects.latest('id')
    setting = Setting.objects.latest('id')
    backround = BackroundTeam.objects.latest('id')
    team = Team.objects.all()
    context = {
        'contact':contact,
        'setting' : setting,
        'backround' : backround,
        'team' : team,
        
        
    }
    
    return render   (request, 'website/team.html', context)