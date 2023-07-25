from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
  
try:
	browser = webdriver.Chrome()
	link = "https://suninjuly.github.io/execute_script.html"
	browser.get(link)

	x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
	x = x_element.text
	y = calc(x)
	browser.find_element(By.CSS_SELECTOR, '#answer').send_keys(y)
	
	browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']").click()
	el = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")
	browser.execute_script("return arguments[0].scrollIntoView(true);", el)
	browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']").click()
	button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
	browser.execute_script("return arguments[0].scrollIntoView(true);", button)
	button.click()
	
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()