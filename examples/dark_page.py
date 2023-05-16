import flet as ft
from fletSDP.views import FletView

class DarkView(FletView):
    def __init__(self, page: ft.Page) -> None:
        super().__init__(page)

    def controls(self):
        self.dark_btn = ft.ElevatedButton("LIGHT")
        self.d = 0
        print(self.d)
    
    def layout(self):
        # self.page.clean()
        print(__name__, "layout serving...")
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
        