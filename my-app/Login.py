import flet as ft
import requests
from global_state import global_state
import threading
import time

API_BASE_URL = "http://192.168.0.105:3000/api/v2/audiencia"

def login_view(page):
    username = ft.TextField(label="Nombre de Usuario", width=300)
    password = ft.TextField(label="Contraseña", width=300, password=True)
    
    def login(e):
        response = requests.post(f"{API_BASE_URL}/login", json={"NombreUsuario": username.value, "Password": password.value})
        if response.status_code == 200:
            data = response.json()
            global_state.token = data['token']
            global_state.user_data = data['data']['user']
            global_state.user_type = data['data']['userType']
            page.snack_bar = ft.SnackBar(ft.Text("Inicio de sesión exitoso"), open=True)
            if global_state.user_type == "Audiencia":
                page.go("/menu_audiencia")
            elif global_state.user_type == "Artista":
                page.go("/menu_artista")
            start_token_renewal()
        else:
            page.snack_bar = ft.SnackBar(ft.Text(response.json().get('message', 'Error en el inicio de sesión')), open=True)

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

def renew_token():
    while True:
        time.sleep(1500)  # 25 minutes
        if global_state.token:
            response = requests.get(f"{API_BASE_URL}/refresh-token", headers={"Authorization": global_state.token})
            if response.status_code == 200:
                data = response.json()
                global_state.token = data['token']
                print("Token renovado")
            else:
                print("Error al renovar el token")

def start_token_renewal():
    thread = threading.Thread(target=renew_token)
    thread.daemon = True
    thread.start()

if __name__ == "__main__":
    ft.app(target=login_view)
