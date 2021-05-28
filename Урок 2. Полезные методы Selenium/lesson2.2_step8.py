import os
import time
from selenium import webdriver

link = "http://suninjuly.github.io/file_input.html"

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, "test_file_1.txt")

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input_1 = browser.find_element_by_css_selector("input:nth-child(2)")
    input_1.send_keys("Ivan") #input First name

    input_2 = browser.find_element_by_css_selector("input:nth-child(4)")
    input_2.send_keys("Ivanov") #input Last name

    input_3 = browser.find_element_by_css_selector("input:nth-child(6)")
    input_3.send_keys("Ivan@Ivanov.ru") #input Email

    input_file = browser.find_element_by_id("file")
    input_file.send_keys(file_path) #send file

    browser.find_element_by_tag_name("button").click() #click on Submit button

finally:
    time.sleep(15)
    browser.quit()