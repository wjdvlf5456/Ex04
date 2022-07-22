import requests
from bs4 import BeautifulSoup

import movieDao
import util

###################################################
# 랭킹추출
###################################################
# 1.사이트에 요청 응답(html)을 받기  - requests
url = "https://movie.naver.com/movie/sdb/rank/rmovie.naver"

# 요청하기
response = requests.get(url);

html = response.text
# print(html)


# 2.필요한 태그 추출하기 - BeautifulSoup4
soup = BeautifulSoup(html, "html.parser")

tags = soup.select(".tit3>a")  # * 전략을 잘 세워야 함
print(tags[0])

for index, tag in enumerate(tags):
    # 랭킹
    rank = index + 1

    # 영화제목
    title = tag.text

    # 포스터
    sub_page_url = tag["href"]
    sub_url = "https://movie.naver.com/" + sub_page_url
    filePath = util.imgDown(sub_url)  # 서브페이지에서 포스터를 수집한다
    #print(rank, title, filePath)

    #db저장
    movieVo = [rank, title, filePath]
    count = movieDao.insert(movieVo)
    print(count)