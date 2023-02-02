from django.shortcuts import render,redirect
from apps.settings.models import Setting,Slide, Partners, Number
from apps.contact.models import Contact
from apps.about.models import About
from apps.rooms.models import Room
from apps.review.models import Review
from apps.blog.models import Blog, BackroundBlog


# from apps.rooms.models import Room

# Create your views here.
def index(request):
    room = Room.objects.all()
    blog = Blog.objects.all()
    
    setting = Setting.objects.latest('id')
    contact = Contact.objects.latest('id')
    slide = Slide.objects.all()
    about = About.objects.latest('id')
    partners = Partners.objects.all()
    num = Number.objects.latest('id')
    review = Review.objects.all()
    
    if request.method == "POST":
        name_user = request.POST.get('name_user')
        image_user = request.FILES.get('image_user')
        email_user = request.POST.get('email_user')
        message_user = request.POST.get('message_user')
        product = Review.objects.create( name_user = name_user, image_user = image_user,email_user = email_user, message_user = message_user)
        return redirect('index')
    
    context = {
        'setting' : setting,
        'contact' : contact,
        'slide': slide,
        'about' : about,
        'room' : room,
        'partners' : partners,
        'num' : num,
        'review' : review,
        'blog' : blog,
        
        
        
    }
    return render(request, 'index.html', context)