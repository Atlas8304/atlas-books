from django.db import models
from django.contrib.auth.models import User

PUBLISHED_STATES = ((0, "Draft"), (1, "Publish"))


class BlogPost(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    creation_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    content = models.TextField()
    published_state = models.IntegerField(choices=PUBLISHED_STATES, default=0)

    class meta:
        ordering = ["-creation_date"]

    def __str__(self) -> str:
        return self.title
