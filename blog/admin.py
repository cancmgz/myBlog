from django.contrib import admin
from .models import Post
from .models import Category,Page,Setting

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Page)
admin.site.register(Setting)