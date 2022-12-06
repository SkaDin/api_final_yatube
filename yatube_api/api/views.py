from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import (
    ModelViewSet,
    ReadOnlyModelViewSet,
    GenericViewSet
)
from rest_framework.filters import SearchFilter
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from posts.models import Group, Post
from django.shortcuts import get_object_or_404
from api.serializers import (
    PostSerializer,
    GroupSerializer,
    CommentSerializer,
    FollowSerializer,
)
from api.permissions import IsOwnerOrReadOnly
from rest_framework.pagination import LimitOffsetPagination


class GroupViewSet(ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsOwnerOrReadOnly,)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (IsOwnerOrReadOnly,)

    def get_queryset(self):
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        return post.comments

    def perform_create(self, serializer):
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        serializer.save(author=self.request.user, post=post)


class FollowViewSet(
    ListModelMixin,
    CreateModelMixin,
    GenericViewSet,
):
    serializer_class = FollowSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (SearchFilter,)
    search_fields = ('=following__username',)

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(user=self.request.user)

    def get_queryset(self):
        return self.request.user.follower
