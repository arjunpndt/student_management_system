# Generated by Django 2.0 on 2020-07-15 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('E_R_P_students', '0002_auto_20200715_0035'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='students',
            name='Users_text',
        ),
        migrations.RemoveField(
            model_name='students',
            name='students_text',
        ),
        migrations.RemoveField(
            model_name='students',
            name='votes',
        ),
        migrations.RemoveField(
            model_name='users',
            name='pub_date',
        ),
        migrations.AddField(
            model_name='students',
            name='PASSWORD',
            field=models.CharField(default='KIET123', max_length=250),
        ),
        migrations.AddField(
            model_name='students',
            name='USER_NAME',
            field=models.CharField(default='NULL', max_length=250),
        ),
        migrations.AddField(
            model_name='students',
            name='branch',
            field=models.CharField(default='IT', max_length=250),
        ),
        migrations.AddField(
            model_name='students',
            name='father_name',
            field=models.CharField(default='father', max_length=250),
        ),
    ]