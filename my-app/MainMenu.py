import flet as ft
from ProfileSetting import profile_setting_page


def main_menu(page: ft.Page, login_page):
    page.title = "Menú Principal"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.START

    # Componentes de la UI del menú principal
    bienvenida = ft.Text("Bienvenido", size=24)
    boton_favoritos = ft.ElevatedButton(text="Favoritos")
    boton_configuracion = ft.ElevatedButton(text="Configuración Perfil", on_click=lambda e: page.clean() or profile_setting_page(page, login_page))  
    boton_cerrar_sesion = ft.ElevatedButton(text="Cerrar Sesión", on_click=lambda e: page.clean() or login_page(page))  

    # Agregar componentes a la página del menú principal
    page.add(
        ft.Column(
            [
                bienvenida,
                boton_favoritos,
                boton_configuracion,
                boton_cerrar_sesion
            ],
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.START,
            spacing=20  # Espaciado entre los botones
        )
    )
