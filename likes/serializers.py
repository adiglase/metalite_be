from rest_framework import serializers

from likes.models import Like


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'


class AddLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['post']
