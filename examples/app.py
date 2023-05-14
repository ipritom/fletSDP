
import flet as ft

from fletSDP.app import FletApp

from edit_page import EditView
from initial_page import InitialView

 
class App(FletApp):
    def main(self, page:ft.Page):
        self.page = page
        self.init_page = InitialView(page)
        self.edit_page = EditView(page)  
        self.app_presentaion()

    def app_presentaion(self):
        self.init_page.layout()
        self.init_page.test_btn.on_click = self.test_click
        self.edit_page.edit_btn.on_click = self.edit_click
        self.page.update()
    
    def test_click(self,e ):
        self.edit_page.layout()
        self.page.update()
    
    def edit_click(self,e ):
        self.init_page.layout()
        self.page.update()
        


app = App()

app.run()