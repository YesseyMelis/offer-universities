from django.utils import timezone
from rest_framework import serializers

from universities.models import University


class RetrieveUniversitiesSerializer(serializers.ModelSerializer):

    class Meta:
        model = University
        fields = '__all__'


class QueryParamsSerializer(serializers.Serializer):
    first_subject = serializers.CharField()
    second_subject = serializers.CharField()
    city = serializers.CharField()
