from django.contrib import admin
from universities.models import (
    City,
    University,
    Profession,
    Speciality,
    Subject
)

my_models = [
    City,
    University,
    Profession,
    Speciality,
    Subject
]


admin.site.register(my_models)
