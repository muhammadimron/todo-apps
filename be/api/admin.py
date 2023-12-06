from django.contrib import admin
from api.models import Person, Project

# Register your models here.
class PersonAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "first_name",
        "last_name",
        "email"
    )

admin.site.register(Person, PersonAdmin)
admin.site.register(Project)