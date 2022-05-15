from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = 'http://suninjuly.github.io/redirect_accept.html'
    browser = webdriver.Chrome()
    browser.get(link)

    # Жмем на кнопку

    browser.find_element(By.CSS_SELECTOR, 'button.trollface').click()

    # Переходим на новое окно

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    # Решаем пример и кликаем на Submit

    x = browser.find_element(By.CSS_SELECTOR, '#input_value').text
    browser.find_element(By.CSS_SELECTOR, '#answer').send_keys(calc(x))
    browser.find_element(By.CSS_SELECTOR, 'button').click()

finally:
    time.sleep(10)
    browser.quit()