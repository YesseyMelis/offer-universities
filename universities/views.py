from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.db.models import Q

from universities.models import University, Profession, City, Speciality
from universities.serializers import RequestDataSerializer, RecommendationSerializer, \
    CityAutoCompleteRequestDataSerializer, CitySerializer

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
        ser_params = RequestDataSerializer(data=request.query_params)
        ser_params.is_valid(raise_exception=True)
        first_sub, second_sub, city, score, inter_lang = (
            ser_params.validated_data.get('first_subject'),
            ser_params.validated_data.get('second_subject'),
            ser_params.validated_data.get('city'),
            ser_params.validated_data.get('score'),
            ser_params.validated_data.get('interface_lang')
        )
        subjects = (first_sub, second_sub)
        universities = University.objects.all() if city == 'ALL' else University.objects.filter(Q(city__name_en=city) | Q(city__name_ru=city) | Q(city__name_kz=city))
        specialities = Speciality.objects.filter(first_subject__in=subjects, second_subject__in=subjects, university__in=universities)
        professions = Profession.objects.filter(speciality_id__in=specialities)
        ser = RecommendationSerializer(professions, many=True, context={'lang': inter_lang})
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
        city = City.objects.filter(Q(name_en__icontains=name) | Q(name_ru__icontains=name) | Q(name_kz__icontains=name)).all()
        ser = CitySerializer(city, many=True)
        return Response(ser.data, status=status.HTTP_200_OK)
    
    @action(
        methods=['get'],
        detail=False,
        url_name='city/list',
        url_path='city/list',
    )
    def city_list(self, request):
        inter_lang = request.query_params.get('interface_lang')
        cities = City.objects.all()
        values = cities.values_list('name_en', flat=True)
        if inter_lang == 'ru':
            values = cities.values_list('name_ru', flat=True)
        elif inter_lang == 'kz':
            values = cities.values_list('name_kz', flat=True)
        return Response({'data': values}, status=status.HTTP_200_OK)

    @action(
        methods=['get'],
        detail=False,
        url_name='subject/list',
        url_path='subject/list',
    )
    def subject_list(self, request):
        f_subs = Speciality.objects.all().values_list('first_subject', flat=True).distinct()
        s_subs = Speciality.objects.all().values_list('second_subject', flat=True).distinct()
        subs = list(set(list(f_subs) + list(s_subs)))
        return Response({'data': subs}, status=status.HTTP_200_OK)
