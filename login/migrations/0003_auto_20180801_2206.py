# Generated by Django 2.0.7 on 2018-08-01 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_auto_20180801_2135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='username',
            field=models.EmailField(blank=True, max_length=140, null=True, unique=True),
        ),
    ]
