from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

try:
    link = 'http://suninjuly.github.io/selects1.html'
    browser = webdriver.Chrome()
    browser.get(link)

    first_number_element = browser.find_element(By.CSS_SELECTOR, '#num1')
    firs_number = int(first_number_element.text)

    second_number_element = browser.find_element(By.CSS_SELECTOR, '#num2')
    second_number = int(second_number_element.text)

    total = str(firs_number + second_number)

    select = Select(browser.find_element(By.CSS_SELECTOR, '#dropdown'))
    select.select_by_visible_text(total)

    browser.find_element(By.CSS_SELECTOR, 'button').click()

finally:
    time.sleep(7)
    browser.quit()