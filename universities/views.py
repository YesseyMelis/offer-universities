from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from universities.models import University, Profession, City
from universities.serializers import RequestDataSerializer, RetrieveUniversitiesSerializer, \
    CityAutoCompleteRequestDataSerializer, CityAutoCompleteSerializer


class UniversityViewSet(viewsets.GenericViewSet):
    permission_classes = (AllowAny,)
    queryset = University.objects.all()

    @action(
        methods=['get'],
        detail=False,
        url_path='recommendations',
        url_name='recommendations',
    )
    def get_universities(self, request):
        ser_params = RequestDataSerializer(data=request.data)
        ser_params.is_valid(raise_exception=True)
        first_sub, second_sub, city = (
            ser_params.validated_data.get('first_subject'),
            ser_params.validated_data.get('second_subject'),
            ser_params.validated_data.get('city'),
        )
        subjects = (first_sub, second_sub)
        universities = University.objects.all() if city == 'ALL' else University.objects.filter(city__name=city)
        professions = Profession.objects.filter(first_subject__in=subjects, second_subject__in=subjects, university__in=universities)
        ser = RetrieveUniversitiesSerializer(professions, many=True)
        return Response(ser.data, status=status.HTTP_200_OK)

    @action(
        methods=['get'],
        detail=False,
        url_name='city/autocomplete',
        url_path='city/autocomplete',
    )
    def city_autocomplete(self, request):
        ser_params = CityAutoCompleteRequestDataSerializer(data=request.data)
        ser_params.is_valid(raise_exception=True)
        name = ser_params.validated_data.get('name')
        city = City.objects.filter(name__icontains=name).all()
        ser = CityAutoCompleteSerializer(city, many=True)
        return Response(ser.data, status=status.HTTP_200_OK)
