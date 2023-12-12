# Generated by Django 5.0 on 2023-12-11 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_contacts', '0002_alter_contact_birthday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone_number',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
