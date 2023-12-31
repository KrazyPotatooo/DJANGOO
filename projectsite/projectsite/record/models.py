from django.db import models

# Create your models here.
from django.db import models

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class artist(BaseModel):
    Artist_Name = models.AutoField(primary_key=True)
    Song = models.CharField(max_length=255)
    Email = models.EmailField()
    ProfileImage = models.ImageField(upload_to='artist_images/',blank=True, null=True)

    def __str__(self):
        return f"{self.Artist_Name} {self.Song}"

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

class albums(BaseModel):
    Artist_Name = models.ForeignKey(title, on_delete=models.CASCADE, default=1)  # Example default value '1'
    song_name = models.ForeignKey(duration, on_delete=models.CASCADE)
    
class date_added(models.Model):
    artist_name = models.AutoField(primary_key=True)
    albums_name = models.ForeignKey('albums', on_delete=models.CASCADE)  # Adding the 'albums' field
    song = models.ForeignKey('duration', on_delete=models.CASCADE)
    DateAdded = models.DateField()  # Adding the 'DateAdded' field as a DateField

    def __str__(self):
        return str(self.artist_name)  # Assuming ArtistName is an integer or ID

    class Meta:
        verbose_name_plural = "Date Added"  # Optional, sets the plural name for the model in the admin panel

