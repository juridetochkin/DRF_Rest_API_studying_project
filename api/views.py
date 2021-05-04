from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.exceptions import PermissionDenied

from posts.models import Post, Comment
from .serializers import PostSerializer, CommentSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        if not serializer.instance.author == self.request.user:
            raise PermissionDenied()
        serializer.save()

    def perform_destroy(self, instance):
        if not instance.author == self.request.user:
            raise PermissionDenied()
        instance.delete()


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self, *args, **kwargs):
        post = get_object_or_404(Post, pk=self.kwargs.get('post_pk'))
        if 'pk' not in self.kwargs:
            return self.queryset.filter(post=post)
        return self.queryset.filter(post=post, pk=self.kwargs.get('pk'))

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, post_id=self.kwargs['post_pk'])

    def perform_update(self, serializer):
        if not serializer.instance.author == self.request.user:
            raise PermissionDenied
        serializer.save()

    def perform_destroy(self, instance):
        if not instance.author == self.request.user:
            raise PermissionDenied
        instance.delete()

