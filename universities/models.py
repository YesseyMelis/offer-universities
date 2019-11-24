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
    code = models.IntegerField(null=True)
    name = models.CharField(max_length=191)
    city = models.ForeignKey(City, on_delete=None, related_name='universities')
    created_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True, auto_now=True)

    objects = models.Manager()

    class Meta:
        # managed = False
        db_table = 'universities'


class Profession(models.Model):
    code = models.CharField(max_length=191, null=True)
    name = models.CharField(max_length=191)
    university = models.ForeignKey(University, on_delete=None, related_name='professions')
    created_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True, auto_now=True)

    objects = models.Manager()

    class Meta:
        # managed = False
        db_table = 'professions'


class Subjects(models.Model):
    first_subject = models.CharField(max_length=191)
    second_subject = models.CharField(max_length=191)
    profession = models.ForeignKey(Profession, on_delete=None, related_name='subjects')
    created_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True, auto_now=True)

    objects = models.Manager()

    class Meta:
        # managed = False
        db_table = 'subjects'
