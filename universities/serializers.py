from django.utils import timezone
from rest_framework import serializers

from universities.models import University, Profession, City, Speciality


class UniversitySerializer(serializers.ModelSerializer):
    city = serializers.CharField(source='city.name', allow_null=True)

    class Meta:
        model = University
        fileds = (
            'name',
            'code',
            'sity',
            'city',
        )


class SpecialitySerializer(serializers.ModelSerializer):
    universities = serializers.SerializerMethodField()

    class Meta:
        model = Speciality
        fields = (
            'name',
            'code',
            'total_grant',
            'grant_rus',
            'grant_kaz',
            'universities',
        )

    def get_universities(self, obj):
        specs = Speciality.objects.filter(code=obj.code).values_list('university', flat=True)
        univers = University.objects.filter(id__in=specs)
        ser = UniversitySerializer(univers, many=True)
        return ser.data


class RecommendationSerializer(serializers.ModelSerializer):
    profession = serializers.CharField(source='name', allow_null=True)
    specialities = serializers.SerializerMethodField()

    class Meta:
        model = Profession
        fields = (
            'profession',
            'specialities'
        )
    
    def get_specialities(self, obj):
        spec_ids = Profession.objects.filter(name=obj.name).values_list('cpeciality', flat=True)
        specs = Speciality.objects.filter(id__in=spec_ids)
        ser = SpecialitySerializer(specs, many=True)
        return ser.data


class RequestDataSerializer(serializers.Serializer):
    first_subject = serializers.CharField()
    second_subject = serializers.CharField()
    city = serializers.CharField()
    score = serializers.IntegerField()


class CityAutoCompleteRequestDataSerializer(serializers.Serializer):
    name = serializers.CharField()


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = (
            'id',
            'name',
        )


class CreateCitySerializer(serializers.ModelSerializer):
    name = serializers.CharField()

    class Meta:
        model = City
        fields = (
            'id',
            'name',
        )

    def create(self, validated_data):
        return City.objects.create(**validated_data)


class CreateUniversityValidateSerializer(serializers.Serializer):
    code = serializers.CharField()
    name = serializers.CharField()
    city_name = serializers.CharField()


class CreateUniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = '__all__'

    def create(self, validated_data):
        return University.objects.create(**validated_data)


class CreateProfessionValidateSerializer(serializers.Serializer):
    code = serializers.CharField()
    name = serializers.CharField()
    university_code = serializers.CharField()
    first_subject = serializers.CharField()
    second_subject = serializers.CharField()


class CreateProfessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profession
        fields = '__all__'

    def create(self, validated_data):
        return Profession.objects.create(**validated_data)
