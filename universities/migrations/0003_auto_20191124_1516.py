# Generated by Django 2.2.6 on 2019-11-24 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('universities', '0002_auto_20191123_2238'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='city',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='profession',
            name='code',
            field=models.CharField(max_length=191, null=True),
        ),
        migrations.AddField(
            model_name='profession',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='profession',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='subjects',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='subjects',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='university',
            name='code',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='university',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='university',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
