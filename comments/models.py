from django.db import models
from django.db import models
from django.utils import timezone


class Comment(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    url = models.URLField(blank=True)
    text = models.TextField()
    created_time = models.DateTimeField(default=timezone.now)
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'comments'
        verbose_name_plural = verbose_name
        ordering = ['-created_time']

    def __str__(self):
        return f'{self.name}:{self.text[:15]}'

