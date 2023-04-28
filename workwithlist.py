from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select
import math




try:
    link="https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    # s=str(math.ceil(math.pow(math.pi, math.e) * 10000))
    # number_luck=browser.find_element(By.PARTIAL_LINK_TEXT,s)
    # number_luck.click()

    first_number = browser.find_element(By.CSS_SELECTOR, "span[id='num1']")

    second_number=browser.find_element(By.CSS_SELECTOR, "span[id='num2']")
    field=str(int(first_number.text)+int(second_number.text))

    select=Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(field)




#     input3=browser.find_element(By.CSS_SELECTOR,"input[id='answer']" )
#     input3.send_keys(chrager)
#     chech_box=browser.find_element(By.CSS_SELECTOR, "input[type='checkbox']")
#     chech_box.click()
#     rediobut=browser.find_element(By.CSS_SELECTOR, "input[id='robotsRule']").click()
    submit=browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit.click()
# #     people_radio = browser.find_element(By.ID, "robotsRule")
# #     people_checked = people_radio.get_attribute("checked")
# #     try:
# #         print("value of people radio: ", people_checked)
# #         assert people_checked is None, "People radio is not selected by default"
# #     except AssertionError:
# #         print("People radio is not selected by default")
# #
# #
# #
# # # Проверяем, что смогли зарегистрироваться
# #     # ждем загрузки страницы
# #     time.sleep(1)
# #
# # # находим элемент, содержащий текст
# # #     welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
# # #     # записываем в переменную welcome_text текст из элемента welcome_text_elt
# # #     welcome_text = welcome_text_elt.text
# # #
# # #     # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
# # #     assert "Congratulations! You have successfully registered!" == welcome_text
# #

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()