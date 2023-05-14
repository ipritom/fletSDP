import flet as ft
from fletSDP.views import FletView

class InitialView(FletView):
    def __init__(self, page: ft.Page) -> None:
        super().__init__(page)

    def controls(self):
        self.test_btn = ft.ElevatedButton("TEST")
    

    def layout(self):
        self.page.clean()
        self.page.add(
            ft.Row(
                [
                    self.test_btn
                ]
            )
        )