# 셀리니움_웹드라이버_네이버로그인.py ( 주소를 보여주지 않는 사이트에서 사용 )
# pip install clipboard  # cmd 창에서 설치함
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import clipboard  # clipboard : 아이디 패스워드 입력하는 약간의 시간차를 두고 싶을 때 ( 기다림 )
import time  # time : 

driver = webdriver.Chrome(ChromeDriverManager().install())  
driver.get('https://nid.naver.com/nidlogin.login')  # 네이버에 로그인하는 페이지

# 네이버 메인화면에서 로그인 버튼 클릭
# driver.find_element_by_xpath('//*[@id="account"]/a').click()
# time.sleep(1)   # 1초 시간 지연

# 로그인 창에 아이디/비밀번호 입력
loginID = "kim"  # 본인 아이디
clipboard.copy(loginID)   # 클립보드에 담아놓음
#mac은 COMMAND, window는 CONTROL
driver.find_element(By.XPATH,'//*[@id="id"]').send_keys(Keys.CONTROL, 'v')

loginPW = "1234"  # 본인 비번
clipboard.copy(loginPW)
driver.find_element(By.XPATH,'//*[@id="pw"]').send_keys(Keys.CONTROL, 'v')
time.sleep(1)

# 로그인 버튼 클릭
driver.find_element(By.XPATH,'//*[@id="log.login"]').click()

while True:
    pass 