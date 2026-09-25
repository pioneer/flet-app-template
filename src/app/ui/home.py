import flet as ft

from app.config import APP_NAME
from app.domain import readiness_message


def home_view() -> ft.SafeArea:
    return ft.SafeArea(
        ft.Column(
            controls=[
                ft.Image(src="icon.png", width=64, height=64),
                ft.Text(APP_NAME, size=24),
                ft.Text(readiness_message(ready=True)),
            ],
            spacing=16,
        )
    )
