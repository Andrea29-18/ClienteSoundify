import flet as ft
from Login import login_view
from Register import register_view
from MenuAudiencia import menu_audiencia_view
from MenuArtista import menu_artista_view
from Favorites import favorites_view
from Settings import settings_view
from CreateAlbum import create_album_view
from BeArtist import be_artista_view
from SettingsArtist import settings_artista_view
from UploadSong import upload_song_view
from ListenerMusic import listening_music_view
from DowloadMusic import download_music_view
 
def main(page: ft.Page):
    def route_change(route):
        page.views.clear()
        if page.route == "/":
            login_view(page)
        elif page.route == "/register":
            register_view(page)
        elif page.route == "/menu_audiencia":
            menu_audiencia_view(page)
        elif page.route == "/menu_artista":
            menu_artista_view(page)
        elif page.route == "/favorites":
            favorites_view(page)
        elif page.route == "/settings":
            settings_view(page)
        elif page.route == "/settings_artist":
            settings_artista_view(page)
        elif page.route == "/create_album":
            create_album_view(page)
        elif page.route == "/be_artist":
            be_artista_view(page)
        elif page.route == "/upload_song":
            upload_song_view(page)
        elif page.route == "/listening_music":
            listening_music_view(page)
        elif page.route == "/download_music":
            download_music_view(page)
        page.update()

    page.on_route_change = route_change
    page.go("/")

ft.app(target=main)
