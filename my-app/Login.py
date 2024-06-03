import flet as ft
import requests
import jwt
from Register import register_page  # Importar la función de registro
from MainMenu import main_menu  # Importar la función del menú principal

def login_page(page: ft.Page):
    page.title = "Login con Flet y API"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Función para ir a la pantalla de registro
    def go_to_register(e):
        page.clean()  # Limpiar la página
        register_page(page, login_page)  # Llamar a la función de la página de registro

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
            response = requests.post('http://192.168.56.108:3000/api/v2/audiencia/login', json=data)
            
            # Manejar la respuesta
            if response.status_code == 200:
                response_data = response.json()
                print(response_data)  # Imprimir los datos de la respuesta para depuración
                token = response_data.get('token')
                
                if token:
                    # Decodificar el token JWT para obtener el objeto de usuario
                    decoded_token = jwt.decode(token, options={"verify_signature": False})
                    user_object = {
                        'NombreUsuario': decoded_token.get('NombreUsuario'),
                        'Correo': decoded_token.get('Correo')
                    }
                    mensaje_login.value = "Login exitoso"
                    mensaje_login.color = "green"
                    page.clean()
                    main_menu(page, login_page, user_object)  # Navegar al menú principal pasando el objeto de usuario
                else:
                    mensaje_login.value = "Error: No se pudo obtener el token."
                    mensaje_login.color = "red"
            elif response.status_code == 404:
                mensaje_login.value = "Usuario no encontrado"
                mensaje_login.color = "red"
            elif response.status_code == 401:
                mensaje_login.value = "Contraseña incorrecta"
                mensaje_login.color = "red"
            else:
                mensaje_login.value = f"Error: {response.status_code} {response.json().get('message')}"
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

def main(page: ft.Page):
    login_page(page)

ft.app(target=main)
