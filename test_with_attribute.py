from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = 'http://suninjuly.github.io/get_attribute.html'
    browser = webdriver.Chrome()
    browser.get(link)

    treasure_element = browser.find_element(By.CSS_SELECTOR, '#treasure')
    x = treasure_element.get_attribute('valuex')

    browser.find_element(By.CSS_SELECTOR, '#answer').send_keys(calc(x))
    time.sleep(1)
    browser.find_element(By.CSS_SELECTOR, '#robotCheckbox').click()
    time.sleep(1)
    browser.find_element(By.CSS_SELECTOR, '#robotsRule').click()
    time.sleep(1)
    browser.find_element(By.CSS_SELECTOR, 'button').click()

finally:
    time.sleep(10)
    browser.quit()