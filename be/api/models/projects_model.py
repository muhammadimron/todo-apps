from django.db import models
from api.models import Person

class Project(models.Model):
    title = models.CharField(max_length=255)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    due = models.DateTimeField()
    status = models.CharField(max_length=255)
    content = models.TextField(max_length=10000)