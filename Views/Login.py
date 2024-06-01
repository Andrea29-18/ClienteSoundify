import flet as ft
import requests
from Register import register_page  # Importar la función de registro

def main(page: ft.Page):
    page.title = "Login con Flet y API"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Función para ir a la pantalla de registro
    def go_to_register(e):
        page.clean()  # Limpiar la página
        register_page(page, main)  # Llamar a la función de la página de registro

    # Componentes de la UI de login
    username = ft.TextField(label="Nombre de usuario")
    password = ft.TextField(label="Contraseña", password=True, can_reveal_password=True)
    mensaje_login = ft.Text()

    # Función de manejo del login
    def login(e):
        # Datos del login
        data = {
            'NombreUsuario': username.value,
            'Password': password.value
        }
        
        try:
            # Realizar la solicitud a la API
            response = requests.post('http://localhost:3000/api/v2/audiencia/login', json=data)
            
            # Manejar la respuesta
            if response.status_code == 200:
                mensaje_login.value = "Login exitoso"
                mensaje_login.color = "green"
            else:
                mensaje_login.value = "Nombre de usuario o contraseña incorrectos"
                mensaje_login.color = "red"
            
        except requests.exceptions.RequestException as err:
            mensaje_login.value = f"Error al conectar con la API: {err}"
            mensaje_login.color = "red"
        
        mensaje_login.update()

    boton_login = ft.ElevatedButton(text="Iniciar sesión", on_click=login)
    boton_registrar = ft.TextButton(text="Registrarse", on_click=go_to_register)

    # Agregar componentes a la página de login
    page.add(
        ft.Column(
            [
                username,
                password,
                boton_login,
                mensaje_login,
                boton_registrar
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )

ft.app(target=main)
