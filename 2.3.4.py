from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select
import os 

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
  
try:
	browser = webdriver.Chrome()
	link = "http://suninjuly.github.io/alert_accept.html"
	browser.get(link)

	browser.find_element(By.CSS_SELECTOR, "[type = 'submit']").click()
	alert = browser.switch_to.alert
	alert.accept()
	
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