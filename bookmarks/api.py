from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

from .models import BookmarkBase, Bookmark


class BookmarkBaseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BookmarkBase
        fields = ('title', 'url', 'description')


class BookmarkBaseViewSet(viewsets.ModelViewSet):
    serializer_class = BookmarkBaseSerializer
    queryset = BookmarkBase.objects.all()


class BookmarkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bookmark
        fields = ('title', 'url', 'description')
        # TODO: function create

    def create(self, validated_data):
        user = self.context['request'].user
        bookmark = Bookmark.objects.create(
            user=user, **validated_data
        )
        return bookmark


class BookmarkViewSet(viewsets.ModelViewSet):
    serializer_class = BookmarkSerializer
    queryset = Bookmark.objects.all()

    def get_queryset(self):
        user = self.request.user
        if user.is_anonymous:
            return Bookmark.objects.none()

        else:
            return Bookmark.objects.filter(user=user)
