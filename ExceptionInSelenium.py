from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException, NoSuchElementException, StaleElementReferenceException, NoSuchWindowException, TimeoutException


import time

driver = webdriver.Chrome()

try:
    driver.get("https://www.google.com")

    #example1: handling NoSuchElementException
    try:
        driver.find_element(By.ID, "non_existent_id")
    except NoSuchElementException:
        print("Element Not Found: NoSuchElementException caught")

    #example 2: Handling timeout exception
    try:
        driver.implicitly_wait(2)
        driver.find_element(By.NAME, 'q').send_keys("Selenium")
    except TimeoutException:
        print("Element took to long to open")

    #example 3: handling StaleElementReferenceException
    try:
        element = driver.find_element(By.NAME,'q')
        driver.refresh()
        element.send_keys("Python")
    except StaleElementReferenceException:
        print("Exception")
except WebDriverException as e:
    print(f"WebDriverException:{e}")

finally:
    print("c,losing Browser")
    driver.quit()
