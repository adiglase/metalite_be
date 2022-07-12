from django.conf import settings
from rest_framework import serializers

from posts.models import Post


class PostSerializer(serializers.ModelSerializer):
    user_id = serializers.SerializerMethodField()
    user_image = serializers.SerializerMethodField()
    user_full_name = serializers.SerializerMethodField()
    user_username = serializers.SerializerMethodField()
    total_likes = serializers.SerializerMethodField()
    total_comments = serializers.SerializerMethodField()
    is_liked = serializers.SerializerMethodField(method_name='get_is_liked')

    class Meta:
        model = Post
        fields = ['description', 'id', 'image', 'created_at', 'total_likes', 'is_liked', 'user_id', 'user_image', 'user_full_name', 'user_username', 'total_comments']
        read_only_fields = (
            "created_by",
            "created_at"
        )

    def get_total_likes(self, obj):
        return obj.likes.count()

    def get_is_liked(self, obj):
        user = self.context.get('request').user
        return obj.likes.filter(user=user).exists()

    def get_total_comments(self, obj):
        return obj.comments.count()

    def get_user_id(self, obj):
        return obj.created_by.id

    def get_user_image(self, obj):
        return settings.HOME_URL + obj.created_by.image.url if obj.created_by.image else None

    def get_user_full_name(self, obj):
        return obj.created_by.full_name

    def get_user_username(self, obj):
        return obj.created_by.username


class PostDetailSerializer(PostSerializer):
    class Meta(PostSerializer.Meta):
        fields = PostSerializer.Meta.fields + ['comments']
