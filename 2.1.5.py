from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
  
try: 
	
	browser = webdriver.Chrome()
	browser.get("http://suninjuly.github.io/get_attribute.html")

    # Ваш код, который заполняет обязательные поля
	x_element = browser.find_element(By.CSS_SELECTOR, '#treasure')
	x = x_element.get_attribute("valuex")
	print(x)
	y = calc(x)
	browser.find_element(By.CSS_SELECTOR, '#answer').send_keys(y)
	browser.find_element(By.CSS_SELECTOR, '#robotCheckbox').click()
	browser.find_element(By.CSS_SELECTOR, '#robotsRule').click()
	browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()
	
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()