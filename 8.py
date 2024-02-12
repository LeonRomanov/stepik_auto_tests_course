from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    text = (By.XPATH, "//h5[@id='price']")
    wait = WebDriverWait(browser, 10).until(
        EC.text_to_be_present_in_element(text, "100"))
    button = browser.find_element(By.XPATH, "//button[@id='book']").click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла