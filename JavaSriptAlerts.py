from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#from HadlingIframes import browser

a = webdriver.Chrome()
a.maximize_window()
a.get('https://the-internet.herokuapp.com/javascript_alerts')

AlertButton = a.find_element(By.XPATH,"//button[normalize-space()='Click for JS Alert']")

AlertButton.click()

alert = a.switch_to.alert
alert_text = alert.text

print(alert_text)
alert.accept()

time.sleep(5)

AlertButton = a.find_element(By.XPATH,"//button[normalize-space()='Click for JS Confirm']")

AlertButton.click()

alert = a.switch_to.alert
alert_text = alert.text

print(alert_text)
alert.dismiss()
time.sleep(5)



AlertButton = a.find_element(By.XPATH,"//button[normalize-space()='Click for JS Prompt']")

AlertButton.click()

alert = a.switch_to.alert
alert_text = alert.text

print(alert_text)
alert.send_keys("Hi")
alert.dismiss()
time.sleep(5)