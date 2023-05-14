import flet as ft
from fletSDP.views import FletView

class EditView(FletView):
    def __init__(self, page: ft.Page) -> None:
        super().__init__(page)

    def controls(self):
        self.edit_btn = ft.ElevatedButton("EDIT")
    
    def layout(self):
        self.page.clean()
        self.page.add(
            ft.Row(
                [
                    self.edit_btn
                ]
            )
        )