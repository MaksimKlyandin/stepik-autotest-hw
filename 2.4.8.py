import os
import time 
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()
browser.get(link)




price = WebDriverWait(browser, 15).until(
    EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
 
button = browser.find_element(By.CSS_SELECTOR, "button").click()
 





def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
  
x = int(browser.find_element(By.CSS_SELECTOR, "#input_value").text)
print(x, type(x))

y = calc(x)
print(y, type(y))

input = browser.find_element(By.CSS_SELECTOR, "input")
input.send_keys(y)

button = browser.find_element(By.CSS_SELECTOR, "#solve").click()

time.sleep(15)

browser.quit()


