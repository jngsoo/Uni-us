from konlpy.tag import Kkma
# from openpyxl import load_workbook
import collections
import re

kkma = Kkma()

testLine = "우리형"
malist = kkma.pos(testLine)
for i in malist:
    print(i)