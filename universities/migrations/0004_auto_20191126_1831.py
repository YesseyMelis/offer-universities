# Generated by Django 2.2.6 on 2019-11-26 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('universities', '0003_auto_20191124_1724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='university',
            name='code',
            field=models.CharField(max_length=191),
        ),
    ]
