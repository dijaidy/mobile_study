import urllib.request
from bs4 import BeautifulSoup
import json
import xmltodict

# ttbsmartapple031950001 TTBkey
# 요청url주소 = http://www.aladin.co.kr/ttb/api/ItemList.aspx
# http://www.aladin.co.kr/ttb/api/ItemSearch.aspx?ttbkey=ttbsmartapple031950001&Query=쎈&QueryType=쎈&MaxResults=10&CategoryId=76841&output=XML&Version=20131101
# 76842, 76812중1과학
# 76839, 76813중1국어
# 76844, 76814중1기가
# 76847, 76818중1도덕
# 76843, 76833중1사탐
# 76841, 76816중1수학
# 76840, 76817중1영어
# 76846       중1시험

# 76830, 76804중2과학
# 76831, 76805중2국어
# 76832, 76806중2기가
# 76837, 76810중2도덕
# 76833, 76807중2사탐
# 76834, 76808중2수학
# 76835, 76809중2영어
# 76836중2시험

# 76820중3과학
# 76821중

# 검색어에 따라 결과 출력
# input_word = input("검색어 입력> ")
# input_choice = input("선택사항 입력(학년, 과목):")
# query = "&query=" + urllib.parse.quote(input_word)
# url = (
#    "http://www.aladin.co.kr/ttb/api/ItemSearch.aspx?ttbkey=ttbsmartapple031950001%s&MaxResults=10&CategoryId=76000&output=JS&Version=20131101"
#    % query
# )

# request = urllib.request.Request(url)
# response = urllib.request.urlopen(request)
# rescode = response.getcode()

# if rescode == 200:
#    respose_body = response.read()
#    print(respose_body.decode("utf-8"))

url_edunet = "http://down.edunet4u.net/KEDNCM/OPENAPI/WKSTCONT/nedu_wkst_cont_(CLSS0000000362).xml"
request = urllib.request.Request(url_edunet)
response = urllib.request.urlopen(request)
rescode = response.getcode()

if rescode == 200:
    respose_body = response.read()
    cc = xmltodict.parse(respose_body.decode("utf-8"))  # return collections.OrderedDict
    dd = json.loads(json.dumps(cc))  # return dict
    animals = dd["animals"]["animal"]
    print(animals)  # 결과를 출력한다


class Book:
    def __init__(self, title):
        pass
