from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):  # pyright: ignore
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):  # pyright: ignore
        return self.title


class Post(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=True, blank=True
    )
    tags = models.ManyToManyField(Tag, null=True, blank=True)
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=250)
    rate = models.FloatField(null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to="media/", null=True, blank=True)

    def __str__(self):  # pyright: ignore
        return self.title
