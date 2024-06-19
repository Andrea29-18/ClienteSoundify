import flet as ft
import os
import random

assets_folder = "downloaded_audio"

songs = [f for f in os.listdir(assets_folder) if f.endswith('.mp3')]

if not songs:
    raise ValueError("No se encontraron canciones en la carpeta.")

# Función para obtener una canción aleatoria
def get_random_song():
    return random.choice(songs)

def listening_music_view(page):
    current_index = [0]

    def load_song(index):
        audio1.src = os.path.join(assets_folder, songs[index])
        audio1.update()
        audio1.play()
        
    def volume_down(_):
        audio1.volume = max(0, audio1.volume - 0.1)
        audio1.update()

    def volume_up(_):
        audio1.volume = min(1, audio1.volume + 0.1)
        audio1.update()

    def play_next_song(_):
        current_index[0] = (current_index[0] + 1) % len(songs)
        load_song(current_index[0])

    def play_previous_song(_):
        current_index[0] = (current_index[0] - 1) % len(songs)
        load_song(current_index[0])

    audio1 = ft.Audio(
        src=os.path.join(assets_folder, songs[current_index[0]]),
        autoplay=False,
        volume=1,
        balance=0,
    )
    page.overlay.append(audio1)

    page.views.clear()
    page.views.append(
        ft.View(
            "/listening_music",
            [
                ft.ElevatedButton("Play", on_click=lambda _: audio1.play()),
                ft.ElevatedButton("Pause", on_click=lambda _: audio1.pause()),
                ft.Row(
                    [
                        ft.ElevatedButton("Volume down", on_click=volume_down),
                        ft.ElevatedButton("Volume up", on_click=volume_up),
                    ]
                ),
                ft.Row(
                    [
                        ft.ElevatedButton("Previous", on_click=play_previous_song),
                        ft.ElevatedButton("Next", on_click=play_next_song),
                    ]
                ),
                ft.ElevatedButton("Regresar a Menú", on_click=lambda _: page.go("/menu_audiencia"))
            ]
        )
    )
    page.update()

if __name__ == "__main__":
    ft.app(target=listening_music_view)
