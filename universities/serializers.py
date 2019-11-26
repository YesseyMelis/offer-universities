from django.utils import timezone
from rest_framework import serializers

from universities.models import University, Profession, City


class RetrieveUniversitiesSerializer(serializers.ModelSerializer):
    university_name = serializers.CharField(source='university.name', allow_null=True)
    city_name = serializers.CharField(source='university.city.name', allow_null=True)

    class Meta:
        model = Profession
        fields = (
            'code',
            'name',
            'university_name',
            'city_name',
        )


class RequestDataSerializer(serializers.Serializer):
    first_subject = serializers.CharField()
    second_subject = serializers.CharField()
    city = serializers.CharField()


class CityAutoCompleteRequestDataSerializer(serializers.Serializer):
    name = serializers.CharField()


class CityAutoCompleteSerializer(serializers.ModelSerializer):
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
