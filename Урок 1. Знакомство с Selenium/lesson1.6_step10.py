from selenium import webdriver
import time

#link = "http://suninjuly.github.io/registration1.html"      # ссылка без бага
link = "http://suninjuly.github.io/registration2.html"     # ссылка с багом

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input_1 = browser.find_element_by_css_selector("div.first_block > div:nth-child(1) > input")    # first_name
    input_1.send_keys("Ivan")
    input_2 = browser.find_element_by_css_selector("input[placeholder='Input your last name']")     # last_name
    input_2.send_keys("Ivanov")
    input_3 = browser.find_element_by_css_selector("div.third_class > input")     # email
    input_3.send_keys("i.ivanov@email.ru")


    button = browser.find_element_by_css_selector("button.btn")
    button.click()                                              # нажатие на кнопку

    time.sleep(3)   # ожидание загрузки страницы

    welcome_text_el = browser.find_element_by_css_selector("div h1")
    welcome_text = welcome_text_el.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(60)
    browser.quit()
