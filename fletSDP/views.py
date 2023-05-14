from abc import ABC, abstractmethod
import flet as ft

class AbstractView(ABC):
    @abstractmethod
    def get_view(self):
        pass

    @abstractmethod
    def controls():
        pass

class Views:
    def __init__(self) -> None:
        pass


class FletView(AbstractView):
    def __init__(self, page) -> None:
        self.page = page
        self.controls()
    
    def get_view(self, page: ft.Page):
        pass

    def controls():
        pass
