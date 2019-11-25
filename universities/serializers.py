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
