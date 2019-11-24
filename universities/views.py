from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from universities.models import University, Profession
from universities.serializers import QueryParamsSerializer, RetrieveUniversitiesSerializer


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
        ser_params = QueryParamsSerializer(data=request.data)
        ser_params.is_valid(raise_exception=True)
        first_sub, second_sub, city = (
            ser_params.validated_data.get('first_subject'),
            ser_params.validated_data.get('second_subject'),
            ser_params.validated_data.get('city'),
        )
        universities = University.objects.filter(city__name=city)
        professions = Profession.objects.filter(first_subject=first_sub, second_subject=second_sub, university__in=universities)
        ser = RetrieveUniversitiesSerializer(professions, many=True)
        return Response(ser.data, status=status.HTTP_200_OK)
