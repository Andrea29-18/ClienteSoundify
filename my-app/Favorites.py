import flet as ft
from global_state import global_state


def favorites_view(page):
    def go_to_menu(e):
        if global_state.user_type == "Audiencia":
            page.go("/menu_audiencia")
        elif global_state.user_type == "Artista":
            page.go("/menu_artista")
    
    page.views.clear()
    page.views.append(
        ft.View(
            "/favorites",
            [
                ft.Column(
                    [
                        ft.Text("Favoritos", size=30),
                        ft.ElevatedButton("Regresar a Menú", on_click=go_to_menu)
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                )
            ]
        )
    )
    page.update()

if __name__ == "__main__":
    ft.app(target=favorites_view)
