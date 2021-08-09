from selenium import webdriver
from bs4 import BeautifulSoup
driver=webdriver.Chrome("chromedriver")
driver.implicitly_wait(1)

#ELLT학과 링크
driver.get("http://ellt.hufs.ac.kr/")
driver.implicitly_wait(1)

#NOTICE 게시판 내 각 페이지 명
board_contents=[]
urls=[]
#NOTICE 게시판 url
driver.get("http://builder.hufs.ac.kr/user/indexSub.action?codyMenuSeq=110904182&siteId=ellt&menuType=T&uId=4&sortChar=A&menuFrame=&linkUrl=4_1.html&mainFrame=right")
driver.implicitly_wait(1)

boards=driver.find_elements_by_css_selector('table.view_bg')
#contents=driver.find_elements_by_class_name("contented")
#links=[content.get_attribute("href") for content in contents]


for board in boards:
    board_contents.append(board.text)  #NOTICE 게시판에서 게시글 폴더별로 분류해둔 부분
    url=board.get_attribute("href")
    urls.append(url)
print(board_contents)
print(urls)



