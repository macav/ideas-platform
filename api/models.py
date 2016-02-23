from django.contrib.auth.models import User
from django.db import models


class Idea(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=50)
    content = models.TextField()
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)