
import flet as ft

from fletSDP.app import FletApp

from edit_page import EditView
from initial_page import InitialView

 
class App(FletApp):
    def __init__(self, title=None) -> None:
        super().__init__(title)

    def views(self, page:ft.Page):
        self.page = page
        self.init_page = InitialView(page)
        self.edit_page = EditView(page)  
 
    def app_presentaion(self):
        self.init_page.layout()
        self.init_page.test_btn.on_click = self.test_click
        self.edit_page.edit_btn.on_click = self.edit_click
       
    
    def test_click(self, e):
        self.edit_page.layout()
        self.page.update()
    
    def edit_click(self, e):
        self.init_page.layout()
        self.page.update()
        


app = App()

app.run()