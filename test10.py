import selenium, os, time
from selenium import webdriver

#curr_dir = os.path.abspath(os.path.dirname(__file__))
#print(curr_dir)
#file_dir = os.path.join(curr_dir,'file_for_test_10.txt')
#print(file_dir)
#print(os.path.abspath(os.path.dirname(__file__)))
#print(os.path.abspath(__file__))
#print(tett)

link = "http://suninjuly.github.io/file_input.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
#    time.sleep(3)

    f_name = browser.find_element_by_name("firstname").send_keys('firstname')
    l_name = browser.find_element_by_name("lastname").send_keys('lastname')
    email = browser.find_element_by_name("email").send_keys('some@email.com')

    t_file_dir = os.path.abspath(os.path.dirname(__file__))
    print(t_file_dir)
    t_file_path = os.path.join(t_file_dir,'file.txt')
    print(t_file_path)

    t_file = browser.find_element_by_id("file").send_keys(t_file_path)

    btn = browser.find_element_by_css_selector(".btn.btn-primary").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()


