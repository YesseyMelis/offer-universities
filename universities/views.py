from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from universities.models import University, Profession, City
from universities.serializers import RequestDataSerializer, RetrieveUniversitiesSerializer, \
    CityAutoCompleteRequestDataSerializer, CityAutoCompleteSerializer, CreateCitySerializer, CreateUniversitySerializer, \
    CreateProfessionSerializer, CreateUniversityValidateSerializer, CreateProfessionValidateSerializer


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

    @action(
        methods=['post'],
        detail=False,
        url_name='city/add',
        url_path='city/add',
    )
    def city_add(self, request):
        ser = CreateCitySerializer(data=request.data)
        ser.is_valid(raise_exception=True)
        ser.save()
        return Response(ser.data, status=status.HTTP_200_OK)

    @action(
        methods=['post'],
        detail=False,
        url_name='university/add',
        url_path='university/add',
    )
    def university_add(self, request):
        ser_valid = CreateUniversityValidateSerializer(data=request.data)
        ser_valid.is_valid(raise_exception=True)
        code, name, city = (
            ser_valid.validated_data.get('code'),
            ser_valid.validated_data.get('name'),
            ser_valid.validated_data.get('city_name'),
        )
        if City.objects.filter(name=city).exists():
            data = {
                'code': code,
                'name': name,
                'city': City.objects.filter(name=city).first().id
            }
            ser = CreateUniversitySerializer(data=data)
            ser.is_valid(raise_exception=True)
            ser.save()
            return Response(ser.data, status=status.HTTP_200_OK)
        return Response(
            {'error': 'City not found'},
            status=status.HTTP_404_NOT_FOUND
        )

    @action(
        methods=['post'],
        detail=False,
        url_name='profession/add',
        url_path='profession/add',
    )
    def profession_add(self, request):
        ser_valid = CreateProfessionValidateSerializer(data=request.data)
        ser_valid.is_valid(raise_exception=True)
        code, name, university_code, first, second = (
            ser_valid.validated_data.get('code'),
            ser_valid.validated_data.get('name'),
            ser_valid.validated_data.get('university_code'),
            ser_valid.validated_data.get('first_subject'),
            ser_valid.validated_data.get('second_subject'),
        )
        if University.objects.filter(code=university_code).exists():
            data = {
                'code': code,
                'name': name,
                'university': University.objects.filter(code=university_code).first().id,
                'first_subject': first,
                'second_subject': second,
            }
            ser = CreateProfessionSerializer(data=data)
            ser.is_valid(raise_exception=True)
            ser.save()
            return Response(ser.data, status=status.HTTP_200_OK)
        return Response({'error': 'University not found'}, status=status.HTTP_404_NOT_FOUND)
