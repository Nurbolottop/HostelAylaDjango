from django.shortcuts import render,redirect
from apps.settings.models import Setting
from django.core.mail import send_mail
from apps.contact.models import Contact,BackroundContact,Comment
# Create your views here.

def contact(request):
    contact = Contact.objects.latest('id')
    setting = Setting.objects.latest('id')
    backround = BackroundContact.objects.latest('id')
    if request.method == "POST":
        name  = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        Comment.objects.create(name = name, email = email, message = message)

        send_mail(
            f'{message}',
            f'Здравствуйте, {name}. Спасибо за ваше сообщение. Мы свяжемся с вами в ближайшее время, пожалуйста, оставайтесь на связи. Ваше сообщение: {message}, ваша почта: {email}',
            "noreply@somehost.local",
            [email]
        )
        return redirect('index')
    
    context = {
        'contact':contact,
        'setting' : setting,
        'backround' : backround,
        
    }
    
    return render   (request, 'website/contact-1.html', context)