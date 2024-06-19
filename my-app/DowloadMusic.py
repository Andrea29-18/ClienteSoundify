import os
import grpc
import flet as ft
import audio_pb2
import audio_pb2_grpc
from global_state import global_state

def download_audio(stub, file_name):
    request = audio_pb2.DownloadFileRequest(nombre=file_name)
    
    # Asegúrate de que el directorio 'downloaded_audio' exista
    os.makedirs("downloaded_audio", exist_ok=True)
    
    # Añade la extensión .mp3 si no está presente en el nombre del archivo
    if not file_name.endswith('.mp3'):
        file_name += '.mp3'
    
    file_path = os.path.join("downloaded_audio", file_name)
    
    try:
        with open(file_path, 'wb') as file:
            for response in stub.downloadAudio(request):
                if response.HasField('data'):
                    file.write(response.data)
        return file_path
    except grpc.RpcError as e:
        print(f"gRPC error: {e}")
        return None

def download_music_view(page):
    page.title = "gRPC Audio Downloader"
    
    file_name_input = ft.TextField(label="Nombre del archivo", width=300)
    result_text = ft.Text()

    def go_to_menu(e):
        if global_state.user_type == "Audiencia":
            page.go("/menu_audiencia")
        elif global_state.user_type == "Artista":
            page.go("/menu_artista")

    def download(file_name):
        channel = grpc.insecure_channel('localhost:3500')  # Cambia el puerto si es necesario
        stub = audio_pb2_grpc.AudioServiceStub(channel)
        file_path = download_audio(stub, file_name)
        if file_path:
            result_text.value = f"Archivo descargado: {file_path}"
        else:
            result_text.value = "Error al descargar el archivo."
        page.update()

    download_button = ft.ElevatedButton(text="Descargar", on_click=lambda _: download(file_name_input.value))

    page.add(file_name_input, download_button, result_text)

    page.views.clear()
    page.views.append(
        ft.View(
            "/download_music",
            [
                ft.Column(
                    [
                        ft.Text("Menú de Descargas", size=30),
                        ft.ElevatedButton("Regresar a Menú", on_click=go_to_menu),
                        file_name_input,
                        download_button,
                        result_text
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                )
            ]
        )
    )
    page.update()

if __name__ == "__main__":
    ft.app(target=download_music_view)
