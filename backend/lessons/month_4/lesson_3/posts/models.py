from django.db import models


"""
    posts = posts.objects.all() === SELECT * FROM posts
"""


class Category(models.Model):
    title = models.CharField(max_length=56)

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=56)

    def __str__(self):
        return self.title


class Post(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=True, blank=True
    )
    tag = models.ManyToManyField(Tag, null=True, blank=True)
    title = models.CharField(max_length=56)
    description = models.CharField(max_length=256)
    rate = models.IntegerField(null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True, null=True)
    update_at = models.DateTimeField(auto_now=True, null=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return f"{self.title} | desc: {self.description}"
