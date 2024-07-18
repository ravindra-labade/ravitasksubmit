from django.db import models


class Post(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

