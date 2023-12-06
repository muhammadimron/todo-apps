from rest_framework import serializers
from api.models import Project

class PersonDetailSerializer(serializers.Serializer):
    first_name = serializers.CharField(read_only=True)
    last_name = serializers.CharField(read_only=True)

class ProjectSerializer(serializers.ModelSerializer):
    person_detail = PersonDetailSerializer(source="person", read_only=True)
    class Meta:
        model = Project
        fields = [
            'id',
            'title',
            'person',
            'person_detail',
            'due',
            'status',
            'content'
        ]
