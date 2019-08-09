from bs4 import BeautifulSoup as bs
from selenium import webdriver
from time import sleep
import pandas as pd
import datetime

today = datetime.date.today()

def crawler(enddate, start_page, end_page):
    driver = webdriver.Chrome('/Users/jngsoo/Desktop/coding/web_crawling/chromedriver')
    driver.get('https://everytime.kr/login')
    driver.find_element_by_name('userid').send_keys('icke')
    driver.find_element_by_name('password').send_keys('0okm9ijn')
    driver.find_element_by_xpath('//*[@id="container"]/form/p[3]/input').click()

    for z in range(start_page, end_page):
        driver.get('https://everytime.kr/370454/p/' + str(z))
        sleep(0.2)
        start = driver.page_source
        parse = bs(start, 'html.parser')
        atags = parse.findAll('a', 'article')
        url = []

        for b in atags:
            if 'lecture' not in b['href'] and '370454' in b['href']:
                url.append(b['href'])

        for a in url:
            driver.get('https://everytime.kr/370454/' + a)
            sleep(0.5)
            new_start = driver.page_source
            new_parse = bs(new_start, 'html.parser')

            time = new_parse.find('time', 'large')
            if time == None:
                time_text == 0
            else:
                if '분' in time.text or '방금' in time.text:
                    if today.timetuple()[1] < 10:
                        month = str(0) + str(today.timetuple()[1])
                    if today.timetuple()[2] < 10:
                        datee = str(0) + str(today.timetuple()[2])

                    time_text = month + '/' + datee
                else:
                    time_text = time.text[:5]

            if time_text == enddate:
                return

            title = new_parse.find('h2', 'large')
            vote = new_parse.find('li', 'vote')
            comment = new_parse.find('li', 'comment')
            scrap = new_parse.find('li', 'scrap')
            content = new_parse.findAll('p', 'large')
            new_content = []
            for a in content:
                new_content.append(a.text)

            content = ' '.join(new_content)

            with open('date.txt', 'a', encoding='utf-8') as f:
                f.write(time_text + '\n')
            with open('title.txt', 'a', encoding='utf-8') as f:
                f.write(title.text+ '\n')
            with open('content.txt', 'a' , encoding='utf-8') as f:
                f.write(content+ '\n')
            with open('vote.txt', 'a' , encoding='utf-8') as f:
                f.write(vote.text+ '\n')
            with open('comment.txt', 'a', encoding='utf-8') as f:
                f.write(comment.text+ '\n')
            with open('scrap.txt', 'a', encoding='utf-8') as f:
                f.write(scrap.text+ '\n')
    driver.close()

for i in range(1, 10000000, 10):
    crawler('01/01', i, i+5)