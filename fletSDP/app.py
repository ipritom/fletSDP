from abc import abstractmethod
import flet as ft



class FletApp:
    def __init__(self, title=None) -> None:
        self.title = title

        if title == None:
            self.title = "fletSDP App Window"

        self.page : ft.Page = None

    @abstractmethod
    def views(self, page:ft.Page):
        '''
        Create View Class objects here in App class method
        '''
        pass
    
    @abstractmethod
    def app_presentaion(self):
        '''
        App Presentation Logic under this method
        '''
        pass

    def main(self, page:ft.Page):
        # assign page attribute to the class
        self.page = page
        # creating page  
        self.page.title = self.title
        self.views(self.page)
        self.app_presentaion()
        page.update()

    def run(self):
        ft.app(target=self.main)
