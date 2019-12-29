from django.shortcuts import render, get_object_or_404
from .models import Blog, Message, Tag
from .forms import MessageForm
from abijith.settings import BLOGS_PER_PAGE
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def index(request):
    return render(request, 'index.html', {})

def resume(request):
    return render(request, 'resume.html', {})

def services(request):
    return render(request, 'services.html', {})

def portfolio(request):
    return render(request, 'portfolio.html', {})

def get_page_object(page, num_pages):
    p_obj = {}
    if(page != 1):
        p_obj["prev"] = page - 1
    if(page != num_pages):
        p_obj["next"] = page + 1
    if num_pages == 1:
        p_list = []
    elif(num_pages < 5):
        p_list = list(range(1, num_pages + 1))
    elif(page < 3):
        p_list = list(range(1, 6))
    elif(num_pages < page + 2):
        p_list = list(range(num_pages-4, num_pages + 1))
    else:
        p_list = list(range(page-2,page+3))
    p_obj["list"] = p_list
    p_obj["page"] = page
    return p_obj


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
    context = {
        "blog": blog,
        "tags": tags
    }
    return render(request, 'blog-view.html', context)

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def contact(request):
    form = MessageForm()
    message_saved = False
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = Message(
                name=form.cleaned_data["name"],
                email=form.cleaned_data["email"], 
                subject=form.cleaned_data["subject"],
                message=form.cleaned_data["message"],
                ip=get_client_ip(request)
            )
            message.save()
            message_saved = True
    
    context = {
        "form" : form,
        "message_saved" : message_saved
    }
    return render(request, 'contact.html', context)