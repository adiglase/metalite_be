from djoser.serializers import UserSerializer
from rest_framework import serializers

from posts.models import Post


class PostSerializer(serializers.ModelSerializer):
    created_by = serializers.SerializerMethodField(method_name='get_created_by')
    total_likes = serializers.SerializerMethodField()
    is_liked = serializers.SerializerMethodField(method_name='get_is_liked')

    class Meta:
        model = Post
        fields = ['created_at', 'created_by', 'description', 'id', 'image', 'total_likes', 'is_liked']
        read_only_fields = (
            "created_by",
            "created_at"
        )

    def get_created_by(self, obj):
        serializer = UserSerializer(obj.created_by)
        return serializer.data

    def get_total_likes(self, obj):
        return obj.likes.count()

    def get_is_liked(self, obj):
        user = self.context.get('request').user
        return obj.likes.filter(user=user).exists()
