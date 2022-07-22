import requests
import uuid

##############################
#이미지 추출
##############################

img_url="https://movie-phinf.pstatic.net/20220509_176/1652081912471yhg3N_JPEG/movie_image.jpg"

saveName = str(uuid.uuid4());
print(saveName,type(saveName));

#저장위치 + 파일이름
filePath = "\\Users\\choijungphil\\javaStudy\\upload\\movie\\"+saveName+".jpg"
print("파일경로: "+filePath)

img_response = requests.get(img_url)
print(img_response)

file = open(filePath,"wb")
file.write(img_response.content)
file.close()
