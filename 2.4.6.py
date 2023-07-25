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
	link = "http://suninjuly.github.io/cats.html"
	browser.get(link)
	browser.find_element(By.ID, "button")
	
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
	time.sleep(10)
    # закрываем браузер после всех манипуляций
	browser.quit()