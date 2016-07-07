from abc import ABCMeta, abstractmethod

from django.views.generic import TemplateView


class BaseView(TemplateView):
    __metaclass__ = ABCMeta

    def create_session(self, request):
        if not request.session.exists(request.session.session_key):
            request.session.create()

    def handle_request_without_params(self, request):
        self.create_session(request)
        if request.method == 'GET':
            return self.index(request)
        elif request.method == 'POST':
            return self.handle_create(request)

    def handle_request_with_params(self, request, id):
        self.create_session(request)
        if request.method == 'GET':
            return self.show(request, id)
        elif request.method == 'PUT':
            return self.handle_update(request, id)
        elif request.method == 'DELETE':
            return self.handle_delete(request, id)

    def handle_create(self, request):
        self.create_session(request)
        return self.create(request)

    def handle_update(self, request, id):
        self.create_session(request)
        return self.update(request, id)

    def handle_delete(self, request, id):
        self.create_session(request)
        return self.delete(request, id)

    @abstractmethod
    def index(self, request):
        raise NotImplementedError()

    @abstractmethod
    def show(self, request, id):
        raise NotImplementedError()

    @abstractmethod
    def create(self, request):
        raise NotImplementedError()

    @abstractmethod
    def update(self, request, id):
        raise NotImplementedError()

    @abstractmethod
    def delete(self, request, id):
        raise NotImplementedError()