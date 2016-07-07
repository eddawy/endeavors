from django.contrib import admin

from .models import Section, Subject, Topic, Feedback

class SectionAdmin(admin.ModelAdmin):
    fields = ['name',]

class SubjectAdmin(admin.ModelAdmin):
    fields = ['name', 'section']

class TopicAdmin(admin.ModelAdmin):
    fields = ['title', 'quote', 'body', 'subject', 'image', 'featured']

    def save_model(self, request, obj, form, change):
        if not change:
            obj.user = request.user
        obj.save()

class FeedbackAdmin(admin.ModelAdmin):
    fields = ['name', 'email', 'message']

admin.site.register(Section.Section, SectionAdmin)
admin.site.register(Subject.Subject, SubjectAdmin)
admin.site.register(Topic.Topic, TopicAdmin)
admin.site.register(Feedback.Feedback, FeedbackAdmin)
