from audioop import reverse
from time import timezone
from tkinter import CASCADE
from turtle import title
import django
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date, datetime


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='blog_posts')

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        #return reverse('mangxahoi:chitiet', args=(str(self.id)))
        return reverse('mangxahoi:mangxahoi')

    def total_likes(self):
        return self.likes.count()
        #co the dung tuong tu{{post.likes.count}}


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    cmt_date = models.DateTimeField(auto_now_add=True)
    cmt_likes = models.ManyToManyField(User, related_name='blog_cmts')

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)
