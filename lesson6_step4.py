from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/redirect_accept.html")
    button1 = browser.find_element(By.XPATH, "//button[@type='submit']").click()
    new_window = browser.window_handles[1]  #получили массив имен вкладок
    browser.switch_to.window(new_window)
    inp_value = browser.find_element(By.XPATH, "//span[@id='input_value']")
    x = inp_value.text
    print(x)
    y = calc(x)    
    print(y)
    answer = browser.find_element(By.XPATH, "//input[@id='answer']")
    answer = answer.send_keys(y)
    button = browser.find_element(By.XPATH, "//button[@type='submit']").click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла