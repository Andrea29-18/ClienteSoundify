import flet as ft

def menu_audiencia_view(page):
    def go_to_favorites(e):
        page.go("/favorites")
    
    def go_to_settings(e):
        page.go("/settings")

    def go_to_listener_music(e):
        page.go("/listening_music")

    def go_to_download_music(e):
        page.go("/download_music")
    
    def logout(e):
        page.go("/")

    page.views.clear()
    page.views.append(
        ft.View(
            "/menu_audiencia",
            [
                ft.Column(
                    [
                        ft.Text("Menú de Audiencia", size=30),
                        ft.ElevatedButton("Favoritos", on_click=go_to_favorites),
                        ft.ElevatedButton("Configuración", on_click=go_to_settings),
                        ft.ElevatedButton("Escuchar Música", on_click=go_to_listener_music),
                        ft.ElevatedButton("Descargar Música", on_click=go_to_download_music),
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
    ft.app(target=menu_audiencia_view)
