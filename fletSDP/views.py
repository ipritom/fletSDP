from abc import abstractmethod
import flet as ft




class FletView:
    def __init__(self, page: ft.Page) -> None:
        self.page = page
        self.controls()

    @abstractmethod
    def layout(self):
        pass

    @abstractmethod
    def controls():
        pass
