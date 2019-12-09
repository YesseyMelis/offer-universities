from django.contrib import admin
from universities.models import (
    City,
    University,
    Profession,
    Speciality,
)

my_models = [
    City,
    University,
    Profession,
    Speciality,
]


admin.site.register(my_models)
