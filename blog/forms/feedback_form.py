from django import forms
from django.forms import ModelForm

from blog.models.Feedback import Feedback


class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'email', 'subject', 'message']
