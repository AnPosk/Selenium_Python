from selenium import webdriver
import time 
import math
from selenium.webdriver.support.ui import Select

def calc(x, a):
    return str(int(x)+int(a))

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id('num1')
    x = x_element.text
    y_element = browser.find_element_by_id('num2')
    a = y_element.text
    y = calc(x, a)

    # browser.find_element_by_tag_name("select").click()
    # browser.find_element_by_css_selector("[value='1']").click() не для этого примера

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(y)
    
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла