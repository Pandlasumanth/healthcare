# Generated by Django 2.1.3 on 2018-12-03 13:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patients_register',
            old_name='Addres',
            new_name='Address',
        ),
    ]
