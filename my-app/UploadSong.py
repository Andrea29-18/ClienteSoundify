import flet as ft
import requests
import os
from global_state import global_state
API_BASE_URL = "http://192.168.0.105:3000/api/v2/cancion"

def upload_song_view(page):
    token = global_state.token
    user_data = global_state.user_data
    
    nombre_cancion = ft.TextField(label="Nombre de Canción", width=400)
    idioma = ft.TextField(label="Idioma", width=400)
    artista = ft.TextField(label="Artista", width=400, value=user_data['NombreArtista'])
    album = ft.TextField(label="Álbum", width=400)
    audio_path = ft.Text("Seleccionar Archivo de Audio", width=400)
    error_text = ft.Text("", color="red")
    success_text = ft.Text("", color="green")
    
    file_picker = ft.FilePicker(
        on_result=lambda e: on_file_selected(e)
    )

    def on_file_selected(e):
        if e.files and e.files[0].name.endswith('.mp3'):
            audio_path.value = e.files[0].path
            success_text.value = "Archivo cargado correctamente"
            error_text.value = ""
        else:
            audio_path.value = ""
            success_text.value = ""
            error_text.value = "Solo se permiten archivos .mp3"
        page.update()

    def submit_song(e):
        if not nombre_cancion.value or not idioma.value or not artista.value or not album.value or not audio_path.value:
            error_text.value = "Todos los campos son obligatorios"
            success_text.value = ""
            page.update()
            return

        file_path = audio_path.value

        if not file_path:
            error_text.value = "Debe seleccionar un archivo de audio"
            success_text.value = ""
            page.update()
            return
        
        with open(file_path, 'rb') as f:
            form_data = {
                'NombreCancion': nombre_cancion.value,
                'Idioma': idioma.value,
                'Artista': artista.value,
                'Album': album.value
            }
            files = {'audio': (os.path.basename(file_path), f, 'audio/mpeg')}
            response = requests.post(
                API_BASE_URL,
                data=form_data,
                files=files
            )

            if response.status_code == 201:
                page.snack_bar = ft.SnackBar(ft.Text("Canción creada y archivo de audio subido exitosamente"), open=True)
                page.go("/menu_artista")
            else:
                error_text.value = response.json().get('message', 'Error al crear la canción')
                success_text.value = ""
                page.update()

    page.views.clear()
    page.views.append(
        ft.View(
            "/upload_song",
            [
                ft.Column(
                    [
                        ft.Text("Subir Canción", size=30),
                        nombre_cancion,
                        idioma,
                        artista,
                        album,
                        ft.Row([audio_path, ft.ElevatedButton("Seleccionar", on_click=lambda _: file_picker.pick_files(allow_multiple=False))]),
                        success_text,
                        error_text,
                        ft.ElevatedButton("Subir", on_click=submit_song),
                        ft.ElevatedButton("Regresar", on_click=lambda _: page.go("/menu_artista"))
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                ),
                file_picker  # Asegúrate de agregar el file_picker al árbol de widgets
            ]
        )
    )
    page.update()

if __name__ == "__main__":
    ft.app(target=upload_song_view)
