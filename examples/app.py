
import flet as ft

from fletSDP.app import FletApp

from light_page import LightView
from dark_page import DarkView


class App(FletApp):
    
    def __init__(self, title=None) -> None:
        super().__init__(title)

    def views(self, page:ft.Page):
        self.light_page_view = LightView(self.page)
        self.dark_page_view = DarkView(self.page)  
        
    def app_presentaion(self):
        self.light_page_view.render()
        self.light_page_view.light_btn.on_click = self.light_btn_click
        self.dark_page_view.dark_btn.on_click = self.dark_btn_click
       
    def light_btn_click(self, e):
        self.page.theme_mode = "dark"
        self.dark_page_view.render()
       
    def dark_btn_click(self, e):
        self.page.theme_mode = "light"
        self.light_page_view.render()
    
        
# creating app object and running the app
app = App()
app.run()