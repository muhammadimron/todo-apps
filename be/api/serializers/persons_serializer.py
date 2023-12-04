from rest_framework import serializers
from api.models import Person

class PersonSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    role = serializers.CharField()
    email = serializers.CharField()
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Person
        fields = [
            'id',
            'first_name',
            'last_name',
            'role',
            'email',
            'password'
        ]