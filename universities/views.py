from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from universities.models import University


class UniversityViewSet(viewsets.GenericViewSet):
    permission_classes = (AllowAny,)
    queryset = University.objects.all()

    @action(
        methods=['get'],
        detail=False,
        url_path='universities',
        url_name='universities',
    )
    def get_universities(self, request):
        data = {c.name: c.city.name for c in University.objects.all()}
        return Response(data, status=status.HTTP_200_OK)
