import flet as ft
import requests

API_BASE_URL = "http://192.168.0.105:3000/api/v2/audiencia"

def register_view(page):
    email = ft.TextField(label="Correo", width=300)
    username = ft.TextField(label="Nombre de Usuario", width=300)
    password = ft.TextField(label="Contraseña", width=300, password=True)
    phone = ft.TextField(label="Número Telefónico", width=300)
    
    def register(e):
        response = requests.post(f"{API_BASE_URL}/", json={"Correo": email.value, "NombreUsuario": username.value, "Password": password.value, "NumeroTelefonico": phone.value})
        if response.status_code == 201:
            page.snack_bar = ft.SnackBar(ft.Text("Registro exitoso"), open=True)
            page.go("/")
        else:
            page.snack_bar = ft.SnackBar(ft.Text(response.json().get('message', 'Error en el registro')), open=True)
    
    def go_to_login(e):
        page.go("/")
    
    page.views.clear()
    page.views.append(
        ft.View(
            "/register",
            [
                ft.Column(
                    [
                        ft.Text("Registrar", size=30),
                        email,
                        username,
                        password,
                        phone,
                        ft.ElevatedButton("Registrar", on_click=register),
                        ft.ElevatedButton("Regresar", on_click=go_to_login)
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                )
            ]
        )
    )
    page.update()

if __name__ == "__main__":
    ft.app(target=register_view)
