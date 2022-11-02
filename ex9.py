import time
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService



try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    browser.get(link)

    num1 = browser.find_element(By.ID, "num1")
    num2 = browser.find_element(By.ID, "num2")
    num1 = int(num1.text)
    num2 = int(num2.text)
    my_sum = str(num1 + num2)

    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(my_sum)

    button = browser.find_element(By.CLASS_NAME, "btn-default")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()


