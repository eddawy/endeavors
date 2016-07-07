from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader

from blog.models.Section import Section
from blog.models.Topic import Topic, TopicVisit
from blog.views.base import BaseView

class TopicView(BaseView):
    def index(self, request):
        sections = Section.objects.all
        template = loader.get_template('index.html')
        context = {
            'sections': sections,
        }
        return HttpResponse(template.render(context, request))

    def show(self, request, id):
        topic = get_object_or_404(Topic, id = id)
        if not TopicVisit.objects.filter(
                        topic=topic,
                        session_key=request.session.session_key):
            visit = TopicVisit(topic=topic,
                                ip=request.META['REMOTE_ADDR'],
                                session_key=request.session.session_key)
            visit.save()
        template = loader.get_template('topic.html')
        featured_topics = Topic.get_featured_topics()
        context = {
            'topic': topic,
            'featured_topics': featured_topics,
        }
        return HttpResponse(template.render(context, request))
