from django.shortcuts import render, get_object_or_404
from .models import Blog, Message, Tag, Comment
from .forms import MessageForm, CommentForm
from .utils import get_page_object, get_client_ip, send_email_to_admin
from abijith.settings import BLOGS_PER_PAGE
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
import datetime

def index(request):
    return render(request, 'index.html', {})

def resume(request):
    return render(request, 'resume.html', {})

def services(request):
    return render(request, 'services.html', {})

def portfolio(request):
    return render(request, 'portfolio.html', {})

def blog_list(request):
    return blog_list_n(request, 1)
    
def blog_list_n(request, pk):
    blogs = Blog.objects.all().order_by('-created_on')
    paginator = Paginator(blogs, BLOGS_PER_PAGE)
    try:
        blogs_list = paginator.page(pk)
    except EmptyPage:
        blogs_list = paginator.page(paginator.num_pages)

    page_object = get_page_object(pk, paginator.num_pages)
    
    context = {
        "blogs": blogs_list,
        "pages": page_object
    }
    return render(request, 'blog.html', context)

def blog_view(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    tags = [tag for tag in Tag.objects.all() if tag in blog.tags.all()]
    comments = blog.comments.filter(active=True)

    new_comment = False
    # Comment posted
    if request.method == 'POST':
        form = CommentForm(data=request.POST)
        if form.is_valid():
            c_obj = {
                "name" : form.cleaned_data["name"],
                "email" : form.cleaned_data["email"], 
                "comment" : form.cleaned_data["message"],
                "ip" : get_client_ip(request),
                "host" : request.get_host()
            }
            comment = Comment(
                name=c_obj["name"],
                email=c_obj["email"], 
                message=c_obj["comment"],
                ip=c_obj["ip"],
                blog=blog,
                created_on=datetime.datetime.now()
            )
            comment.save()
            send_email_to_admin(c_obj)
            new_comment = True
    else:
        form = CommentForm()
    context = {
        "blog": blog,
        "tags": tags,
        "comments": comments,
        "form": form,
        "comment_submitted": new_comment
    }
    return render(request, 'blog-view.html', context)

def contact(request):
    form = MessageForm()
    message_saved = False
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            m_obj = {
                "name" : form.cleaned_data["name"],
                "email" : form.cleaned_data["email"], 
                "subject" : form.cleaned_data["subject"],
                "message" : form.cleaned_data["message"],
                "ip" : get_client_ip(request),
                "host" : request.get_host()
            }
            message = Message(
                name=m_obj["name"],
                email=m_obj["email"], 
                subject=m_obj["subject"],
                message=m_obj["message"],
                ip=m_obj["ip"]
            )
            message.save()
            send_email_to_admin(m_obj)
            message_saved = True
    
    context = {
        "form" : form,
        "message_saved" : message_saved
    }
    return render(request, 'contact.html', context)