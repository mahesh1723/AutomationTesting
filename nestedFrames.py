from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.maximize_window()
browser.get('https://the-internet.herokuapp.com/nested_frames')

# switching to top frames

browser.switch_to.frame("frame-top")

#switching to Middle Frame
browser.switch_to.frame("frame-middle")

content = browser.find_element(By.ID, 'content').text
print("Content in Middle is: ", content)

#switch to Default content
browser.switch_to.default_content()

#switch to the bottom frame
browser.switch_to.frame("frame-bottom")
content1 = browser.find_element(By.TAG_NAME, "body").text
print("Content in the bottom is: ", content1)
