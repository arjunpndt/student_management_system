# Generated by Django 2.0 on 2020-07-18 18:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('E_R_P_students', '0012_auto_20200718_1732'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quires',
            name='query',
        ),
    ]
