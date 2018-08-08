# coding:utf-8
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC  # 开启自动化工具显式等待
import time
driver = webdriver.Chrome()
driver.maximize_window()
res = driver.get('https://i.qq.com/')
driver.switch_to.frame('login_frame')
user = ''
pwd = ''
driver.find_element_by_id('bottom_qlogin').click()
driver.find_element_by_id('u').send_keys(user)
driver.find_element_by_id('p').send_keys(pwd)
driver.find_element_by_id('login_button').click()
js = 'window.open("https://user.qzone.qq.com/614345508/311")'
driver.execute_script(js)
handles = driver.window_handles
driver.switch_to_window(handles[1])
driver.switch_to_default_content()
next_num = 0
while True:
    for i in range(0, 5):
        height = 20000 * i
        jsstr = 'window.scrollBy(0,'+str(height)+')'
        driver.execute_script(jsstr)
        time.sleep(2)
    driver.switch_to.frame('app_canvas_frame')
    content = BeautifulSoup(driver.page_source, 'lxml')
    msgList = content.find_all('li', class_="feed")
    with open('word.txt', 'a+', encoding='utf-8') as f:
        for msg in msgList:
            tag_div = BeautifulSoup(
                str(msg), 'lxml').find_all('div', class_='bd')
            one_tag = BeautifulSoup(str(tag_div), 'lxml').find('pre')
            f.write(one_tag.get_text()+'\n')
    if driver.find_element_by_id('pager_next_'+str(next_num)) == -1:
        print('end', next_num)
        break
    print('success:', next_num)
    driver.find_element_by_id('pager_next_'+str(next_num)).click()
    next_num += 1
    driver.switch_to.parent_frame()
