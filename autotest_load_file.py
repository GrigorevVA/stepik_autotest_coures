from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os


try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)

    First_name=browser.find_element(By.CSS_SELECTOR,"input[name='firstname']").send_keys("Donald")
    Last_name=browser.find_element(By.CSS_SELECTOR, "input[name='lastname']").send_keys('Tramp')
    e_mail=browser.find_element(By.CSS_SELECTOR, "input[name='email']").send_keys("macdonalds@gmail.com")
    current_dir=os.path.abspath(os.path.dirname(__file__))
    file_path=os.path.join(current_dir, 'jump.txt')
    print(os.path.abspath(__file__))
    print(os.path.abspath(os.path.dirname(__file__)))
    file=browser.find_element(By.CSS_SELECTOR, "input[id='file']").send_keys(file_path)
    button=browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    # field= browser.find_element(By.CSS_SELECTOR, "input[id='answer']").send_keys(y)
    # checkbox=browser.find_element(By.CSS_SELECTOR,"input[id='robotCheckbox']").click()

    # button = browser.find_element(By.TAG_NAME, "button")
    # browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    #
    # radiobutton=browser.find_element(By.CSS_SELECTOR, "input[id='robotsRule']").click()
    # button.click()
finally:
    time.sleep(10)
    browser.quit()

