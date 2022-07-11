from django.contrib.auth import get_user_model
from rest_framework import viewsets

from users.serializers import CustomUserSerializer

User = get_user_model()


class CustomUserViewSet(viewsets.ModelViewSet):
    serializer_class = CustomUserSerializer
    queryset = User.objects.filter(is_staff=False)

