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


class BookmarkViewSet(viewsets.ModelViewSet):
    serializer_class = BookmarkSerializer
    queryset = Bookmark.objects.all()
