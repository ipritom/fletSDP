from abc import abstractmethod
import flet as ft

class FletView:
    def __init__(self, page: ft.Page, updater=None) -> None:
        """
        FletView Parameters
        """
        self.page = page
        self.update_control_function = updater
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

    def render(self, clean_render=True, clean_controls=True):
        '''
        Use this method to render the GUI to the user.
        '''
        if clean_render==True:
            self.page.clean()

        if clean_controls==True:
            self.controls()
            
        if self.update_control_function !=None:
            self.update_control_function()
        
        self.layout()
        self.page.update()
