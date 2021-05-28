import time
from selenium import webdriver
import math

link = "http://SunInJuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element_by_id("input_value").text
    result = str(math.log(abs(12*math.sin(int(x)))))

    input_1 = browser.find_element_by_id("answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", input_1)
    input_1.send_keys(result)

    browser.find_element_by_id("robotCheckbox").click()
    browser.find_element_by_id("robotsRule").click()

    browser.find_element_by_tag_name("button").click()

finally:
    time.sleep(15)
    browser.quit()
