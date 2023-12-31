from django.db import models
from django.utils import timezone
from django.utils.translation import gettext as _
from django.core.exceptions import ValidationError
# Create your models here.

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class artist(BaseModel):
    Artist_ID = models.AutoField(primary_key=True)
    Artist_name = models.CharField(max_length=100, default='') 
    Song = models.CharField(max_length=255)
    Email = models.EmailField()
    ProfileImage = models.ImageField(upload_to='media/',blank=True, null=True)
    nameofartist = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.Artist_ID} {self.Song}"

class duration(BaseModel):
    Song_ID = models.AutoField(primary_key=True)
    artist_Names =models.CharField(max_length=255)
    Duration = models.CharField(max_length=255)
    NamesArtist = models.CharField(max_length=255)
    ARTistName = models.CharField(max_length=255)

    def __str__(self):
        return str(self.artist_Names) 

class title(BaseModel):
    song_number = models.AutoField(primary_key=True)
    Artist = models.CharField(max_length=255)
    Email = models.EmailField()
  
    def __str__(self):
        return f"{self.song_number} {self.Artist}"
    
def no_numbers_validator(value):
    if any(char.isdigit() for char in value):
        raise ValidationError('Field should not contain numbers')  
    
class albums(models.Model):
    ArtistID = models.ForeignKey(title, on_delete=models.CASCADE, default=None)
    song_Name = models.CharField(max_length=255, default="")
    Songs_artist = models.CharField(max_length=255) 
   
    def __str__(self):
        return f"{self.ArtistID} - {self.ArtistID}"
    
class date_added(models.Model):
    artistID = models.AutoField(primary_key=True)
    albumsArtist = models.CharField( max_length=50)
    albums_name = models.CharField(max_length=255)  # Adding the 'albums' field
    song = models.CharField(max_length=255)
    DateAdded = models.DateField() 
    artistNames=models.CharField(max_length=255)# Adding the 'DateAdded' field as a DateField

    def __str__(self):
        return str(self.artistID)  # Assuming ArtistName is an integer or ID

    class Meta:
        verbose_name_plural = "Date Added"  # Optional, sets the plural name for the model in the admin panel

