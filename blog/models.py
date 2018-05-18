from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    imageUrl = models.ImageField
    category = models.ForeignKey('Category', default=0, on_delete=models.CASCADE)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    isActive = models.BooleanField(default=1)
    isDelete = models.BooleanField(default=0)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    isActive = models.BooleanField(default=1)
    isDelete = models.BooleanField(default=0)

    def publish(self):
        self.save()

    def __str__(self):
        return self.name

class Page(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    isActive = models.BooleanField(default=True)
    isDelete = models.BooleanField(default=False)

    def publish(self):
        self.save()

    def __str__(self):
        return self.title

class Setting(models.Model):
    title = models.CharField(max_length=200)
    logo = models.CharField(max_length=200)

    def publish(self):
        self.save()

    def __str__(self):
        return self.title

class Photo(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField(null=True)
    created_date = models.DateTimeField(default=timezone.now)
    camera = models.CharField(max_length=50)
    diaphragm = models.CharField(max_length=4)
    iso = models.IntegerField()
    shootTime = models.CharField(max_length=8, null=True)
    lens = models.CharField(max_length=100, null=True)
    mode = models.CharField(max_length=10, null=True)
    model = models.CharField(max_length=100, null=True)
    shootDate = models.DateTimeField(default=timezone.now,null=True)
    distance = models.CharField(max_length=10, null=True)
    category = models.ForeignKey('PhotoCategory', on_delete=models.CASCADE)
    photoUrl = models.CharField(max_length=200)

    def publish(self):
        self.save()

    def __str__(self):
        return self.title

class PhotoCategory(models.Model):
    name = models.CharField(max_length=50)
    createDate = models.DateTimeField(default=timezone.now)
    isActive = models.BooleanField(default=True)
    isDelete = models.BooleanField(default=False)

    def publish(self):
        self.save()

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)

    def publish(self):
        self.save()

    def __str__(self):
        return self.name








# Create your models here.