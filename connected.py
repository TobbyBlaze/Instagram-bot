from kivy.app import App
from kivy.uix.screenmanager import Screen, SlideTransition

from selenium import webdriver

class Connected(Screen):
    def disconnect(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'login'
        self.manager.get_screen('login').resetForm()

        driver = webdriver.Chrome()

        driver.quit()

    def change(self):
        self.manager.transition = SlideTransition(direction="up")
        self.manager.current = 'login'

    def comment(self, emailText, passwordText, commentText):
        print(emailText)
        '''
        global driver
        driver = webdriver.Chrome()

        driver.get("https://www.instagram.com")
        driver.implicitly_wait(0.5)

        email_box = driver.find_element(by=By.NAME, value="username")
        email_box.send_keys("Selenium")
        driver.implicitly_wait(0.5)

        password_box = driver.find_element(by=By.NAME, value="password")
        password_box.send_keys("Selenium")
        driver.implicitly_wait(0.5)

        submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")
        '''

        