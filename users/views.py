from multiprocessing import context
from django.contrib.auth import get_user_model
from django.db.models import Q
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
            id__exact=request.user.id).order_by('?')[:5]

        serializer = CustomUserSerializer(users, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['post'])
    def search(self, request):
        user_identity = request.data.get('userIdentity')
        filtered_user = User.objects.filter(Q(is_staff=False) & (Q(full_name__icontains=user_identity) | Q(username__icontains=user_identity)))[:5]
        serializer = CustomUserSerializer(filtered_user, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
