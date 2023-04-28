from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser.get(link)
    but=browser.find_element(By.CSS_SELECTOR, "button[id='book']")
    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "h5[id='price']"), "100"))
    but.click()
    button = browser.find_element(By.CSS_SELECTOR, "button[id='solve']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    LF_X=browser.find_element(By.CSS_SELECTOR, "span[id='input_value']").text
    y=calc(LF_X)
    field=browser.find_element(By.CSS_SELECTOR, "input[id='answer']" ).send_keys(y)
    button.click()






    # button_1=browser.find_element(By.CSS_SELECTOR, "button[type='submit']" ).click()
    # confirm=browser.switch_to.alert
    # confirm.accept()
    #
    # LF_x = browser.find_element(By.CSS_SELECTOR, "span[id='input_value']").text
    # y = calc(LF_x)
    # field = browser.find_element(By.CSS_SELECTOR, "input[id='answer']").send_keys(y)
    # button_2=browser.find_element(By.CSS_SELECTOR, "button[type='submit']" ).click()

    # First_name=browser.find_element(By.CSS_SELECTOR,"input[name='firstname']").send_keys("Donald")
    # Last_name=browser.find_element(By.CSS_SELECTOR, "input[name='lastname']").send_keys('Tramp')
    # e_mail=browser.find_element(By.CSS_SELECTOR, "input[name='email']").send_keys("macdonalds@gmail.com")
    # current_dir=os.path.abspath(os.path.dirname(__file__))
    # file_path=os.path.join(current_dir,'jump.txt')
    # print(os.path.abspath(__file__))
    # print(os.path.abspath(os.path.dirname(__file__)))
    # file=browser.find_element(By.CSS_SELECTOR, "input[id='file']").send_keys(file_path)
    # button=browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    # # field= browser.find_element(By.CSS_SELECTOR, "input[id='answer']").send_keys(y)
    # # checkbox=browser.find_element(By.CSS_SELECTOR,"input[id='robotCheckbox']").click()
    #
    # # button = browser.find_element(By.TAG_NAME, "button")
    # # browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    # #
    # # radiobutton=browser.find_element(By.CSS_SELECTOR, "input[id='robotsRule']").click()
    # # button.click()
finally:

    browser.quit()

