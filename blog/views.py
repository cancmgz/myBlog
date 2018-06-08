from django.utils import timezone
from .models import Post, Category, Page, PhotoCategory, Photo, Setting, PostComment
from django.shortcuts import render, get_object_or_404, redirect
from .forms import PostCommentForm
from django.db.models import Count
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django import template
from django.template.loader import get_template

register = template.Library()

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

@register.inclusion_tag('blog/head.html', takes_context=True)
def header(request):
    pages = Page.objects.filter(isActive=1)
    settings = get_object_or_404(Setting, pk=1)
    print(pages)
    return {'pages': pages, 'settings': settings}

def index(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    page = request.GET.get('page', 1)
    paginator = Paginator(posts, 5)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    categorys = Category.objects.filter(isActive=1).order_by('created_date')
    populerPost = PostComment.objects.filter(isActive=1, isDelete=0).values('post', 'post__title').annotate(adet=Count('post')).order_by('-adet')[:5]
    lastPostComment = PostComment.objects.filter(isActive=1, isDelete=0).order_by('-createdDate')[:5]

    return render(request, 'blog/index.html',
                  {'posts': posts, 'categorys': categorys, 'populerPost': populerPost, 'lastPostComment': lastPostComment})


def categoryDetail(request, pk):
    posts = Post.objects.filter(published_date__lte=timezone.now(), category=pk).order_by('-published_date')
    page = request.GET.get('page', 1)
    paginator = Paginator(posts, 5)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    categorys = Category.objects.filter(isActive=1).order_by('created_date')
    pages = Page.objects.filter(isActive=1)
    settings = get_object_or_404(Setting, pk=1)
    populerPost = PostComment.objects.filter(isActive=1, isDelete=0).values('post', 'post__title').annotate(adet=Count('post')).order_by(
        '-adet')[:5]
    lastPostComment = PostComment.objects.filter(isActive=1, isDelete=0).order_by('-createdDate')[:5]
    categoryDetails = get_object_or_404(Category, pk=pk)

    return render(request, 'blog/category.html',
                  {'posts': posts, 'categorys': categorys, 'pages': pages, 'settings': settings, 'populerPost': populerPost, 'lastPostComment': lastPostComment, 'categoryDetails': categoryDetails})


def post_detail(request, pk):
    form = PostCommentForm()
    post = get_object_or_404(Post, pk=pk)
    pages = Page.objects.filter(isActive=1)
    settings = get_object_or_404(Setting, pk=1)
    comments = PostComment.objects.filter(post=pk)
    populerPost = PostComment.objects.filter(isActive=1, isDelete=0).values('post', 'post__title').annotate(adet=Count('post')).order_by(
        '-adet')[:5]
    lastPostComment = PostComment.objects.filter(isActive=1, isDelete=0).order_by('-createdDate')[:5]
    categorys = Category.objects.filter(isActive=1, isDelete=0).order_by('created_date')

    return render(request, 'blog/post_detail.html',
                  {'post': post, 'pages': pages, 'settings': settings, 'comments': comments, 'form': form, 'populerPost': populerPost, 'lastPostComment': lastPostComment, 'categorys': categorys})


def pageDetail(request, pk):
    page = get_object_or_404(Page, pk=pk)
    pages = Page.objects.filter(isActive=1)
    settings = get_object_or_404(Setting, pk=1)
    return render(request, 'blog/page.html', {'page': page, 'pages': pages, 'settings': settings})


def photo(request):
    photos = Photo.objects.filter(isActive=1, isDelete=0)
    categorys = PhotoCategory.objects.filter(isActive=1, isDelete=0).order_by('name')
    settings = get_object_or_404(Setting, pk=1)
    pages = Page.objects.filter(isActive=1)
    return render(request, 'blog/photo.html',
                  {'photos': photos, 'categorys': categorys, 'pages': pages, 'settings': settings})


def PostComments(request, pk):
    if request.method == "POST":
        form = PostCommentForm(request.POST)
    if form.is_valid():
        PostComments = form.save(commit=False)
        PostComments.isActive = 1
        PostComments.isDelete = 0
        PostComments.createdDate = timezone.now()
        PostComments.post_id = pk
        PostComments.save()
        return redirect('post_detail', pk=pk)


def Search(request):
    searchField = request.GET.get('q')
    posts = Post.objects.filter(isActive=1, isDelete=0, title__contains=searchField)
    page = request.GET.get('page', 1)
    paginator = Paginator(posts, 5)
    settings = get_object_or_404(Setting, pk=1)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    categorys = Category.objects.filter(isActive=1, isDelete=0)
    pages = Page.objects.filter(isDelete=0, isActive=1)
    populerPost = PostComment.objects.filter(isActive=1, isDelete=0).values('post','post__title').annotate(adet=Count('post')).order_by('-adet')[:5]
    lastPostComment = PostComment.objects.filter(isActive=1, isDelete=0).order_by('-createdDate')[:5]
    return render(request, 'blog/search.html',
                      {'posts': posts, 'categorys': categorys, 'pages': pages, 'settings': settings, 'populerPost': populerPost, 'lastPostComment': lastPostComment})
