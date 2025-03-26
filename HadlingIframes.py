#https://the-internet.herokuapp.com/iframe
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


browser = webdriver.Chrome()
browser.maximize_window()
browser.get("https://the-internet.herokuapp.com/iframe")

iframe = browser.find_element(By.ID,'mce_0_ifr')
browser.switch_to.frame(iframe)

text_editor = browser.find_element(By.ID, 'tinymce')
#text_editor.clear()
text_editor.send_keys("This is selenium")
time.sleep(5)
browser.switch_to.default_content()

Selenium_link = browser.find_element(By.XPATH,"//a[normalize-space()='Elemental Selenium']")
Selenium_link.click()
