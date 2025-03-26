import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://interviewbit.com/software-testing-interview-questions/")

images = driver.find_elements(By.TAG_NAME,'img')
print(f"Total Broken Found {len(images)}")

for img in images:
    img_url = img.get_attribute("src")
    if img_url:
        response = requests.head(img_url, allow_redirects=True, timeout=5)
        if response.status_code >=400:
            print(f"Broken Images {len(img_url)}")