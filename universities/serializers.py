from django.utils import timezone
from rest_framework import serializers

from universities.models import University, Profession


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


class QueryParamsSerializer(serializers.Serializer):
    first_subject = serializers.CharField()
    second_subject = serializers.CharField()
    city = serializers.CharField()
