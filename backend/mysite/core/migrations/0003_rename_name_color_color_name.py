# Generated by Django 5.0.4 on 2024-04-17 05:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_color_person_color'),
    ]

    operations = [
        migrations.RenameField(
            model_name='color',
            old_name='name',
            new_name='color_name',
        ),
    ]