# Generated by Django 2.0 on 2020-07-15 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('E_R_P_students', '0003_auto_20200715_1233'),
    ]

    operations = [
        migrations.RenameField(
            model_name='students',
            old_name='branch',
            new_name='Branch',
        ),
        migrations.RenameField(
            model_name='students',
            old_name='father_name',
            new_name='Father_name',
        ),
        migrations.AddField(
            model_name='students',
            name='Email',
            field=models.CharField(default='kiet123@.com', max_length=250, unique=True),
        ),
        migrations.AddField(
            model_name='students',
            name='Phone_no',
            field=models.BigIntegerField(default='1234567890', unique=True),
        ),
    ]
