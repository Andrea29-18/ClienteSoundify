import flet as ft

def favorites_view(page):
    def go_to_menu(e):
        page.go("/menu")
    
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
