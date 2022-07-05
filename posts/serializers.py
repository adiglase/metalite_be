from djoser.serializers import UserSerializer
from rest_framework import serializers

from posts.models import Post


class PostSerializer(serializers.ModelSerializer):
    created_by = serializers.SerializerMethodField(method_name='get_created_by')

    class Meta:
        model = Post
        fields = ['created_at', 'created_by', 'description', 'id', 'image']
        read_only_fields = (
            "created_by",
            "created_at"
        )

    def get_created_by(self, obj):
        serializer = UserSerializer(obj.created_by)
        return serializer.data
