import flet as ft
from views import Views, FletView

    
class InitialView(FletView):
    def __init__(self, global_views_object) -> None:
        super().__init__(global_views_object)
        self.controls = InitialControl()
    
    def get_view(self, page: ft.Page):
        page.clean()
        page.add(
            ft.Row(
                [
                    self.controls.test_btn
                 
                ]
            )
        )

class InitialControl:
    def __init__(self) -> None:
        self.test_btn = ft.ElevatedButton("TEST")

class EditView(FletView):
    def __init__(self, global_views_object) -> None:
        super().__init__(global_views_object)
        
    
    
    def get_view(self, page: ft.Page):
        page.clean()
        print(self)
        page.add(
            ft.Row(
                [
                    
                 
                ]
            )
        )
    def on_click_test(self):
        # self.global_views_object.
        pass

class AppViews(Views):
    def __init__(self) -> None:
        super().__init__()
        self.initial_page = InitialView(self)
        self.edit_page = EditView(self)

        self.control_on_click()
        
    def control_on_click(self):
        self.initial_page.controls.test_btn.on_click = self.on_click_test

    def on_click_test(self, e):
        self.edit_page.get_view(self.page)

class App:
    def main(self, page:ft.Page):
        # explain view logic here
        app_views = AppViews()
        app_views.initial_page.get_view(page)
        app_views.initial_page 
        page.update()

    def run(self):
        ft.app(target=self.main)



app = App()

app.run()