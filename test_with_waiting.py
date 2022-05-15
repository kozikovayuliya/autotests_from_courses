from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = 'http://suninjuly.github.io/explicit_wait2.html'
    browser = webdriver.Chrome()
    browser.get(link)
    browser.implicitly_wait(2)

    price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#price'), '100'))
    browser.find_element(By.CSS_SELECTOR, '#book').click()

    x = browser.find_element(By.CSS_SELECTOR, '#input_value').text
    browser.find_element(By.CSS_SELECTOR, '#answer').send_keys(calc(x))
    browser.find_element(By.CSS_SELECTOR, '#solve').click()

finally:
    time.sleep(5)
    browser.quit()