# Generated by Django 2.2.6 on 2019-12-10 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_en', models.CharField(max_length=255, null=True)),
                ('name_ru', models.CharField(max_length=255, null=True)),
                ('name_kz', models.CharField(max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'db_table': 'cities',
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_en', models.CharField(max_length=255)),
                ('name_ru', models.CharField(max_length=255)),
                ('name_kz', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'subjects',
            },
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=255, null=True)),
                ('name_en', models.TextField(null=True)),
                ('name_ru', models.TextField(null=True)),
                ('name_kz', models.TextField(null=True)),
                ('site', models.CharField(max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('city', models.ForeignKey(on_delete=None, related_name='universities', to='universities.City')),
            ],
            options={
                'db_table': 'universities',
            },
        ),
        migrations.CreateModel(
            name='Speciality',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=255, null=True)),
                ('name_en', models.TextField(null=True)),
                ('name_ru', models.TextField(null=True)),
                ('name_kz', models.TextField(null=True)),
                ('description_en', models.TextField(null=True)),
                ('description_ru', models.TextField(null=True)),
                ('description_kz', models.TextField(null=True)),
                ('total_grant', models.IntegerField(null=True)),
                ('grant_kaz', models.IntegerField(null=True)),
                ('grant_rus', models.IntegerField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('first_subject', models.ForeignKey(on_delete=None, related_name='first_name', to='universities.Subject')),
                ('second_subject', models.ForeignKey(on_delete=None, related_name='second_name', to='universities.Subject')),
                ('university', models.ForeignKey(on_delete=None, related_name='specialities', to='universities.University')),
            ],
            options={
                'db_table': 'specialities',
            },
        ),
        migrations.CreateModel(
            name='Profession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_en', models.CharField(max_length=255, null=True)),
                ('name_ru', models.CharField(max_length=255, null=True)),
                ('name_kz', models.CharField(max_length=255, null=True)),
                ('speciality', models.ForeignKey(on_delete=None, related_name='professions', to='universities.Speciality')),
            ],
            options={
                'db_table': 'professions',
            },
        ),
    ]
