from rest_framework import serializers
from posts.models import Post, Comment


class CommentSerializer(serializers.ModelSerializer):
    # Fetching 'author.username' instead of standard 'author.id'.
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ['author', 'created', 'post']


class PostSerializer(serializers.ModelSerializer):
    # Fetching 'author.username' instead of standard 'author.id'.
    author = serializers.ReadOnlyField(source='author.username')
    # Fetching additional 'comments' field
    comments = CommentSerializer(many=True, required=False)

    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ['author', 'pub_date', 'comments']
