from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from blog.views.base import BaseView
from ..models import Section

class SectionView(BaseView):

    def index(self, request):
        pass

    def show(self, request, id):
        section = Section.Section.objects.get(id = id)
        subjects = section.subjects.all
        template = loader.get_template('section.html')
        context = {
            'section': section,
            'subjects': subjects,
        }
        return HttpResponse(template.render(context, request))

    def create(self, request):
        pass

    def update(self, request, id):
        pass

    def delete(self, request, id):
        pass
