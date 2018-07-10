from django.contrib import admin

from .models import BookmarkBase, Bookmark

admin.site.register(BookmarkBase)
admin.site.register(Bookmark)
