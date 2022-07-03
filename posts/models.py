from django.db import models
from users.models import User


def upload_to(instance, filename):
    return f'posts/{filename}'.format(filename=filename)


class Post(models.Model):
    created_by = models.ForeignKey(User, related_name="posts", null=True, on_delete=models.SET_NULL)
    image = models.ImageField("Image", upload_to=upload_to)
    description = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
