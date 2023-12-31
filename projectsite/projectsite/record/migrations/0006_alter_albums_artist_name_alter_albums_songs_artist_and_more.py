# Generated by Django 5.0 on 2023-12-31 06:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0005_alter_albums_artist_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='albums',
            name='Artist_Name',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='record.title'),
        ),
        migrations.AlterField(
            model_name='albums',
            name='Songs_artist',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='artist',
            name='ProfileImage',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
    ]
