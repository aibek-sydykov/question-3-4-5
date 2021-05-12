from rest_framework import serializers
from post.models import Post, Comment
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username')


class CommentSerializer(serializers.ModelSerializer):
    comment_author = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ('content', 'creation_date', 'comment_author')


class PostSerializer(serializers.ModelSerializer):
    post_author = UserSerializer(read_only=True, many=False)
    post_comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ('title', 'body', 'creation_date', 'post_comments', 'post_author')