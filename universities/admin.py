from django.contrib import admin
from universities.models import (
    City,
    University,
    Profession,
)

my_models = [
    City,
    University,
    Profession,
]


admin.site.register(my_models)
