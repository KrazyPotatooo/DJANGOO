# Generated by Django 5.0 on 2023-12-31 08:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0006_rename_albums_name_date_added_albums'),
    ]

    operations = [
        migrations.RenameField(
            model_name='date_added',
            old_name='albums',
            new_name='albums_name',
        ),
    ]