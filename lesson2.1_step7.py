from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/get_attribute.html"

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_elem = browser.find_element_by_id("treasure")
    x = x_elem.get_attribute("valuex")

    print(x, type(x))

    result = calc(x)

    input_1 = browser.find_element_by_id("answer")
    input_1.send_keys(result)

    click_chBox = browser.find_element_by_id("robotCheckbox")
    click_chBox.click()

    click_radio = browser.find_element_by_id("robotsRule")
    click_radio.click()

    button = browser.find_element_by_tag_name("button")
    button.click()

finally:
    time.sleep(10)
    browser.quit()