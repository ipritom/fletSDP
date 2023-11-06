import flet as ft
from fletSDP.app import FletSDPApp

from views.login_view import LoginView
from views.register_view import RegisterView


class App(FletSDPApp):
    
    def __init__(self, title=None) -> None:
        super().__init__(title)

    def views(self, page:ft.Page):
        self.login_page = LoginView(page)
        self.registration_page = RegisterView(page)
    
    def go_registration_page(self):
        self.registration_page.render()

    def pre_config_buttons(self):
        self.login_page.register_page_button.on_click = lambda e: self.go_registration_page()
        self.registration_page.login_page_button.on_click = lambda e:self.login_page.render()
   

    def app_presentaion(self):
        self.pre_config_buttons()
        self.login_page.render()
        # self.light_page_view.light_btn.on_click = self.light_btn_click
        # self.dark_page_view.dark_btn.on_click = self.dark_btn_click

    def run(self):
        # ft.app(target=main, host=host_ip, port=host_port, view=ft.WEB_BROWSER, upload_dir="uploads", assets_dir="uploads")
        ft.app(target=self.main, view=ft.WEB_BROWSER, upload_dir="uploads", assets_dir="uploads")



app = App(title="FIME")
app.run()
