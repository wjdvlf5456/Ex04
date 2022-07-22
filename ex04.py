from selenium import webdriver


#브라우저 생성
wd = webdriver.Chrome("/Users/choijungphil/javaStudy/chromedriver")

#사이트 요청
url = "https://movie.naver.com/movie/sdb/rank/rmovie.naver"
wd.get(url)
wd.implicitly_wait(10)  #최대10초 로딩끝나면 그전에 끝남

#더보기 클릭
wd.find_element(By.CSS_SELECTOR,".alex_more").click()


#필요한 태그 추출하기 webdriver
cmt_tags = wd.find_elements((By.CSS_SELECTOR,".cmt_info"))
print(cmt_tags)

for cmt_tag in cmt_tags:
    point = cmt_tag.find_element(By.CSS_SELECTOR,".ratings").text
    cmt = cmt_tag.find_element(By.CSS_SELECTOR,"li>a").text
    date = cmt_tag.find_element(By.CSS_SELECTOR,"").text

    print(point,cmt,date,ene="\n\n")