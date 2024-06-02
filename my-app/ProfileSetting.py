import flet as ft
import requests

def profile_setting_page(page: ft.Page, return_to_main_menu):
    page.title = "Actualizar Perfil"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Componentes de la UI de actualización de perfil
    correo = ft.TextField(label="Correo")
    username = ft.TextField(label="Nombre de usuario")
    password = ft.TextField(label="Contraseña", password=True, can_reveal_password=True)
    numero_telefonico = ft.TextField(label="Número telefónico")
    mensaje_actualizacion = ft.Text()

    # Función de manejo de la actualización del perfil
    def update_user_data():
        # Datos para actualizar el usuario
        data = {
            "Correo": correo.value,
            "Password": password.value,
            "NumeroTelefonico": numero_telefonico.value
        }

        try:
            # Obtener el nombre de usuario del objeto de usuario
            user_singleton = ft.Singleton.get_instance("user_singleton")
            user = user_singleton.get_user()
            if user:
                username = user.get("NombreUsuario")
                # Realizar la solicitud PUT a la API
                response = requests.put(f'http://localhost:3000/api/v2/audiencia/{username}', json=data)
                
                # Manejar la respuesta
                if response.status_code == 200:
                    mensaje_actualizacion.value = "Datos de usuario actualizados correctamente"
                    mensaje_actualizacion.color = "green"
                else:
                    mensaje_actualizacion.value = "Error al actualizar los datos de usuario"
                    mensaje_actualizacion.color = "red"
            else:
                mensaje_actualizacion.value = "No se pudo obtener el objeto de usuario"
                mensaje_actualizacion.color = "red"
            
        except requests.exceptions.RequestException as err:
            mensaje_actualizacion.value = f"Error al conectar con la API: {err}"
            mensaje_actualizacion.color = "red"

    # Botón para actualizar perfil
    boton_actualizar = ft.ElevatedButton(text="Actualizar", on_click=update_user_data)
    
    # Botón para volver al menú principal
    boton_volver = ft.TextButton(text="Volver al menú principal", on_click=return_to_main_menu)

    # Agregar componentes a la página de actualización de perfil
    page.add(
        ft.Column(
            [
                correo,
                username,
                password,
                numero_telefonico,
                boton_actualizar,
                mensaje_actualizacion,
                boton_volver
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )
