from django.db import models


"""
    posts = posts.objects.all() === SELECT * FROM posts
"""


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=56)
    description = models.CharField(max_length=256)
    rate = models.IntegerField(null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True, null=True)
    update_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f"{ self.title } | desc: { self.description }"
