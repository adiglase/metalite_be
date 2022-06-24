from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser

from posts.models import Post
from posts.serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    parser_classes = [MultiPartParser, FormParser]
