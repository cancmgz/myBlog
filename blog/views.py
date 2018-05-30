from django.utils import timezone
from .models import Post,Category,Page,PhotoCategory,Photo,Setting,Tag,PostComment
from django.shortcuts import render, get_object_or_404
from blog import forms
from django.shortcuts import redirect

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def index(request, pageNumber=0):
    if not pageNumber:
        pageNumber=0
    first = int(pageNumber)*5
    last = int(first)+5
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[first:last]
    categorys = Category.objects.filter(isActive=1).order_by('created_date')
    pages = Page.objects.filter(isActive=1)
    settings = Setting.objects.filter()
    return render(request, 'blog/index.html', {'posts': posts, 'categorys': categorys, 'pages': pages, 'settings': settings})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    pages = Page.objects.filter(isActive=1)
    settings = Setting.objects.filter()
    comments = PostComment.objects.filter(post=pk)
    return render(request, 'blog/post_detail.html', {'post': post, 'pages': pages, 'settings': settings, 'comments': comments})

def pageDetail(request, pk):
    page = get_object_or_404(Page, pk=pk)
    pages = Page.objects.filter(isActive=1)
    settings = Setting.objects.filter()
    return render(request, 'blog/page.html', {'page': page, 'pages': pages, 'settings': settings})

def photo(request):
    photos = Photo.objects.filter()
    categorys = PhotoCategory.objects.filter(isActive=1).order_by('name')
    settings = Setting.objects.filter()
    pages = Page.objects.filter(isActive=1)
    return render(request, 'blog/photo.html', {'photos': photos, 'categorys': categorys, 'pages': pages, 'settings': settings})

def PostComments(request):
    if request.method == 'POST':
        form = forms
        fullname = request.POST['fullname']
        createdDate = timezone.now()
        email = request.POST['email']
        post = request.POST['post']
        comment = request.POST['comment']
        userPostComment = PostComment()
        userPostComment.fullname = fullname
        userPostComment.createdDate = createdDate
        userPostComment.isActive = 1
        userPostComment.isDelete = 0
        userPostComment.email = email
        userPostComment.post =get_object_or_404(Post, pk=post)
        PostComment.comment = comment
        userPostComment.save()

        return redirect('post_detail', pk=4)

