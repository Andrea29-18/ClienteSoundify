import flet as ft
import requests
from Models.UserSingleton import UserSingleton

def profile_setting_page(page: ft.Page, return_to_main_menu):
    page.title = "Actualizar Perfil"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Componentes de la UI de actualización de perfil
    correo = ft.TextField(label="Correo")
    username_field = ft.TextField(label="Nombre de usuario")
    numero_telefonico = ft.TextField(label="Número telefónico")
    mensaje_actualizacion = ft.Text()

    # Función de manejo de la actualización del perfil
    def update_user_data():
        # Obtener la instancia del Singleton
        user_singleton = UserSingleton()
        # Obtener el objeto de usuario
        user = user_singleton.get_user()
        if user:
            # Obtener el nombre de usuario
            username = user.get('NombreUsuario', '')
            # Construir los datos para actualizar el perfil
            data = {
                "Correo": correo.value,
                "NombreUsuario": username_field.value,
                "NumeroTelefonico": numero_telefonico.value
            }
            try:
                # Realizar la solicitud PUT a la API con el nombre de usuario obtenido
                response = requests.put(f'http://localhost:3000/api/v2/audiencia/{username}', json=data)
                
                # Manejar la respuesta
                if response.status_code == 200:
                    mensaje_actualizacion.value = "Datos de usuario actualizados correctamente"
                    mensaje_actualizacion.color = "green"
                else:
                    mensaje_actualizacion.value = "Error al actualizar los datos de usuario"
                    mensaje_actualizacion.color = "red"
                
            except requests.exceptions.RequestException as err:
                mensaje_actualizacion.value = f"Error al conectar con la API: {err}"
                mensaje_actualizacion.color = "red"
        else:
            mensaje_actualizacion.value = "No se pudo obtener el objeto de usuario del Singleton"
            mensaje_actualizacion.color = "red"

    boton_actualizar = ft.ElevatedButton(text="Actualizar", on_click=update_user_data)
    boton_volver = ft.TextButton(text="Volver al menú principal", on_click=return_to_main_menu)

    # Agregar componentes a la página de actualización de perfil
    page.add(
        ft.Column(
            [
                correo,
                username_field,
                numero_telefonico,
                boton_actualizar,
                mensaje_actualizacion,
                boton_volver
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )
