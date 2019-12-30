#HINT TO USAGE OF CLASS "BY"
#from selenium import webdriver
#from selenium.webdriver.common.by import By

#browser = webdriver.Chrome()
#browser.get("http://suninjuly.github.io/simple_form_find_task.html")
#button = browser.find_element(By.ID, "submit_button")
#Можно использовать те же стратегии поиска, что и в первом способе. Второй способ более удобен для оформления архитектуры тестовых сценариев с помощью подхода Page Object Model, о котором мы будем говорить далее. Пока же предлагаем пользоваться первым методом с явным указанием способа поиска, так как он кажется нам более удобным, но ничто не мешает вам пользоваться и тем, и другим. Поля класса By, которые можно использовать для поиска:

#By.ID – поиск по уникальному атрибуту id элемента;
#By.CSS_SELECTOR – поиск элементов с помощью правил на основе CSS;
#By.XPATH – поиск элементов с помощью языка запросов XPath;
#By.NAME – поиск по атрибуту name элемента;
#By.TAG_NAME – поиск по названию тега;
#By.CLASS_NAME – поиск по атрибуту class элемента;
#By.LINK_TEXT – поиск ссылки с указанным текстом. Текст ссылки должен быть точным совпадением;
#By.PARTIAL_LINK_TEXT – поиск ссылки по частичному совпадению текста.

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
time.sleep(5)

browser.get("http://suninjuly.github.io/math.html")

radio = browser.find_element(By.ID, "peopleRule")
chk = radio.get_attribute("checked");
element = browser.find_element(By.ID, "input_value")

print('{0},{1}'.format(chk, element.text))

time.sleep(5)

browser.quit()