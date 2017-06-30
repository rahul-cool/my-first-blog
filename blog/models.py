from django.db import models
from django.utils import timezone

class Post(models.Model):

    author = models.ForeignKey('auth.user')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_Date = models.DateTimeField(default=timezone.now())
    published_Date = models.DateTimeField(blank=True, null=True)

    def published(self):
        self.published_Date = timezone.now()

    def __str__(self):
        return self.title

# Create your models here.
