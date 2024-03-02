from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time

def scrapeImages(item, itemAmount):
    driver = webdriver.Chrome()
    driver.maximize_window()
    wait = WebDriverWait(driver, 3)

    driver.get(f"https://www.google.com/search?sca_esv=302ce67c0d679abb&sxsrf=ACQVn0_6LULGAaSbclrGccgQ3wWFAHjAIQ:1709403891992&q={item}&tbm=isch&source=lnms&sa=X&ved=2ahUKEwiF0InemdaEAxVwrokEHegFDeAQ0pQJegQIDRAB&biw=1707&bih=825&dpr=1.5")
    for i in range(itemAmount):
        try:
            itemImage = wait.until(EC.presence_of_element_located((By.XPATH, f'(//div[@role="list"])/*[{i+2}]/*/*/*'))).get_attribute('src')
            scrollTo = driver.find_element(By.XPATH, value=f'(//div[@role="list"])/*[{i+2}]/*/*/*')
            driver.execute_script("arguments[0].scrollIntoView();", scrollTo)
            print(itemImage)
        except Exception:
            print('no')
    
    time.sleep(10)

x = input('What would you like to detect?     ')
scrapeImages(x, 100)
