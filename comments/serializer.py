from rest_framework import serializers

from comments.models import Comment
from users.serializers import CustomUserSerializer


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['description', 'created_at', 'user_detail']

    user_detail = serializers.SerializerMethodField()

    def get_user_detail(self, obj):
        serializer = CustomUserSerializer(obj.user, context={'request': self.context.get(('request'))})
        return serializer.data


class AddCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['description', 'post']
