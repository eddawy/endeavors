from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from ..models import Topic
def index(request):
    latest_topics = Topic.Topic.get_latest_topics()
    featured_topics = Topic.Topic.get_featured_topics()
    context = {
        'latest_topics': latest_topics,
        'featured_topics': featured_topics,
    }
    template = loader.get_template('index.html')
    return HttpResponse(template.render(context, request))

def elements(request):
    return render(request, 'elements.html')

def generic(request):
    return render(request, 'generic.html')
