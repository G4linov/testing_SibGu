from selenium import webdriver
import math
import time
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

link = "http://suninjuly.github.io/find_link_text"
find_str = str(math.ceil(math.pow(math.pi, math.e)*10000))

try:
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    browser.get(link)

    button = browser.find_element(By.LINK_TEXT, find_str)
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
