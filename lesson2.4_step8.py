from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

url = 'http://suninjuly.github.io/explicit_wait2.html'

try:
    browser = webdriver.Chrome()
    browser.get(url)

    book_button = browser.find_element_by_id('book')
    #browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100')) #ждем, пока текст не будет равен $100
    book_button.click()

    answer = browser.find_element_by_id('answer')
    answer.send_keys(calc(int(browser.find_element_by_id('input_value').text)))

    submit_button = browser.find_element_by_id('solve')
    submit_button.click()
    alert = browser.switch_to.alert
    print(alert.text)

    time.sleep(20)

finally:
    browser.quit()