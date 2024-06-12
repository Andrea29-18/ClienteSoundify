import flet as ft

def menu_artista_view(page):
    def go_to_favorites(e):
        page.go("/favorites")
    
    def go_to_settings(e):
        page.go("/settings_artist")

    def go_to_create_album(e):
        page.go("/create_album")
    
    def upload_song(e):
        # Implementar la lógica para cargar una canción
        page.snack_bar = ft.SnackBar(ft.Text("Funcionalidad para cargar una canción aún no implementada"), open=True)
    
    def logout(e):
        page.go("/")

    page.views.clear()
    page.views.append(
        ft.View(
            "/menu_artista",
            [
                ft.Column(
                    [
                        ft.Text("Menú de Artista", size=30),
                        ft.ElevatedButton("Crear Álbum", on_click=go_to_create_album),
                        ft.ElevatedButton("Cargar Canción", on_click=upload_song),
                        ft.ElevatedButton("Favoritos", on_click=go_to_favorites),
                        ft.ElevatedButton("Configuración", on_click=go_to_settings),
                        ft.ElevatedButton("Cerrar Sesión", on_click=logout)
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                )
            ]
        )
    )
    page.update()

if __name__ == "__main__":
    ft.app(target=menu_artista_view)
