from django.shortcuts import render
from rest_framework import viewsets

from comments.models import Comment
from comments.serializer import CommentSerializer, AddCommentSerializer


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer(context={'test': 'hahahw'})
    queryset = Comment.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return AddCommentSerializer
        return self.serializer_class

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
