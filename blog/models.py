from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=30)
    body = models.TextField()

    created_time = models.DateTimeField(default=timezone.now)
    modified_time = models.DateTimeField()

    # abstracts
    excerpt = models.CharField(max_length=200, blank=True)
    # category <=> post
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # tag <=> post
    tags = models.ManyToManyField(Tag, blank=True)
    # author <= default
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # Reuse the save method to update the created_time field each time
    # def save(self, *args, **kwargs):
    #     self.modified_time = timezone.now()
    #     super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk':self.pk})