from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select


try:

    link="https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    first_number = browser.find_element(By.CSS_SELECTOR, "span[id='num1']")
    second_number=browser.find_element(By.CSS_SELECTOR, "span[id='num2']")
    field=str(int(first_number.text)+int(second_number.text))
    select=Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(field)
    submit=browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()