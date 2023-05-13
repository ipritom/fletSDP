import flet as ft
class Views:
    def __init__(self) -> None:
        pass


class FletView:
    def __init__(self, global_views_object) -> None:
        self.global_views_object: Views = global_views_object
    
    def get_view(self, page: ft.Page):
        pass
