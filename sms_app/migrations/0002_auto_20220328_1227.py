# Generated by Django 3.2.12 on 2022-03-28 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sms_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='roll_choice',
        ),
        migrations.AddField(
            model_name='user',
            name='roll',
            field=models.CharField(choices=[('SCHOOL', 'SCHOOL'), ('TEACHER', 'TEACHER'), ('STUDENT', 'STUDENT')], default='STUDENT', max_length=20),
        ),
    ]
