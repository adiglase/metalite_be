from rest_framework import serializers

from posts.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        read_only_fields = (
            "created_by",
            "created_at"
        )
        fields = '__all__'
