from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = 'http://suninjuly.github.io/alert_accept.html'
    browser = webdriver.Chrome()
    browser.get(link)

    # Кликаем на кнопку

    browser.find_element(By.CSS_SELECTOR, 'button.btn').click()
    time.sleep(2)

    # Ассептим появляющееся Alert-окно

    browser.switch_to.alert.accept()
    time.sleep(2)

    # Решаем пример и нажимаем на Submit

    x = browser.find_element(By.CSS_SELECTOR, '#input_value').text
    browser.find_element(By.CSS_SELECTOR, '#answer').send_keys(calc(x))
    browser.find_element(By.CSS_SELECTOR, 'button').click()

finally:
    time.sleep(10)
    browser.quit()