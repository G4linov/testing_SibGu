from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import math
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    browser.get(link)

    browser.find_element(By.CSS_SELECTOR, 'button.btn').click()

    newurl = browser.window_handles[1]
    browser.switch_to.window(newurl)

    y = calc(int(browser.find_element(By.ID, 'input_value').text))
    browser.find_element(By.ID, 'answer').send_keys(str(y))
    browser.find_element(By.CLASS_NAME, 'btn-primary').click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()