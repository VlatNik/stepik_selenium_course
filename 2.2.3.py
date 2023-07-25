from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select

try:
	browser = webdriver.Chrome()
	browser.get("http://suninjuly.github.io/selects1.html")	
	
	x = browser.find_element(By.CSS_SELECTOR, '#num1').text
	y = browser.find_element(By.CSS_SELECTOR, '#num2').text
	
	z = int(x)+int(y)
	print(str(z))
	select = Select(browser.find_element(By.CSS_SELECTOR, "#dropdown"))
	select.select_by_visible_text(str(z)) # ищем элемент с текстом "Python"
	
	browser.find_element(By.CSS_SELECTOR, '[type=submit]').click()
	
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()