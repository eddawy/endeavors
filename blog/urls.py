from django.conf.urls import url

from blog.views.feedback import FeedbackView
from blog.views.section import SectionView
from blog.views.subject import SubjectView
from blog.views.topic import TopicView
from .views import index

urlpatterns = [
    url(r'^$', index.index),
    url(r'^topics/$', TopicView().handle_request_with_params),
    url(r'^topics/(?P<id>[0-9]+)/$', TopicView().handle_request_with_params),

    url(r'^sections/(?P<id>[0-9]+)/$', SectionView().handle_request_with_params),

    url(r'^subjects/(?P<id>[0-9]+)/$', SubjectView().handle_request_with_params),

    url(r'^feedbacks/$', FeedbackView().handle_request_without_params),
    url(r'^elements/$', index.elements),
]
