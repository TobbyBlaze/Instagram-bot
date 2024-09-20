from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

from connected import Connected

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException

class Login(Screen):
    def do_login(self, emailText, passwordText, commentText):
        app = App.get_running_app()

        app.email = emailText
        app.password = passwordText
        app.comment = commentText

        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'connected'

        # print(app.email)

        global driver
        chrome_options = Options()
        chrome_options.add_argument('--disable-notifications')
        driver = webdriver.Chrome(options=chrome_options)

        # actions = ActionChains(driver)

        # driver.implicitly_wait(10)
        
        

        driver.get("https://www.instagram.com")
        
        
        # driver.find_element_by_xpath('//*[@id="uc-btn-accept-banner"]').click()
        # driver.find_element("xpath", '//*[@id="uc-btn-accept-banner"]').click()

        # WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="uc-btn-accept-banner"]'))).click()

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Allow all cookies']"))).click()

        # WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#loginForm > div > div:nth-child(3) > button"))).click()  
        # WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Save Info']"))).click()
        # WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Turn On']"))).click()

        '''
        print('Printing cookies')
        print(driver.get_cookies())
        print('Done')
        driver.implicitly_wait(0.5)
        '''

        driver.implicitly_wait(1)

        email_box = driver.find_element(by=By.NAME, value="username")
        email_box.send_keys(app.email)
        driver.implicitly_wait(0.5)

        password_box = driver.find_element(by=By.NAME, value="password")
        password_box.send_keys(app.password)
        driver.implicitly_wait(2)

        submit_button = driver.find_element("xpath", "//button[@type='submit']")
        submit_button.click()

        driver.implicitly_wait(2)

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[text()='Not now']"))).click()

        driver.implicitly_wait(2)

        actions = ActionChains(driver)
        driver.implicitly_wait(2)
        #comment_box = driver.find_element(by=By.CSS_SELECTOR, value="textarea")
        driver.implicitly_wait(1)
        print('Comment start')
        print(app.comment)
        print('Comment ends')
        #comment_box.send_keys(app.comment)

        ignored_exceptions=(NoSuchElementException,StaleElementReferenceException,)

        comment_box = WebDriverWait(driver, 10, ignored_exceptions=ignored_exceptions).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "textarea.x1i0vuye")))
        driver.execute_script("arguments[0].scrollIntoView(true);", comment_box)
        comment_box.send_keys(app.comment)
        
        '''
        actions.send_keys(Keys.TAB)
        actions.send_keys(Keys.ARROW_DOWN)
        actions.send_keys(Keys.ARROW_DOWN)
        actions.send_keys(Keys.ARROW_DOWN)
        actions.send_keys(Keys.ARROW_DOWN)
        actions.send_keys(Keys.ARROW_DOWN)
        actions.send_keys(Keys.ENTER)
        actions.send_keys(app.comment)
        actions.send_keys(Keys.ENTER)
        actions.send_keys(Keys.ARROW_DOWN)
        actions.send_keys(Keys.ARROW_DOWN)
        actions.perform()
        driver.implicitly_wait(0.5)
        '''

        '''
        while True:
            driver.implicitly_wait(2)
            comment_box = driver.find_element(by=By.CSS_SELECTOR, value="textarea")
            driver.implicitly_wait(1)
            print('Comment start')
            print(app.comment)
            print('Comment ends')
            #comment_box.send_keys(app.comment)
            actions.send_keys(app.comment)
            driver.implicitly_wait(0.5)

            #comment_box.send_keys(Keys.ARROW_DOWN)
        '''
        

        # submit_button = driver.find_element("xpath", "//a[contains(text(), 'Log in')]")
        # submit_button = driver.find_element(by=By.CLASS_NAME, value="x1nhvcw1")
        # submit_button = driver.find_element_by_xpath("//a[contains(text(), 'Log in')]")
        # x9f619 xjbqb8w x78zum5 x168nmei x13lgxp2 x5pf9jr xo71vjh x1n2onr6 x1plvlek xryxfnj x1c4vz4f x2lah0s xdt5ytf xqjyukv x1qjc9v5 x1oa3qoh x1nhvcw1
        # submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")
        # submit_button = driver.find_element_by_css_selector("[type='submit']")
        # submit_button.click()
        # print(submit_button)

        # app.config.read(app.get_application_config())
        # app.config.write()

    def resetForm(self):
        self.ids['email'].text = ""
        self.ids['password'].text = ""
        self.ids['comment'].text = ""

    def change(self):
        self.manager.transition = SlideTransition(direction="up")
        self.manager.current = 'login'
        self.background_color =(1, 1, 1, 1)
        print('Seen')

class LoginApp(App):
    email = StringProperty(None)
    password = StringProperty(None)

    def build(self):
        manager = ScreenManager()

        manager.add_widget(Login(name='login'))
        manager.add_widget(Connected(name='connected'))

        return manager

    '''
    Figure this out later
    def get_application_config(self):
        if(not self.email):
            return super(LoginApp, self).get_application_config()

        conf_directory = self.user_data_dir + '/' + self.email

        if(not os.path.exists(conf_directory)):
            os.makedirs(conf_directory)

        return super(LoginApp, self).get_application_config(
            '%s/config.cfg' % (conf_directory)
        )
    '''

if __name__ == '__main__':
    LoginApp().run()