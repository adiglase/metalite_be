from django.db.models import Q
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response

from comments.models import Comment
from comments.serializer import CommentSerializer
from posts.models import Post
from posts.serializers import PostSerializer, PostDetailSerializer


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    parser_classes = [MultiPartParser, FormParser]

    def get_queryset(self):
        current_user = self.request.user
        current_user_following_ids = current_user.following.values_list('following', flat=True)
        posts = Post.objects.filter(Q(created_by__in=current_user_following_ids) | Q(created_by=current_user))
        return posts

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return PostDetailSerializer
        return self.serializer_class

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    @action(detail=True, methods=['get'])
    def comments(self, request, pk=None):
        comments = Comment.objects.filter(post=pk)
        serializer = CommentSerializer(comments, many=True, context={'request': self.request})
        return Response(serializer.data, status=status.HTTP_200_OK)
