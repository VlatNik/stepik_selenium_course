from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select
import os 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
  
try:
	browser = webdriver.Chrome()
	link = "http://suninjuly.github.io/explicit_wait2.html"
	browser.get(link)
	price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID,"price"), "$100"))
	button1 = browser.find_element(By.CSS_SELECTOR, "#book")
	button1.click()
	
	
	x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
	x = x_element.text
	y = calc(x)
	
	browser.find_element(By.CSS_SELECTOR, '#answer').send_keys(y)
	
	button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
	button.click()
	
	alert = browser.switch_to.alert
	print(alert.text)
	
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
	