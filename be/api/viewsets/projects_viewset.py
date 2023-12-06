from rest_framework import viewsets, permissions
from rest_framework_simplejwt.authentication import JWTAuthentication
from api.models import Project
from api.serializers import ProjectSerializer

class ProjectViewset(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    authentication_classes = (JWTAuthentication, )
    permission_classes = (permissions.IsAuthenticated, )
