from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer, UserSerializer
from rest_framework import serializers

from posts.serializers import PostSerializer


class CustomUserSerializer(UserSerializer):
    posts = serializers.SerializerMethodField()
    total_posts = serializers.SerializerMethodField()
    is_followed = serializers.SerializerMethodField()

    class Meta(UserSerializer.Meta):
        fields = '__all__'

    def get_posts(self, obj):
        post_list = obj.posts.all()
        serializer = PostSerializer(post_list, many=True, context={'request': self.context.get(('request'))})
        return serializer.data

    def get_total_posts(self, obj):
        return obj.posts.count()

    def get_is_followed(self, obj):
        user = self.context.get('request').user
        return obj.followers.filter(follower=user).exists()


class UserRegistrationSerializer(BaseUserRegistrationSerializer):
    class Meta(BaseUserRegistrationSerializer.Meta):
        fields = ('url', 'id', 'image', 'email', 'name', 'last_name', 'account_address', 'password')
