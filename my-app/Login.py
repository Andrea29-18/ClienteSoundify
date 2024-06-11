import flet as ft
import requests

API_BASE_URL = "http://192.168.3.37:3000/api/v2/audiencia"
token = None

def login_view(page):
    username = ft.TextField(label="Nombre de Usuario", width=300)
    password = ft.TextField(label="Contraseña", width=300, password=True)
    
    def login(e):
        response = requests.post(f"{API_BASE_URL}/login", json={"NombreUsuario": username.value, "Password": password.value})
        if response.status_code == 200:
            global token
            token = response.json()['token']
            page.snack_bar = ft.SnackBar(ft.Text("Inicio de sesión exitoso"), open=True)
            page.go("/menu")
        else:
            page.snack_bar = ft.SnackBar(ft.Text("Error en el inicio de sesión"), open=True)

    def go_to_register(e):
        page.go("/register")
    
    page.views.clear()
    page.views.append(
        ft.View(
            "/",
            [
                ft.Column(
                    [
                        ft.Text("Iniciar Sesión", size=30),
                        username,
                        password,
                        ft.ElevatedButton("Entrar", on_click=login),
                        ft.ElevatedButton("Registrar", on_click=go_to_register)
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                )
            ]
        )
    )
    page.update()

if __name__ == "__main__":
    ft.app(target=login_view)
