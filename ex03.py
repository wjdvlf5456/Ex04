import requests
from bs4 import BeautifulSoup

import util

print("============================== *1.사이트에 요청 응답(html)을 받기 ==========================================================================================")
url = "https://movie.naver.com/movie/sdb/rank/rmovie.naver"

print("============================== *1-1.주소 요청하기 ==============================")
# respone는 변수명으로 사용할 것이다.
response = requests.get(url);
print(response.status_code)  # 상태코드:주소틀리면 404출력

print("")
print("============================== *1-2.html소스 추출 및 응답확인 ==============================")
html = response.text  # 변수명.text 는 html소스를 가져온다.
print(html)

print("")
print("============================== *2.필요한 태그 추출하기 - BeautifulSoup4 ==========================================================================================")
print("============================== *2-1.html소스 추출 ==============================")
soup = BeautifulSoup(html,"html.parser")
print(soup)

print("")
print("============================== *2-2.enumerate함수 ==============================")
tags = soup.select(".tit3>a")
for index, tag in enumerate(tags):
    # 랭킹
    rank = index + 1

    # 영화제목
    title = tag.text

    # 포스터
    sub_page_url = tag["href"]
    sub_url = "https://movie.naver.com/" + sub_page_url
    filePath = util.imgDown(sub_url)  # 서브페이지에서 포스터를 수집한다

    print(rank, title, filePath)