import flet as ft
import requests

API_BASE_URL = "http://192.168.3.37:3000/api/v2/audiencia"
token = None

def settings_view(page):
    username = ft.TextField(label="Nombre de Usuario", width=300, disabled=True)
    email = ft.TextField(label="Correo", width=300)
    phone = ft.TextField(label="Número Telefónico", width=300)
    
    def load_user_data():
        response = requests.get(f"{API_BASE_URL}/{username.value}", headers={"Authorization": f"Bearer {token}"})
        if response.status_code == 200:
            data = response.json()['data']
            email.value = data['Correo']
            phone.value = data['NumeroTelefonico']
            page.update()
        else:
            page.snack_bar = ft.SnackBar(ft.Text("Error al cargar los datos del usuario"), open=True)

    def update_user(e):
        response = requests.put(f"{API_BASE_URL}/{username.value}", headers={"Authorization": f"Bearer {token}"}, json={
            "Correo": email.value,
            "NumeroTelefonico": phone.value
        })
        if response.status_code == 200:
            page.snack_bar = ft.SnackBar(ft.Text("Usuario actualizado exitosamente"), open=True)
        else:
            page.snack_bar = ft.SnackBar(ft.Text("Error al actualizar el usuario"), open=True)

    load_user_data()

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
                        ft.ElevatedButton("Regresar a Menú", on_click=lambda _: page.go("/menu"))
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
