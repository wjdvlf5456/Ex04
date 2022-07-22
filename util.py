import requests
from bs4 import BeautifulSoup
import uuid

def imgDown(sub_page_url):
    #sub_page_url = "https://movie.naver.com/movie/bi/mi/basic.naver?code=81888"

    # sub_page_url 요청 --> 응답(html)
    # 요청하기
    response = requests.get(sub_page_url);
    html = response.text
    #print(html)

    # 필요한 poster_url 추출
    soup = BeautifulSoup(html, "html.parser")
    tag = soup.select_one(".poster>a>img")
    poster_url =  tag["src"]
    #print(poster_url)

    # poster_url 요청 --> 응답(1020310312031030103013013030130103)
    # 파일이름
    saveName = str(uuid.uuid4())

    # 저장위치+파일이름
    filePath = "/Users/choijungphil/javaStudy/upload/movie/"+saveName+".jpg"

    #요청
    img_response = requests.get(poster_url);

    # /Users/choijungphil/javaStudy/upload/movie/ 저장
    file = open(filePath, "wb")
    file.write(img_response.content)
    file.close()

    # 파일경로 리턴
    return filePath

'''
result = imgDown()
print(result)
'''