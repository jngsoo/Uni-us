from django.db import models

# Create your models here.

class DailyPost:
    def __init__(self,date, post):
        self.date = date
        self.post = post

    def __call__(self):
        print(self.date, self.post)

class Post:
    def __init__(self, title, content, comment ,vote, scrap):
        self.title = title
        self.content = content
        self.comment = comment
        self.vote = vote
        self.scrap = scrap

    def __call__(self):
        print(self.title, self.content, self.comment, self.vote, self.scrap)
        

