import flet as ft
import requests

def register_page(page: ft.Page, return_to_login):
    page.title = "Registro de Usuario"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Componentes de la UI de registro
    correo = ft.TextField(label="Correo")
    username = ft.TextField(label="Nombre de usuario")
    password = ft.TextField(label="Contraseña", password=True, can_reveal_password=True)
    numero_telefonico = ft.TextField(label="Número telefónico")
    mensaje_registro = ft.Text()

    # Función de manejo del registro
    def registrar(e):
        # Datos del registro
        data = {
            'Correo': correo.value,
            'NombreUsuario': username.value,
            'Password': password.value,
            'NumeroTelefonico': numero_telefonico.value,
            'Canciones': []
        }

        try:
            # Realizar la solicitud a la API
            response = requests.post('http://localhost:3000/api/v2/audiencia', json=data)
            
            # Manejar la respuesta
            if response.status_code == 201:
                mensaje_registro.value = "Registro exitoso"
                mensaje_registro.color = "green"
            else:
                mensaje_registro.value = "Error en el registro"
                mensaje_registro.color = "red"
            
        except requests.exceptions.RequestException as err:
            mensaje_registro.value = f"Error al conectar con la API: {err}"
            mensaje_registro.color = "red"
        
        mensaje_registro.update()

    # Función para volver al login
    def volver_al_login(e):
        page.clean()  # Limpiar la página
        return_to_login(page)  # Volver a la pantalla de login

    boton_registrar = ft.ElevatedButton(text="Registrar", on_click=registrar)
    boton_volver = ft.TextButton(text="Volver al login", on_click=volver_al_login)

    # Agregar componentes a la página de registro
    page.add(
        ft.Column(
            [
                correo,
                username,
                password,
                numero_telefonico,
                boton_registrar,
                mensaje_registro,
                boton_volver
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )
