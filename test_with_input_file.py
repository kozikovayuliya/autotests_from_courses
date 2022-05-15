from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    link = 'http://suninjuly.github.io/file_input.html'
    browser = webdriver.Chrome()
    browser.get(link)

    # Заполняем поля

    browser.find_element(By.CSS_SELECTOR, "[name='firstname']").send_keys('Yuliya')
    browser.find_element(By.CSS_SELECTOR, "[name='lastname']").send_keys('Kozikova')
    browser.find_element(By.CSS_SELECTOR, "[name='email']").send_keys('yulyakozikova86@gmail.com')

    # Вставляем файл

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    browser.find_element(By.CSS_SELECTOR, '#file').send_keys(file_path)

    # Нажимаем Submit

    browser.find_element(By.CSS_SELECTOR, 'button').click()

finally:
    time.sleep(10)
    browser.quit()