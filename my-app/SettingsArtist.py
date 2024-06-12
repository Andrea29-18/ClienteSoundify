import flet as ft
import requests
from global_state import global_state

API_BASE_URL = "http://192.168.1.72:3000/api/v2/artista"

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