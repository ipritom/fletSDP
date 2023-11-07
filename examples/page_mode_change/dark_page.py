import flet as ft
from fletSDP.views import FletView

class DarkView(FletView):
    def __init__(self, page: ft.Page, updater) -> None:
        super().__init__(page, updater)

    def controls(self):
        self.dark_btn = ft.ElevatedButton("LIGHT")
    
    def layout(self):
        self.page.add(
            ft.Row(
                [
                    ft.Container(
                    content= self.dark_btn,
                    alignment=ft.alignment.center, 
                    expand=True
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                expand=True
            )
        )
        