import flet as ft
from Login import login_view
from Register import register_view
from MenuAudiencia import menu_audiencia_view
from MenuArtista import menu_artista_view
from Favorites import favorites_view
from Settings import settings_view
from CrearAlbum import create_album_view

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
        elif page.route == "/create_album":
            create_album_view(page)
        page.update()

    page.on_route_change = route_change
    page.go("/")

ft.app(target=main)
