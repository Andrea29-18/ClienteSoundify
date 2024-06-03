import flet as ft
import requests
from CreateArtist import create_artist_page  # Importa la función de la nueva vista

def profile_setting_page(page: ft.Page, login_page, user_object):
    page.title = "Configuración de Perfil"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.START

    nombre_usuario = ft.TextField(label="Nombre de usuario", value=user_object.get('NombreUsuario'))
    correo_usuario = ft.TextField(label="Correo", value=user_object.get('Correo'))
    numero_telefonico = ft.TextField(label="Número Telefónico", value=user_object.get('NumeroTelefonico'))
    mensaje_actualizacion = ft.Text()

    def update_profile(e):
        new_data = {
            "Correo": correo_usuario.value,
            "NumeroTelefonico": numero_telefonico.value,
        }

        try:
            token = user_object.get('token')
            headers = {
                "Authorization": f"Bearer {token}",
                "Content-Type": "application/json"
            }

            response = requests.put(
                f"http://192.168.56.108:3000/api/v2/audiencia/update/{user_object.get('NombreUsuario')}",
                json=new_data,
                headers=headers
            )

            if response.status_code == 200:
                response_data = response.json()
                updated_user = response_data.get('data')
                mensaje_actualizacion.value = "Perfil actualizado correctamente"
                mensaje_actualizacion.color = "green"
                user_object.update(updated_user)
            else:
                mensaje_actualizacion.value = f"Error: {response.status_code} {response.json().get('message')}"
                mensaje_actualizacion.color = "red"
            
        except requests.exceptions.RequestException as err:
            mensaje_actualizacion.value = f"Error al conectar con la API: {err}"
            mensaje_actualizacion.color = "red"
        
        mensaje_actualizacion.update()

    boton_subir_nivel = ft.ElevatedButton(text="Subir de Nivel", on_click=lambda e: page.clean() or create_artist_page(page, profile_setting_page, user_object))
    boton_actualizar = ft.ElevatedButton(text="Actualizar", on_click=update_profile)
    boton_volver = ft.ElevatedButton(text="Volver", on_click=lambda e: page.clean() or login_page(page))

    page.add(
        ft.Column(
            [
                nombre_usuario,
                correo_usuario,
                numero_telefonico,
                boton_actualizar,
                boton_subir_nivel,
                mensaje_actualizacion,
                boton_volver
            ],
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.START,
            spacing=20
        )
    )
