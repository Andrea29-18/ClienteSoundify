import flet as ft
import requests
from global_state import global_state
from decouple import config

api_url = config('API_URL')

API_BASE_URL = api_url +"/artista"

def settings_artista_view(page):
    user_data = global_state.user_data
    
    username = ft.TextField(label="Nombre de Usuario", width=300, value=user_data['NombreArtista'], disabled=True)
    email = ft.TextField(label="Correo", width=300, value=user_data['Correo'])
    phone = ft.TextField(label="Número Telefónico", width=300, value=user_data['NumeroTelefonico'])
    
    def update_user(e):
        response = requests.put(
            f"{API_BASE_URL}/{user_data['NombreArtista']}", 
            json={"Correo": email.value, "NumeroTelefonico": phone.value}
        )
        if response.status_code == 200:
            global_state.user_data['Correo'] = email.value
            global_state.user_data['NumeroTelefonico'] = phone.value
            page.snack_bar = ft.SnackBar(ft.Text("Artista actualizado exitosamente"), open=True)
        else:
            page.snack_bar = ft.SnackBar(ft.Text(response.json().get('message', 'Error al actualizar el artista')), open=True)

    def delete_artist(e):
        response = requests.delete(
            f"{API_BASE_URL}/{user_data['NombreArtista']}"
        )
        if response.status_code == 200:
            page.snack_bar = ft.SnackBar(ft.Text("Artista eliminado exitosamente"), open=True)
            page.go("/")  
        else:
            page.snack_bar = ft.SnackBar(ft.Text(response.json().get('message', 'Error al eliminar el usuario')), open=True)


    page.views.clear()
    page.views.append(
        ft.View(
            "/settings_artist",
            [
                ft.Column(
                    [
                        ft.Text("Configuración", size=30),
                        username,
                        email,
                        phone,
                        ft.ElevatedButton("Actualizar", on_click=update_user),
                        ft.ElevatedButton("Eliminar Cuenta", on_click=delete_artist, style=ft.ButtonStyle(bgcolor=ft.colors.RED)),
                        ft.ElevatedButton("Regresar a Menú", on_click=lambda _: page.go("/menu_artista"))
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                )
            ]
        )
    )
    page.update()

if __name__ == "__main__":
    ft.app(target=settings_artista_view)
