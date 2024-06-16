import flet as ft
import requests
from global_state import global_state

API_BASE_URL = "http://192.168.0.105:3000/api/v2/artista"

def be_artista_view(page):
    description_field = ft.TextField(label="Descripción General", multiline=True, max_length=250, width=400)
    error_text = ft.Text("", color="red")

    user_data = global_state.user_data
    token = global_state.token

    email = ft.TextField(label="Correo", width=300, value=user_data['Correo'], read_only=True)

    def submit_description(e):
        description = description_field.value
        if not description:
            error_text.value = "La descripción no puede estar vacía"
            page.update()
            return

        headers = {'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'}
        payload = {'Correo': email.value, 'DescripcionGeneral': description}

        try:
            response = requests.post(API_BASE_URL, json=payload, headers=headers)
            if response.status_code == 201:
                page.snack_bar = ft.SnackBar(ft.Text("Artista creado exitosamente"), open=True)
                page.go("/menu_audiencia")
            else:
                result = response.json()
                error_text.value = result.get("message", "Error al crear el artista")
                page.update()
        except requests.RequestException as e:
            error_text.value = f"Error de conexión: {e}"
            page.update()

    page.views.clear()
    page.views.append(
        ft.View(
            "/be_artist",
            [
                ft.Column(
                    [
                        ft.Text("Crear Artista", size=30),
                        email,
                        description_field,
                        error_text,
                        ft.ElevatedButton("Enviar", on_click=submit_description),
                        ft.ElevatedButton("Regresar", on_click=lambda _: page.go("/menu_audiencia"))
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                )
            ]
        )
    )
    page.update()

if __name__ == "__main__":
    ft.app(target=be_artista_view)
