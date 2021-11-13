from selenium import webdriver
import time 
import math
import os
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.implicitly_wait(5) #ожидание появления элемента на странице

    button = browser.find_element_by_css_selector("#book")
    button.click()
    
    confirm = browser.switch_to.alert
    confirm.accept()
    
    browser.implicitly_wait(5)
    price=WebDriverWait(browser, 20).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    print(price)
    
    button = browser.find_element_by_css_selector("#book")
    button.click()
    browser.implicitly_wait(5)
    # button = browser.find_element_by_css_selector("#solve")
    # browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    # button.click()
    # browser.execute_script("window.scrollBy(0, 100);")
    # print("scroll")
    x=browser.find_element_by_css_selector("#input_value").text
    y=calc(x)
    print(y)
    answer=browser.find_element_by_css_selector("#answer").send_keys(y)
    
    button = browser.find_element_by_css_selector("#solve")
    button.click()

    confirm = browser.switch_to.alert
    print(allert.text)
finally:
   
    time.sleep(10)
    
    browser.quit()

# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# import math
# import time

# def calc(x):
#   return str(math.log(abs(12*math.sin(int(x)))))

# try:
#     browser = webdriver.Chrome()
#     browser.get("http://suninjuly.github.io/explicit_wait2.html")

#     book_btn = browser.find_element_by_id("book")
#     book_btn.click()
#     confirm = browser.switch_to.alert
#     confirm.accept()
#     time.sleep(1)
#     p=browser.find_element_by_id("price")
#     p=p.text
#     print(p)
#     #Ждем, когда цена станет $100
#     price = WebDriverWait(browser, 12).until( EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
#     print("sdaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaddddddddddddddddddddddddddddddddddddddddddddddddddd")
#     print(browser.find_element_by_id("price").text)
#     # #Находим и нажимаем на кнопку "Book"
#     book_btn = browser.find_element_by_id("book")
#     book_btn.click()
#     time.sleep(1)
#     #Решаем математическую задачу:
#     x_element = browser.find_element_by_id('input_value').text
#     x = calc(x_element)
    
#     input1 = browser.find_element_by_id('answer')
#     input1.send_keys(x)
    
#     submit_btn = browser.find_element_by_id("solve")
#     submit_btn.click()
    

# finally:
#     time.sleep(10)
#     browser.quit()

# from selenium import webdriver
# from selenium.webdriver.common.by import By

# link = "http://suninjuly.github.io/simple_form_find_task.html"

# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#     button = browser.find_element(By.ID, "submit_button")
#     button.click()
#     print("yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy")
# finally:
#     # закрываем браузер после всех манипуляций
#     time.sleep(10)
#     browser.quit()

# Для загрузки файла на веб-страницу, используем метод send_keys("путь к файлу")
# Три способа задать путь к файлу:

# 1. вбить руками

# element.send_keys("/home/user/stepik/Chapter2/file_example.txt")

 

# 2. задать с помощью переменных

# # указывая директорию,где лежит файлу.txt
# # в конце должен быть /
# directory = "/home/user/stepik/Chapter2/"

# # имя файла, который будем загружать на сайт
# file_name = "file_example.txt"

# # собираем путь к файлу
# file_path = os.path.join(directory, file_name)
# # отправляем файл
# element.send_keys(file_path)
# 3.путь автоматизатора.
# если файлы lesson2_7.py и file_example.txt" лежат в одном каталоге
# # импортируем модуль
# import os
# # получаем путь к директории текущего исполняемого скрипта lesson2_7.py
# current_dir = os.path.abspath(os.path.dirname(__file__))

# # имя файла, который будем загружать на сайт
# file_name = "file_example.txt"

# # получаем путь к file_example.txt
# file_path = os.path.join(current_dir, file_name)
# # отправляем файл
# element.send_keys(file_path)
# """
# итоговый код:

# import os
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# link = "http://suninjuly.github.io/file_input.html"
# browser = webdriver.Firefox()
# browser.get(link)
# current_dir = os.path.abspath(os.path.dirname(__file__))
# file_name = "file_example.txt"
# file_path = os.path.join(current_dir, file_name)
# element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
# element.send_keys(file_path)