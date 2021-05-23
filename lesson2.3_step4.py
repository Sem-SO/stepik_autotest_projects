import math
from selenium import webdriver

link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element_by_tag_name("button").click() #click on "journey" button

    browser.switch_to.alert.accept() #accept "journey" alert

    x = browser.find_element_by_id("input_value").text #get value for equation
    result = str(math.log(abs(12*math.sin(int(x))))) #equation
    browser.find_element_by_id("answer").send_keys(result) #send answer
    browser.find_element_by_tag_name("button").click() #submit answer

# get answer from alert for solving task
    answer_alerl = browser.switch_to.alert
    answer_alerl_text = answer_alerl.text
    answer_text = answer_alerl_text.split(": ")[-1]

finally:
    print(answer_text)
    browser.quit()
