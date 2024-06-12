import flet as ft
import requests
from global_state import global_state

API_BASE_URL = "http://192.168.1.72:3000/api/v2/audiencia"

def settings_view(page):
    user_data = global_state.user_data
    token = global_state.token
    
    username = ft.TextField(label="Nombre de Usuario", width=300, value=user_data['NombreUsuario'], disabled=True)
    email = ft.TextField(label="Correo", width=300, value=user_data['Correo'])
    phone = ft.TextField(label="Número Telefónico", width=300, value=user_data['NumeroTelefonico'])

    def go_to_beArtist(e):
        page.go("/be_artist")
    
    def update_user(e):
        response = requests.put(
            f"{API_BASE_URL}/{user_data['NombreUsuario']}", 
            headers={"Authorization": f"Bearer {token}"}, 
            json={"Correo": email.value, "NumeroTelefonico": phone.value}
        )
        if response.status_code == 200:
            global_state.user_data['Correo'] = email.value
            global_state.user_data['NumeroTelefonico'] = phone.value
            page.snack_bar = ft.SnackBar(ft.Text("Usuario actualizado exitosamente"), open=True)
        else:
            page.snack_bar = ft.SnackBar(ft.Text(response.json().get('message', 'Error al actualizar el usuario')), open=True)

    page.views.clear()
    page.views.append(
        ft.View(
            "/settings",
            [
                ft.Column(
                    [
                        ft.Text("Configuración", size=30),
                        username,
                        email,
                        phone,
                        ft.ElevatedButton("Actualizar", on_click=update_user),
                        ft.ElevatedButton("Ser Artista", on_click=go_to_beArtist),
                        ft.ElevatedButton("Regresar a Menú", on_click=lambda _: page.go("/menu_audiencia"))
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                )
            ]
        )
    )
    page.update()

if __name__ == "__main__":
    ft.app(target=settings_view)
