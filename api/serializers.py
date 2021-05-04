from rest_framework import serializers
from posts.models import Post, Comment


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')  # TODO Check if this way is OK

    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ['pub_date', 'author']


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')  # TODO Check if this way is OK

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ['author', 'created', 'post']
