from selenium import webdriver
import math
import time

link = "http://suninjuly.github.io/find_link_text"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    secret_link = browser.find_element_by_link_text(str(math.ceil(math.pow(math.pi, math.e) * 10000)))
    secret_link.click()

    input1 = browser.find_element_by_css_selector("input[name='first_name']")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_css_selector("input[name='last_name']")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_css_selector(".form-control.city")
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_id("country")
    input4.send_keys("Russia")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()


finally:
    time.sleep(15)
    browser.quit()
