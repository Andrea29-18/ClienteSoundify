import flet as ft
import requests

def cargar_cancion_page(page: ft.Page):
    page.title = "Cargar Canción"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.START

    # Componentes de la UI para cargar una canción
    nombre_cancion = ft.TextField(label="Nombre de la Canción")
    idioma = ft.TextField(label="Idioma")
    artista = ft.TextField(label="Artista")
    album = ft.TextField(label="Álbum")
    audio_path = ft.TextField(label="Ruta del archivo de audio")
    mensaje_carga = ft.Text()

    # Función para manejar la carga de la canción
    def cargar_cancion(e):
        data = {
            "NombreCancion": nombre_cancion.value,
            "Idioma": idioma.value,
            "Artista": artista.value,
            "Album": album.value,
            "audioPath": audio_path.value
        }

        try:
            response = requests.post("http://localhost:3000/api/v2/cancion/", json=data)

            if response.status_code == 201:
                mensaje_carga.value = "Canción cargada exitosamente"
                mensaje_carga.color = "green"
            else:
                mensaje_carga.value = f"Error: {response.status_code} {response.json().get('message')}"
                mensaje_carga.color = "red"
        except requests.exceptions.RequestException as err:
            mensaje_carga.value = f"Error al conectar con la API: {err}"
            mensaje_carga.color = "red"

    boton_cargar = ft.ElevatedButton(text="Cargar Canción", on_click=cargar_cancion)
    boton_volver = ft.ElevatedButton(text="Volver", on_click=lambda e: page.clean())

    # Agregar componentes a la página de carga de canción
    page.add(
        ft.Column(
            [
                nombre_cancion,
                idioma,
                artista,
                album,
                audio_path,
                boton_cargar,
                mensaje_carga,
                boton_volver
            ],
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.START,
            spacing=20
        )
    )
