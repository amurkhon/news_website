from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models
from django.urls import reverse

# Create your models here.
class PublishedManager(models.Manager):
  def get_queryset(self) -> models.QuerySet:
    return super().get_queryset().filter(status=News.Status.Published)

class Category(models.Model):
  
  name = models.CharField(max_length=150)

  def __str__(self) -> str:
    return self.name

from django.utils.text import slugify
class News(models.Model):
  class Status(models.TextChoices):
    Draft = "DF","Draft"
    Published = "PB","Published"

  title = models.CharField(max_length=250)
  slug = models.SlugField(max_length=250,unique=True)
  body = models.TextField()
  image = models.ImageField(upload_to='news/images')
  category = models.ForeignKey(Category,on_delete=models.CASCADE)
  pulished_time = models.DateTimeField(default=timezone.now)
  created_time = models.DateTimeField(auto_now_add=True)
  updated_time = models.DateTimeField(auto_now=True)
  status = models.CharField(
                            max_length=2,
                            choices=Status.choices,
                            default=Status.Draft
                            )
  objects = models.Manager() #Default manager
  published = PublishedManager()
  class Meta:
    ordering = ["-pulished_time"]
  
  def get_absolute_url(self):
    return reverse('news_detail_page', args=[self.id])

  def __str__(self) -> str:
    return self.title

class Contact(models.Model):
  name = models.CharField(max_length=150)
  surename = models.CharField(max_length=150, default="")
  email = models.EmailField(max_length=150)
  message = models.TextField()

  def __str__(self):
    return self.email
  
class Comment(models.Model):

  news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='comments')
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')

  body = models.TextField()
  created_time = models.DateTimeField(auto_now_add=True)
  active  = models.BooleanField(default=True)

  class Meta:
    ordering = ['-created_time']
  
  def __str__(self) -> str:
    return f"Comment {self.body} by {self.user}"