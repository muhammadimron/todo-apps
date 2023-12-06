from django.contrib.auth.hashers import make_password
from rest_framework import viewsets, status, permissions, exceptions
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from api.models import Person
from api.serializers import PersonSerializer

class RegisterViewset(viewsets.GenericViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    def create(self, request, *args, **kwargs):
        mutable_data = request.data.copy()
        mutable_data["password"] = make_password(mutable_data["password"])

        serializer = self.get_serializer(data=mutable_data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()

        return Response(self.get_serializer(instance).data, status=status.HTTP_201_CREATED)

class PersonViewset(viewsets.ReadOnlyModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    authentication_classes = (JWTAuthentication, )
    permission_classes = (permissions.IsAuthenticated, )

    def list(self, request, *args, **kwargs):
        person = request.user
        serializer = self.get_serializer(person)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        raise exceptions.MethodNotAllowed("GET")

class PersonAllViewset(viewsets.ReadOnlyModelViewSet):
    queryset = Person.objects.exclude(id=1)
    serializer_class = PersonSerializer
    authentication_classes = (JWTAuthentication, )
    permission_classes = (permissions.IsAuthenticated, )

    def retrieve(self, request, *args, **kwargs):
        raise exceptions.MethodNotAllowed("GET")