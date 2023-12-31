from django.db import models
from django.utils import timezone
import uuid
from django.core.exceptions import ValidationError
from .models.date_added import DateAdded  # Check the exact structure and class name


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class artist(BaseModel):
    Artist_ID = models.AutoField(primary_key=True)
    Artist_ScreenName = models.CharField(max_length=100, default='')
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

class albums(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    song_Name = models.CharField(max_length=255, default=timezone.now)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.id} - {self.song_Name}"
