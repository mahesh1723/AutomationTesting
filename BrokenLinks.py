import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#initialize the web browser
driver = webdriver.Chrome()
driver.get("https://interviewbit.com/software-testing-interview-questions/")

links = driver.find_elements(By.TAG_NAME,'a')
print(f"Total links founds {len(links)}")

for link in links:
    url = link.get_attribute("href")
    if url:
        try:
            response = requests.head(url, allow_redirects=True, timeout=5)
            if response.status_code >= 400:
                print(f"Link broken{url}")
                print(len(url))
        except requests.exceptions.RequestException as e:
            print("Error Checking:{url} ({e})")