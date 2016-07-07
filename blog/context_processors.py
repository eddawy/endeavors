from blog.forms.feedback_form import FeedbackForm
from .models import Section

def sections(request):
    sections = Section.Section.objects.all
    feedback_form = FeedbackForm()
    context = {
        'sections': sections,
        'feedback_form': feedback_form,
    }

    return context
