from rest_framework import viewsets, status
from rest_framework.response import Response

from follows.models import Follow
from follows.serializers import FollowSerializer, AddFollowSerializer
from users.serializers import CustomUserSerializer


class FollowViewSet(viewsets.ModelViewSet):
    serializer_class = FollowSerializer
    queryset = Follow.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return AddFollowSerializer
        return self.serializer_class

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        following_id = serializer.validated_data.get('following')
        return Response(CustomUserSerializer(following_id, context={'request': request}).data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        following_id = serializer.validated_data.get('following')
        followed = Follow.objects.filter(follower=self.request.user, following=following_id)

        if followed:
            followed.delete()
            return Response(CustomUserSerializer(following_id, context={'request': self.request}).data, status=status.HTTP_204_NO_CONTENT)

        serializer.save(follower=self.request.user)
