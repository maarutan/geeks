from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=250)
    rate = models.FloatField(null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
