import flet as ft
from fletSDP.views import FletView

class LightView(FletView):
    def __init__(self, page: ft.Page, updater) -> None:
        super().__init__(page, updater)

    def controls(self):
        self.light_btn = ft.ElevatedButton("DARK")
    
    def layout(self):
        self.page.add(
            ft.Row(
                [
                    ft.Container(
                    content= self.light_btn,
                    alignment=ft.alignment.center, 
                    expand=True
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                expand=True
            )
        )