from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from likes.models import Like
from likes.serializers import LikeSerializer, AddLikeSerializer
from posts.models import Post
from posts.serializers import PostSerializer


class LikeViewSet(viewsets.ModelViewSet):
    serializer_class = LikeSerializer
    queryset = Like.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return AddLikeSerializer
        return LikeSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        post_id = serializer.validated_data.get('post')
        return Response(PostSerializer(post_id, context={'request': request}).data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        post_id = serializer.validated_data.get('post')
        liked = Like.objects.filter(post=post_id, user=self.request.user)

        if liked:
            liked.delete()
            return Response(PostSerializer(post_id, context={'request': self.request}).data, status=status.HTTP_204_NO_CONTENT)

        serializer.save(user=self.request.user)
