# Generated by Django 5.0 on 2023-12-31 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0021_duration_artistname'),
    ]

    operations = [
        migrations.AddField(
            model_name='date_added',
            name='albumsArtist',
            field=models.CharField(default=60, max_length=50),
            preserve_default=False,
        ),
    ]
