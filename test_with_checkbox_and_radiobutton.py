from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = 'http://suninjuly.github.io/math.html'
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element(By.CSS_SELECTOR, '#answer')
    input1.send_keys(y)
    time.sleep(3)

    option1 = browser.find_element(By.CSS_SELECTOR, '#robotCheckbox')
    option1.click()
    time.sleep(3)

    option2 = browser.find_element(By.CSS_SELECTOR, '#robotsRule')
    option2.click()
    time.sleep(3)

    submit_button = browser.find_element(By.TAG_NAME, 'button')
    submit_button.click()

finally:
    time.sleep(10)
    browser.quit()