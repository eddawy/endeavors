from django.http import HttpResponseRedirect

from blog.forms.feedback_form import FeedbackForm
from blog.views.base import BaseView

class FeedbackView(BaseView):
    def create(self, request):
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    def index(self, request):
        pass

    def show(self, request, id):
        pass

    def update(self, request, id):
        pass

    def delete(self, request, id):
        pass
