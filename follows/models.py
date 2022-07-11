from django.db import models

from users.models import User


class Follow(models.Model):
    follower = models.ForeignKey(User, related_name="following", on_delete=models.CASCADE)
    following = models.ForeignKey(User, related_name="followers", on_delete=models.CASCADE)
    followed_at = models.DateTimeField(auto_now_add=True)
