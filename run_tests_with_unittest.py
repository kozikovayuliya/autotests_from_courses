
import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By


class test_asserts(unittest.TestCase):
    def test_registration_1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element(By.CSS_SELECTOR, '.first_block input.form-control.first')
        input1.send_keys('something')
        input2 = browser.find_element(By.CSS_SELECTOR, '.first_block input.form-control.second')
        input2.send_keys('something')
        input3 = browser.find_element(By.CSS_SELECTOR, '.first_block input.form-control.third')
        input3.send_keys('something')

        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual(welcome_text, 'Congratulations! You have successfully registered!',
                         'Inform message is incorrect, registration not successful')
        time.sleep(1)
        browser.quit()

    def test_registration_2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element(By.CSS_SELECTOR, '.first_block input.form-control.first')
        input1.send_keys('something')
        input2 = browser.find_element(By.CSS_SELECTOR, '.first_block input.form-control.second')
        input2.send_keys('something')
        input3 = browser.find_element(By.CSS_SELECTOR, '.first_block input.form-control.third')
        input3.send_keys('something')

        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual(welcome_text, 'Congratulations! You have successfully registered!',
                         'Inform message is incorrect, registration not successful')
        time.sleep(1)
        browser.quit()


if __name__ == "__main__":
    unittest.main()
