import multiprocessing
from time import sleep
# from appium.webdriver.webdriver import By
from selenium.webdriver.common.by import By
# from testcase.common.basePage import BasePage
from testcase.page.reg_login_page.login_page.loginPage import LoginPage

item_class = (By.CLASS_NAME, "android.widget.TextView")
evaluation_id = (By.ID, 'com.langlib.cee:id/evaluation')
action_id = (By.ID, 'com.langlib.cee:id/evaluation_begin_tv')
# com.langlib.cee:id/evaluation_begin_tv
a = "com.langlib.cee:id/fragment_word_trans_detail_answer_a"
radio_id = (By.ID, "com.langlib.cee:id/fragment_word_trans_detail_answer_a")
radio_b_id = (By.ID, "com.langlib.cee:id/fragment_word_trans_detail_answer_b")
radio_classes = (By.CLASS_NAME, "android.widget.RadioButton")
edit_id = (By.ID, "com.langlib.cee:id/write_measure_edit")
next_id = (By.ID, "com.langlib.cee:id/senavaly_quest_next_quest")
title_id = (By.ID, "com.langlib.cee:id/title_iframe_title_tv")
web_class = (By.CLASS_NAME, "android.widget.ScrollView")
step_1_id = (By.ID, "com.langlib.cee:id/measure_step_one")
def func(login_page, ele):
    login_page.find_element(*ele).click()


if __name__ == '__main__':
    ids = [radio_id, next_id]
    login_page = LoginPage()
    login_page.open(noReset=True)
    sleep(15)
    for i in range(100):
        p = multiprocessing.Process(target=func, args=(login_page, ids))
        p.start()
        p.join()
    print("Sub-process done.")