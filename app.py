# -*- coding:utf-8 -*-
import csv
import os
import sys
from linebot import LineBotApi
from linebot.models import TextSendMessage
from requests_html import HTMLSession
import requests
import pandas as pd
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup

ACCESS_TOKEN = 'qV/aUVRqv9ZhKjB/9toPGmj3Hdko5WlBN2QLlBRdA8Uy1zBc7oI2RhhfQdPfl53lvzLRG8JvI5F/nZSiTQXVMXQKSMN4QaPSq+RrMOBtrue6cChA3xYgAnk9aqmg0J+38dyAEdN1PFeciG12M/D3kwdB04t89/1O/w1cDnyilFU='
TARGET_URL = 'http://127.0.0.1:5500/index.html'

html=requests.get("http://127.0.0.1:5500/index.html").text
soup=BeautifulSoup(html,"html.parser")
#print(soup.prettify)

text=soup.get_text()
#print(text)

for script in soup(["script", "style"]):
    script.decompose()
#print(soup)

#info = soup.find_all('p', class_='info')
#print(info)

lines= [line.strip() for line in text.splitlines()]
#print(lines)

text = [a for a in lines if a != ''] #ページ内の文字列をリスト化
#print(text)


del text[0]
del text[0]
del text[18]
#print(text)



set1 = [text[0], text[1], text[2]]
set2 = [text[3], text[4], text[5]]
set3 = [text[6], text[7], text[8]]
set4 = [text[9], text[10], text[11]]
set5 = [text[12], text[13], text[14]]
set6 = [text[15], text[16], text[17]]

sets = [set1, set2, set3, set4, set5, set6]
#print(sets)



with open('test.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    for row in sets:
       writer.writerow(row)
       #print(row)

if not os.path.exists('test.csv'):
    raise Exception('ファイルがありません。')
if os.path.getsize('test.csv') == 0:
    raise Exception('ファイルの中身が空です。')
csv_list = pd.read_csv('test.csv', header=None).values.tolist()

def broadcast_to_friends(message):
        line_bot_api = LineBotApi(ACCESS_TOKEN)
        line_bot_api.broadcast(TextSendMessage(text=message))

if sets == csv_list:
    broadcast_to_friends("イベント情報が更新されました:" + TARGET_URL)



