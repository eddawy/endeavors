from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from blog.views.base import BaseView
from ..models import Subject, Topic

class SubjectView(BaseView):

    def index(self, request):
        pass

    def show(self, request, id):
        subject = Subject.Subject.objects.get(id = id)
        topics = subject.topics.all().order_by('-created_at')
        featured_topics = Topic.Topic.get_featured_topics()
        template = loader.get_template('subject.html')
        context = {
            'subject': subject,
            'topics': topics,
            'featured_topics': featured_topics,
        }
        return HttpResponse(template.render(context, request))

    def create(self, request):
        pass

    def update(self, request, id):
        pass

    def delete(self, request, id):
        pass
