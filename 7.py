from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

# Импортируем нашу функцию для решения математической задачи
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


# Определяем URL страницы
url = "http://suninjuly.github.io/explicit_wait2.html"

# Определяем цену, которую мы готовы заплатить
target_price = "$100"

try:
    # Инициализируем веб-драйвер и открываем страницу
    browser = webdriver.Chrome()
    browser.get(url)

    # Ожидаем, пока цена дома не уменьшится до $100
    price_locator = (By.ID, "price")
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element(price_locator, target_price))

    # Находим и нажимаем на кнопку "Book"
    book_button = browser.find_element(By.ID, "book")
    book_button.click()
    
    inp_value = browser.find_element(By.XPATH, "//span[@id='input_value']")
    x = inp_value.text
    print(x)
    y = calc(x)    
    print(y)
    answer = browser.find_element(By.XPATH, "//input[@id='answer']")
    answer = answer.send_keys(y)
    button = browser.find_element(By.XPATH, "//button[@type='submit']").click()

finally:
    time.sleep(20)
    # Закрываем браузер
    browser.quit()