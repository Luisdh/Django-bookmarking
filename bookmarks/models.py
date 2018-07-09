from django.db import models

from django.contrib.auth.models import User

class BookmarkBase(models.Model):
  title = models.CharField(max_length=100, blank=True)
  created_on = models.DateTimeField(auto_now_add=True)
  url = models.URLField(blank=True)
  description = models.TextField(blank=True)

class Bookmark(BookmarkBase):
  user = models.ForeignKey(User, on_delete=models.CASCADE)

