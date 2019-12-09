from django.db import models


class City(models.Model):
    name = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True, auto_now=True)

    objects = models.Manager()

    class Meta:
        # managed = False
        db_table = 'cities'


class University(models.Model):
    code = models.CharField(max_length=191)
    name = models.CharField(max_length=191)
    city = models.ForeignKey(City, on_delete=None, related_name='universities')
    created_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True, auto_now=True)

    objects = models.Manager()

    class Meta:
        # managed = False
        db_table = 'universities'


class Speciality(models.Model):
    code = models.CharField(max_length=191)
    name = models.CharField(max_length=191)
    university = models.ForeignKey(University, on_delete=None, related_name='specialities')
    first_subject = models.CharField(max_length=191)
    second_subject = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True, auto_now=True)


    objects = models.Manager()

    class Meta:
        # managed = False
        db_table = 'specialities'


class Profession(models.Model):
    name = models.CharField(max_length=191)
    speciality = models.ForeignKey(Speciality, on_delete=None, related_name='professions')

    class Meta:
        db_table = 'professions'