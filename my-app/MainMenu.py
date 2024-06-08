import flet as ft
from ProfileSetting import profile_setting_page
from CargarCancion import cargar_cancion_page

def main_menu(page: ft.Page, login_page, user_object):
    page.title = "Menú Principal"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.START

    bienvenida = ft.Text(f"Bienvenido {user_object.get('NombreUsuario')}", size=24)
    boton_favoritos = ft.ElevatedButton(text="Favoritos")
    boton_configuracion = ft.ElevatedButton(text="Configuración Perfil", on_click=lambda e: page.clean() or profile_setting_page(page, login_page, user_object))
    boton_cargar_cancion = ft.ElevatedButton(text="Cargar Canción", on_click=lambda e: page.clean() or cargar_cancion_page(page, main_menu))
    boton_cerrar_sesion = ft.ElevatedButton(text="Cerrar Sesión", on_click=lambda e: page.clean() or login_page(page))

    page.add(
        ft.Column(
            [
                bienvenida,
                boton_favoritos,
                boton_configuracion,
                boton_cargar_cancion,
                boton_cerrar_sesion
            ],
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.START,
            spacing=20
        )
    )
