from django.db import models


class City(models.Model):
    name_en = models.CharField(max_length=255, null=True)
    name_ru = models.CharField(max_length=255, null=True)
    name_kz = models.CharField(max_length=255, null=True)
    created_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True, auto_now=True)

    class Meta:
        # managed = False
        db_table = 'cities'


class Subject(models.Model):
    name_en = models.CharField(max_length=255)
    name_ru = models.CharField(max_length=255)
    name_kz = models.CharField(max_length=255)

    class Meta:
        db_table = 'subjects'


class University(models.Model):
    code = models.CharField(max_length=255, null=True)
    name_en = models.TextField(null=True)
    name_ru = models.TextField(null=True)
    name_kz = models.TextField(null=True)
    city = models.ForeignKey(City, on_delete=None, related_name='universities')
    site = models.CharField(max_length=255, null=True)
    created_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True, auto_now=True)

    class Meta:
        # managed = False
        db_table = 'universities'


class Speciality(models.Model):
    code = models.CharField(max_length=255, null=True)
    name_en = models.TextField(null=True)
    name_ru = models.TextField(null=True)
    name_kz = models.TextField(null=True)
    description_en = models.TextField(null=True)
    description_ru = models.TextField(null=True)
    description_kz = models.TextField(null=True)
    university = models.ForeignKey(University, on_delete=None, related_name='specialities')
    first_subject = models.ForeignKey(Subject, on_delete=None, related_name='first_name')
    second_subject = models.ForeignKey(Subject, on_delete=None, related_name='second_name')
    total_grant = models.IntegerField(null=True)
    grant_kaz = models.IntegerField(null=True)
    grant_rus = models.IntegerField(null=True)
    created_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True, auto_now=True)

    class Meta:
        # managed = False
        db_table = 'specialities'


class Profession(models.Model):
    name_en = models.CharField(max_length=255, null=True)
    name_ru = models.CharField(max_length=255, null=True)
    name_kz = models.CharField(max_length=255, null=True)
    speciality = models.ForeignKey(Speciality, on_delete=None, related_name='professions')

    class Meta:
        db_table = 'professions'
