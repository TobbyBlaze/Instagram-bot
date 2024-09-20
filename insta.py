from kivy.app import App
from kivy.uix.gridlayout import GridLayout
#from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

from selenium import webdriver


class LoginScreen(GridLayout):

    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 3

        self.add_widget(Label(text='User Name'))
        self.email = TextInput(multiline=False)
        self.add_widget(self.email)

        self.add_widget(Label(text='password'))
        self.password = TextInput(password=False, multiline=False)
        self.add_widget(self.password)

        
        #if
        driver = webdriver.Chrome()

        driver.get("https://www.instagram.com")

        #driver.implicitly_wait(0.5)

        


class MyApp(App):

    def build(self):
        self.title = "Insta bot"
        return LoginScreen()


if __name__ == '__main__':
    MyApp().run()