import flet as ft
import requests
from global_state import global_state
from decouple import config

API_BASE_URL = config('API_URL')

def create_album_view(page):
    # Obtener la lista de géneros musicales disponibles desde la API
    response = requests.get(f"{API_BASE_URL}/genero")
    if response.status_code == 200:
        generos = response.json().get('data', {}).get('generos', [])
        options = [(genero['_id'], genero['NombreGenero']) for genero in generos]
    else:
        options = []

    genero_musical = ft.Dropdown(label="Género Musical", width=300, options=options)

    nombre_album = ft.TextField(label="Nombre del Álbum", width=300)
    descripcion = ft.TextField(label="Descripción", width=300)
    genero_musical = ft.Dropdown(label="Género Musical", width=300, options=options)

    def create_album(e):
        data = {
            "NombreAlbum": nombre_album.value,
            "Descripcion": descripcion.value,
            "ArtistaNombre": global_state.user_data.get('NombreUsuario', ''),
            "GeneroMusical": genero_musical.value
        }
        headers = {"Authorization": f"Bearer {global_state.token}"}
        response = requests.post(f"{API_BASE_URL}/album", json=data, headers=headers)
        if response.status_code == 201:
            page.snack_bar = ft.SnackBar(ft.Text("Álbum creado exitosamente"), open=True)
        else:
            page.snack_bar = ft.SnackBar(ft.Text("Error al crear el álbum"), open=True)

    def go_back(e):
        page.go("/menu_artista" if global_state.user_type == "Artista" else "/menu_audiencia")

    page.views.clear()
    page.views.append(
        ft.View(
            "/create_album",
            [
                ft.Column(
                    [
                        ft.Text("Crear Álbum", size=30),
                        nombre_album,
                        descripcion,
                        genero_musical,
                        ft.ElevatedButton("Crear", on_click=create_album),
                        ft.ElevatedButton("Regresar", on_click=go_back)
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                )
            ]
        )
    )
    page.update()

if __name__ == "__main__":
    ft.app(target=create_album_view)
