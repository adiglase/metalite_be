from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer, UserSerializer
from rest_framework import serializers

from posts.serializers import PostSerializer


class CustomUserSerializer(UserSerializer):
    posts = serializers.SerializerMethodField()
    total_posts = serializers.SerializerMethodField()
    total_followers = serializers.SerializerMethodField()
    total_following = serializers.SerializerMethodField()
    is_followed = serializers.SerializerMethodField()
    is_current_user = serializers.SerializerMethodField()

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

    def get_is_current_user(self, obj):
        request = self.context.get('request')

        return obj.id == request.user.id

    def get_total_followers(self, obj):
        return obj.followers.count()

    def get_total_following(self, obj):
        return obj.following.count()


class UserRegistrationSerializer(BaseUserRegistrationSerializer):
    class Meta(BaseUserRegistrationSerializer.Meta):
        fields = ('url', 'id', 'image', 'email', 'name', 'last_name', 'account_address', 'password')
