from multiprocessing import context
from django.contrib.auth import get_user_model
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from users.serializers import CustomUserSerializer

User = get_user_model()


class CustomUserViewSet(viewsets.ModelViewSet):
    serializer_class = CustomUserSerializer
    queryset = User.objects.filter(is_staff=False)

    @action(detail=False, methods=['get'])
    def people_user_may_know(self, request, pk=None):
        current_user = request.user
        current_user_following_ids = current_user.following.values_list('following', flat=True)
        users = User.objects.exclude(
            id__in=current_user_following_ids).exclude(
            is_staff__exact=True).exclude(
            id__exact=12).order_by('?')[:5]

        serializer = CustomUserSerializer(users, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
