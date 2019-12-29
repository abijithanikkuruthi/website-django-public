from django.db import models
from django.contrib.auth.models import User

class Tag(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField()
    img_thumbnail = models.CharField(max_length=200, default="images/blog-1.jpg")
    tags = models.ManyToManyField('Tag', related_name='posts')
    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

class Message(models.Model):
    name = models.CharField(max_length=60)
    email = models.CharField(max_length=60)
    subject = models.CharField(max_length=200)
    ip = models.CharField(max_length=200)
    message = models.TextField()
    send_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-send_on']

    def __str__(self):
        return self.subject