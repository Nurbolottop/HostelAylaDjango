from django.shortcuts import render,redirect
from apps.settings.models import Setting
from apps.blog.models import Blog, BackroundBlog,Comment
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
    
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        comment = Comment.objects.create(name = name,email = email, message = message, post = blog )
        
        return redirect('blog_detail', blog.id)
    
    context = {
        'contact':contact,
        'setting' : setting,
        'blog' : blog,
        'backround' : backround,
    }
    
    return render(request, 'post-gallery.html', context)