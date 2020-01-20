import selenium, os, time, math
from selenium import webdriver

#curr_dir = os.path.abspath(os.path.dirname(__file__))
#print(curr_dir)
#file_dir = os.path.join(curr_dir,'file_for_test_10.txt')
#print(file_dir)
#print(os.path.abspath(os.path.dirname(__file__)))
#print(os.path.abspath(__file__))
#print(tett)

def calc(a):
        return str(math.log(abs(12*math.sin(int(a)))))

link = "http://suninjuly.github.io/alert_accept.html"


try:
    browser = webdriver.Chrome()
    browser.get(link)
#    time.sleep(3)
#click
    btn_confirm = browser.find_element_by_css_selector(".btn.btn-primary").click()
#accept
#    time.sleep(3)
    confirm = browser.switch_to.alert
    confirm.accept()
#do_math
    x_res = calc(browser.find_element_by_id("input_value").text)
#answer
    browser.find_element_by_id("answer").send_keys(x_res)
    browser.find_element_by_css_selector(".btn.btn-primary").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()


