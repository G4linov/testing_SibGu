from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService



# функция, которая находит значение выражения при заданном x
def calc(x):
    return str(math.log(abs(12 * math.sin(x))))


link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
browser.get(link)


my_button = browser.find_element(By.ID, "book")
price = WebDriverWait(browser, 15).until(
EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
my_button.click()

# находим значение x для выполнения задания
x_string = browser.find_element(By.ID, "input_value")
x_number = int(x_string.text)

# высчитываем результат для задания
answer = calc(x_number)

# вводим результат в поле ввода
input_answer = browser.find_element(By.ID, "answer")
input_answer.send_keys(answer)

# нажимаем на кнопку
send_button = browser.find_element(By.ID, "solve")
send_button.click()


