from selenium import webdriver
import time
import os
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

try:

    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    browser.get(link)

    # находим все нужные элементы на странице
    name_field = browser.find_element(By.CSS_SELECTOR, "[name='firstname']")
    lastname_field = browser.find_element(By.CSS_SELECTOR, "[name='lastname']")
    email_field = browser.find_element(By.CSS_SELECTOR, "[name='email']")
    file_button = browser.find_element(By.CSS_SELECTOR, "[type='file']")
    send_button = browser.find_element(By.CSS_SELECTOR, ".btn-primary")

    # заполняем форму
    name_field.send_keys("*")
    lastname_field.send_keys("*")
    email_field.send_keys("*")

    # находим путь до папки
    current_dir = os.path.abspath(os.path.dirname("F:/mama/"))

    # достраиваем его путь до нужного файла
    file_path = os.path.join(current_dir, "Logo.svg")

    # отправляем этот файл
    file_button.send_keys(file_path)
    send_button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()