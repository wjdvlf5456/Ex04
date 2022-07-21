# 크롤링
# import requests as req     as '이름명'으로 하면 이름명으로 사용가능 (ex:현재는 req라는 변수명으로 사용가능)
import requests
from bs4 import BeautifulSoup

print("============================== *1.사이트에 요청 응답(html)을 받기 ==============================")
url = "https://movie.naver.com/movie/sdb/rank/rmovie.naver"

print("=============== *1-1.주소 요청하기 ===============")
# respone는 변수명으로 사용할 것이다.
response = requests.get(url);
print(response.status_code)  # 상태코드:주소틀리면 404출력

print("")
print("=============== *1-2.html소스 추출 및 응답확인 ===============")
html = response.text  # 변수명.text 는 html소스를 가져온다.
print(html)

print("")
print("============================== *2.필요한 태그 추출하기 - BeautifulSoup4 ==============================")
print("=============== *2-1.html소스 추출 ===============")
soup = BeautifulSoup(html,"html.parser")
