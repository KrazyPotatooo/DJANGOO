from django.contrib import admin
from .models import artist, duration, title, albums, date_added

@admin.register(artist)
class artistAdmin(admin.ModelAdmin):
    list_display = ("Artist_ID", "Song","Email", "created_at", "updated_at")
    search_fields = ("Artist_ID", "Song","Email",)

@admin.register(duration)
class durationAdmin(admin.ModelAdmin):
    list_display = ("Song_ID", "artist_Names","Duration", "created_at", "updated_at")
    search_fields = ("Song_ID", "artist_Names","Duration")

@admin.register(title)
class TitleAdmin(admin.ModelAdmin):
    list_display = ("song_number", "get_artist", "Email", "created_at", "updated_at")
    search_fields = ("song_number", "artist__Artist_Name", "Email",)  # Use 'artist__Artist_Name' for related fields

    def get_artist(self, obj):
        return obj.Artist.song_number if hasattr(obj, 'Email') else ''
    get_artist.short_description = 'Artist'

@admin.register(albums)
class albumsAdmin(admin.ModelAdmin):
   list_display = ("ArtistID", "song_Name") # Assuming 'ArtistName' and 'SongName' are correct field names
   search_fields = ("ArtistID","song_Name")  # Adjusting search fields based on the model relationships

@admin.register(date_added)
class date_addedAdmin(admin.ModelAdmin):
    list_display = ("artistID", "albums_name", "song","DateAdded")  
    search_fields = ("artistID", "albums_name", "song","DateAdded")  # Using '__' for related fields
