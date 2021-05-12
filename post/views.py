from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from post.serializers import PostSerializer, CommentSerializer
from post.models import Post, Comment
from django.db.models import F 
from post.permissions import IsPostOwnerOrReadOnly, IsCommentOwnerOrReadOnly

class PostView(ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    lookup_field = 'pk'
    permission_classes = (IsPostOwnerOrReadOnly, )


class CommentView(ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    lookup_field = 'pk'
    permission_classes = (IsCommentOwnerOrReadOnly, )
