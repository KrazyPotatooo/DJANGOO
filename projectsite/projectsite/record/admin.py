from django.contrib import admin
from .models import artist, duration, title, albums, date_added

@admin.register(artist)
class artistAdmin(admin.ModelAdmin):
    list_display = ("Artist_ID", "Song", "Email", "created_at", "updated_at")
    search_fields = ("Artist_ID", "Song", "Email",)

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
    list_display = ('get_music_albums_name', 'song_Name')  # Adjust this based on available fields

    def get_music_albums_name(self, obj):
        return obj.MusicAlbumsName_ID  # Replace this with the correct attribute/method

    get_music_albums_name.short_description = 'Music Albums Name'




@admin.register(date_added)
class date_addedAdmin(admin.ModelAdmin):
    list_display = ('id', 'albums_name', 'song', 'DateAdded')

    def get_artist_name(self, obj):
        # Assuming 'song' references 'duration' and 'duration' has a foreign key to 'artist'
        return obj.song.Duration.Artist.Artist_ScreenName if obj.song else ''
    
    get_artist_name.short_description = 'Artist'

