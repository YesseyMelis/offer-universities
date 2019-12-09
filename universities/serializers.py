from django.utils import timezone
from rest_framework import serializers
from django.db.models import Q

from universities.models import University, Profession, City, Speciality


class CitySerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    class Meta:
        model = City
        fields = (
            'name',
        )

    def get_name(self, obj):
        lang = self.context.get('lang')
        if lang == 'en':
            return obj.name_en
        elif lang == 'ru':
            return obj.name_ru
        return obj.name_kz


class UniversitySerializer(serializers.ModelSerializer):
    city = serializers.CharField(source='city.name', allow_null=True)
    name = serializers.SerializerMethodField()

    class Meta:
        model = University
        fields = (
            'name',
            'code',
            'city',
            'site',
        )

    def get_name(self, obj):
        lang = self.context.get('lang')
        if lang=='en':
            return obj.name_en
        elif lang=='ru':
            return obj.name_ru
        return obj.name_kz


class SpecialitySerializer(serializers.ModelSerializer):
    universities = serializers.SerializerMethodField()
    name = serializers.SerializerMethodField()

    class Meta:
        model = Speciality
        fields = (
            'name',
            'description',
            'code',
            'total_grant',
            'grant_rus',
            'grant_kaz',
            'universities',
        )

    def get_universities(self, obj):
        specs = Speciality.objects.filter(code=obj.code).values_list('university', flat=True)
        univers = University.objects.filter(id__in=specs)
        ser = UniversitySerializer(univers, many=True, context=self.context)
        return ser.data

    def get_name(self, obj):
        lang = self.context.get('lang')
        if lang=='en':
            return obj.name_en
        elif lang=='ru':
            return obj.name_ru
        return obj.name_kz


class RecommendationSerializer(serializers.ModelSerializer):
    profession = serializers.SerializerMethodField()
    specialities = serializers.SerializerMethodField()

    class Meta:
        model = Profession
        fields = (
            'profession',
            'specialities'
        )
    
    def get_specialities(self, obj):
        spec_ids = Profession.objects.filter(Q(name_en=obj.name_en) | Q(name_ru=obj.name_en) | Q(name_kz=obj.name_en)).values_list('speciality', flat=True)
        specs = Speciality.objects.filter(id__in=spec_ids)
        ser = SpecialitySerializer(specs, many=True, context=self.context)
        return ser.data

    def get_profession(self, obj):
        lang = self.context.get('lang')
        if lang=='en':
            return obj.name_en
        elif lang=='ru':
            return obj.name_ru
        return obj.name_kz


class RequestDataSerializer(serializers.Serializer):
    first_subject = serializers.CharField()
    second_subject = serializers.CharField()
    city = serializers.CharField()
    score = serializers.IntegerField()
    interface_lang = serializers.CharField()


class CityAutoCompleteRequestDataSerializer(serializers.Serializer):
    name = serializers.CharField()
