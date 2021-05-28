import math
from selenium import webdriver

link ="http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element_by_tag_name("button").click() #click on "moving" button

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x = browser.find_element_by_id("input_value").text  # get value for equation
    result = str(math.log(abs(12 * math.sin(int(x)))))  # equation
    browser.find_element_by_id("answer").send_keys(result)
    browser.find_element_by_tag_name("button").click()

    alert = browser.switch_to.alert
    alert_text = alert.text
    answer_text = alert_text.split(": ")[-1]
    alert.accept()

finally:
    print(answer_text)
    browser.quit()