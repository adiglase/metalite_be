from django.db import models

from posts.models import Post
from users.models import User


class Like(models.Model):
    user = models.ForeignKey(User, related_name="liked", on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name="likes", on_delete=models.CASCADE)
    liked_at = models.DateTimeField(auto_now_add=True)
