
import flet as ft

from fletSDP.app import FletSDPApp

from light_page import LightView
from dark_page import DarkView


class App(FletSDPApp):
    
    def __init__(self, title=None) -> None:
        super().__init__(title)

    def views(self, page:ft.Page):
        self.light_page_view = LightView(self.page, updater=self.light_page_updater)
        self.dark_page_view = DarkView(self.page, updater=self.dark_page_updater)  
    
    def light_page_updater(self):
        self.light_page_view.light_btn.on_click = self.light_btn_click

    def dark_page_updater(self):
        self.dark_page_view.dark_btn.on_click = self.dark_btn_click

    def app_presentaion(self):
        self.light_page_view.render()
        
    def light_btn_click(self, e):
        self.page.theme_mode = "dark"
        self.dark_page_view.render()
       
    def dark_btn_click(self, e):
        self.page.theme_mode = "light"
        self.light_page_view.render()
    
        
# creating app object and running the app
app = App()
app.run()