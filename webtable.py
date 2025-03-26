from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.execute_script("window.location.href='https://cosmocode.io/automation-practice-webtable/';")
driver.maximize_window()
driver.execute_script('window.scrollTo(0,600)')
time.sleep(5)

table = driver.find_element(By.ID, "countries")
rows = table.find_elements(By.TAG_NAME,"tr")
row_count = len(rows)
print(row_count)

target_values = "Benin"
found = False

for row in rows:
    cells = row.find_elements(By.TAG_NAME, "td")
    for cell in cells:
        if target_values in cell.text:
            print(f"element found '{target_values}'")
            break
    if found:
        break
if not found:
    print(f"Element {target_values} is not present")