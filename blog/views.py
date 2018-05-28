from django.utils import timezone
from .models import Post,Category,Page,PhotoCategory,Photo,Setting,Tag
from django.shortcuts import render, get_object_or_404

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def index(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    categorys = Category.objects.filter(isActive=1).order_by('created_date')
    pages = Page.objects.filter(isActive=1)
    settings = Setting.objects.filter()
    return render(request, 'blog/index.html', {'posts': posts, 'categorys': categorys, 'pages': pages, 'settings': settings})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def pageDetail(request, pk):
    page = get_object_or_404(Page, pk=pk)
    return render(request, 'blog/page.html', {'page': page})
