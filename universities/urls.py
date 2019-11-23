from rest_framework import routers
from django.conf.urls import url, include

from universities.views import UniversityViewSet

router = routers.DefaultRouter()
router.register('v1/univer', UniversityViewSet)

urlpatterns = []


app_name = 'universities'
urlpatterns += router.urls
