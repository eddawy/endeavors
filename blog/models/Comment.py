from django.db import models
from .Topic import Topic
from django.contrib.auth.models import User

class Comment(models.Model):
    title = models.CharField(max_length = 200, null = False)
    body = models.TextField(null = False)
    topic = models.ForeignKey(Topic, related_name='comments', null = False)
    user = models.ForeignKey(User, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
