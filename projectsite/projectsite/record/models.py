from django.utils.translation import gettext as _
from django.db import models
from django.utils import timezone

from django.core.exceptions import ValidationError

# Create your models here.
from django.db import models

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class artist(BaseModel):
    Artist_ID = models.AutoField(primary_key=True)  # Assuming you still want an AutoField for the primary key
    Artist_ScreenName = models.CharField(max_length=100, default='')  # Adding a default value
    Song = models.CharField(max_length=255)
    Email = models.EmailField()
    ProfileImage = models.ImageField(upload_to='artist_images/', blank=True, null=True)

    def __str__(self):
        return f"{self.Artist_ScreenName} - {self.Song}"


class duration(BaseModel):
    Song_Name = models.AutoField(primary_key=True)
    Duration = models.ForeignKey(artist, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.Song_Name) 

class title(BaseModel):
    song_name = models.AutoField(primary_key=True)
    Artist = models.CharField(max_length=255)
    Email = models.EmailField()
  
    def __str__(self):
        return f"{self.song_name} {self.Artist}"

def no_numbers_validator(value):
    if any(char.isdigit() for char in value):
        raise ValidationError('Field should not contain numbers')

class albums(models.Model):
    song_Name= models.AutoField(primary_key=True)
    song_Name = models.CharField(max_length=255, default=timezone.now)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.MusicAlbumsName_ID} - {self.song_Name}"

from django.db import models

class date_added(models.Model):
    id = models.AutoField(primary_key=True)
    albums_name = models.ForeignKey('albums', on_delete=models.CASCADE)  # Replace 'Album' with the actual model name
    song = models.ForeignKey('duration', on_delete=models.CASCADE)
    DateAdded = models.DateField()

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name_plural = "Date Added"





