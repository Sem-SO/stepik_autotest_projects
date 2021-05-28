import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

#link = "http://suninjuly.github.io/selects1.html"
link = "http://suninjuly.github.io/selects2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    num_1 = browser.find_element_by_id("num1").text
    num_2 = browser.find_element_by_id("num2").text

    value = int(num_1) + int(num_2)

    #print(value, type(value))

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(value))

    browser.find_element_by_tag_name("button").click() #click on Submit button

finally:
    time.sleep(15)
    browser.quit()
