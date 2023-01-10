from django.db import models

# Create your models here.
class Post(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    img_url = models.CharField(max_length=3083)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)