# -*- coding: utf-8 -*-

# 댓글이 없는 글은 포함 x?
# 댓글, 대댓글을 한 리스트에?
# 불용어에 '감사합니다' 반드시 넣기

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time
import csv

# 크롬창 띄우기
options = Options()
options.add_argument("--start-fullscreen")

# 에타 사이트로 이동
driver = webdriver.Chrome("C:/Users/haena/Desktop/chromedriver.exe")
driver.get("https://everytime.kr/")
soup = BeautifulSoup(driver.page_source, "lxml")

# 로그인 버튼 클릭
elem = driver.find_element_by_link_text("로그인")
elem.click()

# 아이디, 비밀번호 입력
id = driver.find_element_by_name('userid')
id.send_keys('haenarang')  # 자신의 아이디 입력
id = driver.find_element_by_name('password')
id.send_keys('andrews701')  # 자신의 비밀번호 입력
id.send_keys(Keys.RETURN)

# 페이지가 로드되기 전 크롤러가 먼저 클릭하는 현상 방지
time.sleep(2.5)

# 에타조교 게시판 들어가기
menu = driver.find_element_by_link_text("더 보기")
menu.click()
jogyo = driver.find_element_by_link_text("에타조교")
jogyo.click()


class Crawler:
    def __init__(self, num):
        self.__count = 1
        self.__page = 1
        self.__num = num
        self.__content, self.__comment = [], []
        self._ar_per_page = 0

    def com_crawl(self):
        for page in range(1, 21):  # 20개의 페이지씩
            time.sleep(1)

            # 첫 페이지 설정 (20개씩 나눠서 진행할 때 11, 21, ..등의 페이지부터 시작할 수 있도록)
            if self._ar_per_page == 0:
                driver.get(f'https://everytime.kr/382452/p/{page}')
                time.sleep(1)

            # 20개의 글 크롤링 했으면 다음 클릭
            if self._ar_per_page == 20:
                daum = driver.find_element_by_link_text("다음")
                daum.click()

            # 초기화
            self._ar_per_page = 0

            for count in range(1, 21):  # 한 페이지당 20개의 글
                try:  # 접근이 안되는 게시글 오류로 인한 실행종료 방지
                    time.sleep(0.5)

                    # 게시글 클릭
                    article = driver.find_element_by_xpath('//*[@id="container"]/div[2]/article[1]/a/p')
                    article.click()
                    time.sleep(1)

                    # 게시글의 내용 크롤링
                    content = driver.find_element_by_xpath('//*[@id="container"]/div[2]/article/a/p').text

                    # 게시글의 댓글 크롤링
                    comment_list = []
                    comment_count = 1

                    while True:
                        try:
                            comment = driver.find_element_by_css_selector(
                                f'#container > div.wrap.articles > article > div > article:nth-child({comment_count}) > p')
                            comment_list.append(comment.text)
                            # print(comment_list)
                            comment_count += 1
                        except:
                            break

                    # '삭제된 댓글입니다.' 제외
                    comment_list = [i for i in comment_list if i != "삭제된 댓글입니다."]

                    self._content.append(content)
                    self.comment.append(comment_list)

                    driver.back()

                    self._ar_per_page += 1

                except:
                    self._ar_per_page += 1
                    continue

            print("크롤링 완료")
            driver.quit()

            return self._content, self._comment


c = Crawler(10)  # 일단 한 번 10개까지 결과물을 뽑아보고자 하는 코드
result = c.com_crawl()
print(result)

print(list(zip(*result)), len(list(zip(*result))))

# eta_jogyo 파일 생성
with open('eta_jogyo.csv', 'w', encoding='utf-8-sig', newline='') as f:
    writer = csv.writer(f)
    for i in list(zip(*result)):
        writer.writerow(i)