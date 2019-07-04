#-*- coding: utf-8 -*-
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from time import sleep
import pandas as pd
import datetime

today = datetime.date.today()
driver = webdriver.Chrome('/Users/jngsoo/Desktop/coding/web_crawling/chromedriver')
driver.get('https://everytime.kr/login')
driver.find_element_by_name('userid').send_keys('icke')
driver.find_element_by_name('password').send_keys('0okm9ijn')
driver.find_element_by_xpath('//*[@id="container"]/form/p[3]/input').click()

date_list = []
title_list = []
content_list = []

for z in range(1,4):
    driver.get('https://everytime.kr/370454/p/'+str(z))
    sleep(1)
    start = driver.page_source
    parse = bs(start, 'html.parser')
    atags = parse.findAll('a', 'article')
    timetag = parse.findAll('time')



    url = []
    post_list ={}
    for b in atags:
        if 'lecture' not in b['href'] and '370454' in b['href']:
            url.append(b['href'])



    for a in url:
        driver.get('https://everytime.kr/370454/' + a)
        sleep(0.2)
        new_start = driver.page_source
        new_parse = bs(new_start, 'html.parser')
        time = new_parse.find('time', 'large')
        if '분' in time.text or '방금' in time.text:
            if today.timetuple()[1] < 10:
                month = str(0) + str(today.timetuple()[1])
            if today.timetuple()[2] < 10:
                datee = str(0) + str(today.timetuple()[2])

            time_text = month +'/'+datee
        else:
            time_text = time.text[:5]

        title = new_parse.find('h2', 'large')
        content = new_parse.find('p', 'large')

        date_list.append(time_text)
        title_list.append(title.text)
        content_list.append(content.text)

driver.close()

data = dict()
data['date'] = date_list
data['title'] = title_list
data['content'] = content_list



df = pd.DataFrame(data)
print(df)

df.to_excel('result.xlsx',sheet_name='sheet1')