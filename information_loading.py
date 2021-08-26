import urllib.request
from bs4 import BeautifulSoup
#ttbsmartapple031950001 TTBkey
#http://www.aladin.co.kr/ttb/api/ItemSearch.aspx?ttbkey=ttbsmartapple031950001&Query=쎈&QueryType=쎈&MaxResults=10&CategoryId=76816&output=XML&Version=20131101
#76842, 76812중1과학
#76839, 76813중1국어
#76844, 76814중1기가
#76847, 76818중1도덕
#76843, 76833중1사탐
#76841, 76816중1수학
#76840, 76817중1영어
#76846       중1시험

#76830, 76804중2과학
#76831, 76805중2국어
#76832, 76806중2기가
#76837, 76810중2도덕
#76833, 76807중2사탐
#76834, 76808중2수학
#76835, 76809중2영어
#76836중2시험

#76820중3과학
#76821중
url='http://www.aladin.co.kr/ttb/api/ItemSearch.aspx?ttbkey=ttbsmartapple031950001&Query=%EC%8E%88&QueryType=%EC%8E%88&MaxResults=10&CategoryId76816&output=JS&Version=20131101'
html=urllib.request.urlopen(url).read()
soup=BeautifulSoup(html, 'JSON.parser')
print(soup)
class Book:
    def __init__(self, title):
        pass
