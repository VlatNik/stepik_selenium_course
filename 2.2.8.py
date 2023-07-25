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
	link = "http://suninjuly.github.io/file_input.html"
	browser.get(link)

	browser.find_element(By.CSS_SELECTOR, "[name = 'firstname']").send_keys("Vladislav")
	browser.find_element(By.CSS_SELECTOR, "[name = 'lastname']").send_keys("Nik")
	browser.find_element(By.CSS_SELECTOR, "[name = 'email']").send_keys("vl.nik@gmail.ru")
	current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
	file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
	element = browser.find_element(By.CSS_SELECTOR, "[type = 'file']")
	element.send_keys(file_path)
	button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
	button.click()
	
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()