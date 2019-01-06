# Generated by Django 2.0.7 on 2018-08-02 00:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_auto_20180801_2226'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slot',
            name='date_time',
        ),
        migrations.AddField(
            model_name='slot',
            name='end_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='slot',
            name='start_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
