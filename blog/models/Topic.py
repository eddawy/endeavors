from django.db import models
from .Subject import Subject
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Topic(models.Model):
    title = models.CharField(max_length = 200, null = False)
    quote = models.CharField(max_length = 400)
    body = RichTextField(null = False)
    image = models.ImageField(upload_to = 'blog/images/')
    featured = models.BooleanField(default = False)
    subject = models.ForeignKey(Subject, related_name='topics')
    user = models.ForeignKey(User, related_name='topics')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    @classmethod
    def get_latest_topics(cls):
        latest_topics = cls.objects.all().order_by('-created_at')[:5]
        return latest_topics

    @classmethod
    def get_featured_topics(cls):
        featured_topics = cls.objects.filter(featured=1).order_by('-updated_at')[:4]
        return featured_topics

class TopicVisit(models.Model):
    topic = models.ForeignKey(Topic, related_name="topic_visits")
    ip = models.CharField(max_length=40)
    session_key = models.CharField(max_length=40)
    created_at = models.DateTimeField(auto_now_add=True)
