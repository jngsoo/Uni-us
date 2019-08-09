import pandas as pd
import re
import konlpy
from konlpy.tag import Kkma

class sort_by_date:
    def __init__(self,date, post):
        self.date = date
        self.post = post

    def __call__(self):
        print(self.date, self.post)

class post:
    def __init__(self, title, content, comment ,vote, scrap):
        self.title = title
        self.content = content
        self.comment = comment
        self.vote = vote
        self.scrap = scrap
    def __call__(self):
        print(self.title, self.content, self.comment, self.vote, self.scrap)

class count:
    def __init__(self, date, freq):
        self.date = date
        self.freq = freq

    def __call__(self):
        print(self.freq, self.freq)

def make_list(date, start):
    post_object = []
    for i in range(start, len(csv)):
        if date == csv['date'][i]:
            post_object.append(post(csv['title'][i], csv['content'][i], csv['comment'][i], csv['vote'][i], csv['scrap'][i]))
    date_object.append(sort_by_date(date, post_object))


def make_date(start, end):

    for i in range(6):
        new_date = str(int(start[-2:])-i)
        if new_date == '0':
            break
        elif len(new_date) != 2:
            date = start[:3] +'0'+ new_date +'\n'
            date_list.append(date)
        else:
            date = start[:3]+ new_date
            date_list.append(date)
    for i in range(26):
        new_date2 = str(int(end[-2:])-i)
        if len(new_date2) != 2:
            date2 = end[:3] +'0'+ new_date2+'\n'
            date_list.append(date2)
        else:
            date2 = end[:3]+ new_date2 +'\n'
            date_list.append(date2)

def cleanText(rawText):
    pattern = re.compile('\w*\s*')
    result = "".join(re.findall(pattern, rawText))
    return result

def merge(object, start, end):
    for i in range(start,end):
        wordDict = {}
        for j in range(len(object[i].post)):
            title = object[i].post[j].title
            content = object[i].post[j].content
            title = cleanText(title)

            if type(content) != str:
                continue
            else:
                content = cleanText(content)
            texts = title + content
            malist = kkma.pos(texts)

            for x in malist:
                if 'NNG' in x:
                    keyword = x[0]
                    if keyword in wordDict:
                        wordDict[keyword] += 1
                    else:
                        wordDict[keyword] = 1

        wordDict = sorted(wordDict.items(), key=lambda t: t[1], reverse=True)
        print(wordDict)
        count_object.append(count(object[i].date, wordDict))

if __name__ == '__main__':
    date_list =[]
    date_object = []
    count_object = []

    kkma = Kkma()

    make_date('08/06', '07/31')
    csv = pd.read_csv('result.csv')

    for a in date_list:
        make_list(a, 0)
    print(0)
    for i in range(0,30,2):
        merge(date_object, i, i+2)