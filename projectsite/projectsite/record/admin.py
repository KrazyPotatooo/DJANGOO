from django.contrib import admin
from .models import artist, duration, title, albums, date_added

@admin.register(artist)
class artistAdmin(admin.ModelAdmin):
    list_display = ("Artist_Name", "Song", "Email", "created_at", "updated_at")
    search_fields = ("Artist_Name", "Song", "Email",)

@admin.register(duration)
class durationAdmin(admin.ModelAdmin):
    list_display = ("Song_Name", "Duration", "created_at", "updated_at")
    search_fields = ("Song_Name", "Duration")

@admin.register(title)
class TitleAdmin(admin.ModelAdmin):
    list_display = ("song_name", "get_artist", "Email", "created_at", "updated_at")
    search_fields = ("song_name", "artist__Artist_Name", "Email",)  # Use 'artist__Artist_Name' for related fields

    def get_artist(self, obj):
        return obj.artist.Artist_Name if hasattr(obj, 'artist') else ''
    get_artist.short_description = 'Artist'

@admin.register(albums)
class albumsAdmin(admin.ModelAdmin):
    list_display = ("Artist_Name", "song_name", "song_artist") # Assuming 'ArtistName' and 'SongName' are correct field names
    search_fields = ("Artist_Name", "song_name", "song_artist")  # Adjusting search fields based on the model relationships

@admin.register(date_added)
class date_addedAdmin(admin.ModelAdmin):
    list_display = ("artist_name", "albums_name", "DateAdded")  
    search_fields = ("artist_name", "albums_name", "DateAdded")  # Using '__' for related fields
