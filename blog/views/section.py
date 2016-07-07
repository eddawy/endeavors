from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from blog.views.base import BaseView
from ..models import Section

class SectionView(BaseView):
    def show(self, request, id):
        section = Section.Section.objects.get(id = id)
        subjects = section.subjects.all
        template = loader.get_template('section.html')
        context = {
            'section': section,
            'subjects': subjects,
        }
        return HttpResponse(template.render(context, request))
