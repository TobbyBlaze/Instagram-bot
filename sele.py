from selenium import webdriver


driver = webdriver.Chrome()

driver.get("http://selenium.dev")

driver.implicitly_wait(0.5)

title = driver.title
assert title == "Web form"

text_box = driver.find_element(by=By.NAME, value="my-text")
submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

text_box.send_keys("Selenium")
submit_button.click()

message = driver.find_element(by=By.ID, value="message")

driver.quit()