from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/math.html"

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_elem = browser.find_element_by_id("input_value")
    x = x_elem.text

    result = calc(x)

    input_1 = browser.find_element_by_id("answer")
    input_1.send_keys(result)

    click_chBox = browser.find_element_by_css_selector("label[for='robotCheckbox']")
    click_chBox.click()

    click_radio = browser.find_element_by_css_selector("label[for='robotsRule']")
    click_radio.click()

    button = browser.find_element_by_tag_name("button")
    button.click()

finally:
    time.sleep(10)
    browser.quit()