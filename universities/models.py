from django.db import models


class City(models.Model):
    name = models.CharField(max_length=191)

    objects = models.Manager()

    class Meta:
        # managed = False
        db_table = 'cities'


class University(models.Model):
    name = models.CharField(max_length=191)
    city = models.ForeignKey(City, on_delete=None, related_name='universities')

    objects = models.Manager()

    class Meta:
        # managed = False
        db_table = 'universities'


class Profession(models.Model):
    name = models.CharField(max_length=191)
    university = models.ForeignKey(University, on_delete=None, related_name='professions')

    objects = models.Manager()

    class Meta:
        # managed = False
        db_table = 'professions'


class Subjects(models.Model):
    first_subject = models.CharField(max_length=191)
    second_subject = models.CharField(max_length=191)
    profession = models.ForeignKey(Profession, on_delete=None, related_name='subjects')

    objects = models.Manager()

    class Meta:
        # managed = False
        db_table = 'subjects'

