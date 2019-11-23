from django.contrib import admin
from universities.models import (
    City,
    University,
    Profession,
    Subjects,
)

my_models = [
    City,
    University,
    Profession,
    Subjects,
]


admin.site.register(my_models)
