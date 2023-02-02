from django.shortcuts import render
from apps.settings.models import Setting
from apps.blog.models import Blog, BackroundBlog
from apps.contact.models import Contact
# Create your views here.

def blog(request):
    contact = Contact.objects.latest('id')
    setting = Setting.objects.latest('id')
    backround = BackroundBlog.objects.latest('id')
    blog = Blog.objects.all()
    context = {
        'contact':contact,
        'setting' : setting,
        'backround' : backround,
        'blog' : blog,
        
        
    }
    
    return render(request, 'news-grid.html', context)

def blog_detail(request, id):
    contact = Contact.objects.latest('id')
    setting = Setting.objects.latest('id')
    blog = Blog.objects.get(id =id)
    backround = BackroundBlog.objects.latest('id')
    
    context = {
        'contact':contact,
        'setting' : setting,
        'blog' : blog,
        'backround' : backround,
    }
    
    return render(request, 'post-gallery.html', context)