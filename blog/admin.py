from django.contrib import admin
from .models import Post
from .models import Category, Page, Setting, Photo, PhotoCategory, Tag, PostComment

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Page)
admin.site.register(Setting)
admin.site.register(Photo)
admin.site.register(PhotoCategory)
admin.site.register(Tag)
admin.site.register(PostComment)
