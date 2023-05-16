from abc import abstractmethod
import flet as ft




class FletView:
    def __init__(self, page: ft.Page) -> None:
        self.page = page
        self.controls()

    @abstractmethod
    def layout(self):
        '''
        APP GUI Layout Code under this method
        '''
        pass

    @abstractmethod
    def controls(self):
        '''
        Flet Controls which will be resued in the app dynamically
        under this methid.
        '''
        pass

    def render(self, clean_render=True):
        '''
        Use this method to render the GUI to the user.
        '''
        # if recall_control == True:
        #     self.controls()
        
        if clean_render==True:
            self.page.clean()

        self.layout()
