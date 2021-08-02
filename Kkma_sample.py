from selenium import webdriver
from konlpy.tag import Kkma
driver=webdriver.Chrome("/chromedriver")
driver.implicitly_wait(1)

#go to the login page & login

driver.get("https://everytime.kr/login")
driver.find_element_by_name("userid").send_keys("*")
driver.find_element_by_name("password").send_keys("*")
driver.find_element_by_xpath('//*[@class="submit"]/input').click()
driver.implicitly_wait(1)

main_results=[] #본문

page=4

driver.get("https://everytime.kr/382452/p/"+str(page))
driver.implicitly_wait(1)

#get articles link
posts=driver.find_elements_by_css_selector("article > a.article")
links=[post.get_attribute("href") for post in posts]

#get detail article
for link in links:
    driver.get(link)

#본문
    main_articles=driver.find_elements_by_css_selector("p.large")


    for main_article in main_articles:   #본문만 추출할 수 있는 html경로를 파악하지 못 해서 본문과 댓글을 우선 전체 크롤링
        main_results.append(main_article.text)   #main_results -> 본문+댓글 리스트





for i in range(len(main_results)):
    kkma=Kkma()
    print("형태소 분석")
    print(kkma.morphs(main_results[i]))

    print("\n명사만")
    print(kkma.nouns(main_results[i]))
    print("\n")

    i+=1
