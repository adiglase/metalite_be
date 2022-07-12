from django.db import models

from posts.models import Post
from users.models import User


class Comment(models.Model):
    description = models.CharField(max_length=500)
    user = models.ForeignKey(User, related_name="comments", on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-id']
