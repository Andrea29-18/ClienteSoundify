import flet as ft
from Login import login_view
from Register import register_view
from Menu import menu_view
from Favorites import favorites_view
from Settings import settings_view

def main(page: ft.Page):
    def route_change(route):
        page.views.clear()
        if page.route == "/":
            login_view(page)
        elif page.route == "/register":
            register_view(page)
        elif page.route == "/menu":
            menu_view(page)
        elif page.route == "/favorites":
            favorites_view(page)
        elif page.route == "/settings":
            settings_view(page)
        page.update()

    page.on_route_change = route_change
    page.go("/")

ft.app(target=main)
