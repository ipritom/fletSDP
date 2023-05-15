from abc import abstractmethod
import flet as ft



class FletApp:
    def __init__(self, title=None) -> None:
        self.title = title

        if title == None:
            self.title = "fletSDP App Window"

    @abstractmethod
    def views(self, page:ft.Page):
        '''
        Create View Class objects here in App class method
        '''
        pass
    
    @abstractmethod
    def app_presentaion(self):
        '''
        App Presentaion Logic under this method
        '''
        pass

    def main(self, page:ft.Page):
        page.title = self.title
        self.views(page)
        self.app_presentaion()
        page.update()

    def run(self):
        ft.app(target=self.main)

   