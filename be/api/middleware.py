from api.models import Person
from rest_framework.authtoken.models import Token

class TodoappsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path == '/api/person/':
            print("")

        response = self.get_response(request)

        return response