# Generated by Django 3.2.5 on 2021-08-08 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_app', '0009_register_students_birthdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register_students',
            name='birthdate',
            field=models.DateField(blank=True, null=True),
        ),
    ]
