# Generated by Django 2.0.7 on 2018-08-01 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_auto_20180801_2141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slot',
            name='user',
            field=models.EmailField(blank=True, max_length=140, null=True, unique=True),
        ),
    ]
