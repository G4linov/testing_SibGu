import unittest

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestRegistration(unittest.TestCase):  # Имя класса должно быть Test*

    def test_registration1_page(self):  # Имя теста должно быть test_*
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        browser.get(link)
        input1 = browser.find_element(By.XPATH, '/html/body/div[1]/form/div[1]/div[1]/input')
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.XPATH, '/html/body/div[1]/form/div[1]/div[2]/input')
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.XPATH, '/html/body/div[1]/form/div[1]/div[3]/input')
        input3.send_keys("pidivanov@mail.ru")
        # Отправляем заполненную форму
        button = browser.find_element(By.XPATH, "//button[@type='submit']")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Welcome text should be displayed on the page")

    def test_registration2_page(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        browser.get(link)
        input1 = browser.find_element(By.XPATH, '/html/body/div[1]/form/div[1]/div[1]/input')
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.XPATH, '/html/body/div[1]/form/div[1]/div[2]/input')
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.XPATH, '/html/body/div[1]/form/div[1]/div[3]/input')
        input3.send_keys("pidivanov@mail.ru")
        # Отправляем заполненную форму
        button = browser.find_element(By.XPATH, "//button[@type='submit']")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Welcome text should be displayed on the page")


if __name__ == '__main__':
    unittest.main()

