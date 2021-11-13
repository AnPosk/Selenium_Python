from selenium import webdriver
import time 
import math
import os

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x=browser.find_element_by_css_selector("#input_value").text
    y=calc(x)

    answer=browser.find_element_by_css_selector("#answer").send_keys(y)
    
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    confirm = browser.switch_to.alert
    confirm.text

    

finally:
   
    time.sleep(10)
    
    browser.quit()

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