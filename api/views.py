from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import SAFE_METHODS, BasePermission, IsAuthenticated

from posts.models import Post, Comment
from .serializers import PostSerializer, CommentSerializer


class OnlyAuthorCanEditPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return bool(request.user == obj.author)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticated, OnlyAuthorCanEditPermission)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticated, OnlyAuthorCanEditPermission,)

    def get_queryset(self, *args, **kwargs):
        post = get_object_or_404(Post, pk=self.kwargs.get('post_pk'))
        if 'pk' not in self.kwargs:
            return self.queryset.filter(post=post)
        return self.queryset.filter(post=post, pk=self.kwargs.get('pk'))

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, post_id=self.kwargs['post_pk'])
