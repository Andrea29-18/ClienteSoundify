import flet as ft
import requests

# Configuración de la API
from dotenv import load_dotenv
import os
load_dotenv()
API_URL = os.getenv('API_URL')

def create_artist_page(page: ft.Page, profile_setting_page, user_object):
    page.title = "Crear Artista"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.START

    correo = ft.TextField(label="Correo", value=user_object.get('Correo'))
    descripcion = ft.TextField(label="Descripción General")
    mensaje_creacion = ft.Text()

    def create_artist(e):
        new_data = {
            "Correo": correo.value,
            "DescripcionGeneral": descripcion.value
        }

        try:
            token = user_object.get('token')
            headers = {
                "Authorization": f"Bearer {token}",
                "Content-Type": "application/json"
            }

            response = requests.post(
                f'{API_URL}/artista',
                json=new_data,
                headers=headers
            )

            if response.status_code == 201:
                response_data = response.json()
                artist = response_data.get('data').get('artist')
                mensaje_creacion.value = "Artista creado correctamente"
                mensaje_creacion.color = "green"
                # Aquí podrías hacer algo con el objeto del artista creado si lo necesitas
            else:
                mensaje_creacion.value = f"Error: {response.status_code} {response.json().get('message')}"
                mensaje_creacion.color = "red"
            
        except requests.exceptions.RequestException as err:
            mensaje_creacion.value = f"Error al conectar con la API: {err}"
            mensaje_creacion.color = "red"
        
        mensaje_creacion.update()

    boton_volver = ft.ElevatedButton(text="Volver", on_click=lambda e: page.clean() or profile_setting_page(page, profile_setting_page, user_object))

    page.add(
        ft.Column(
            [
                correo,
                descripcion,
                ft.ElevatedButton(text="Crear Artista", on_click=create_artist),
                mensaje_creacion,
                boton_volver
            ],
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.START,
            spacing=20
        )
    )
