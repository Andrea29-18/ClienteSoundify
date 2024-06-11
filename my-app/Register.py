import flet as ft
import requests

API_BASE_URL = "http://192.168.3.37:3000/api/v2/audiencia"

def register_view(page):
    email = ft.TextField(label="Correo", width=300)
    username = ft.TextField(label="Nombre de Usuario", width=300)
    password = ft.TextField(label="Contraseña", width=300, password=True)
    phone = ft.TextField(label="Número Telefónico", width=300)
    
    def register(e):
        response = requests.post(API_BASE_URL, json={
            "Correo": email.value,
            "NombreUsuario": username.value,
            "Password": password.value,
            "NumeroTelefonico": phone.value,
            "Canciones": []
        })
        if response.status_code == 201:
            page.snack_bar = ft.SnackBar(ft.Text("Usuario registrado exitosamente"), open=True)
            page.go("/")
        else:
            page.snack_bar = ft.SnackBar(ft.Text("Error en el registro"), open=True)

    page.views.clear()
    page.views.append(
        ft.View(
            "/register",
            [
                ft.Column(
                    [
                        ft.Text("Registrar Usuario", size=30),
                        email,
                        username,
                        password,
                        phone,
                        ft.ElevatedButton("Registrar", on_click=register),
                        ft.ElevatedButton("Regresar", on_click=lambda _: page.go("/"))
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
