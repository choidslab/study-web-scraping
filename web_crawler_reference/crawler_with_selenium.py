import pyperclip
from selenium import webdriver

WEB_DRIVER_PATH = 'D:/chromedriver.exe'
URL = 'https://nid.naver.com/nidlogin.login'

NAVER_ID = ''
NAVER_PW = ''

driver = webdriver.Chrome(WEB_DRIVER_PATH)
# driver.implicitly_wait(3)
driver.get(URL)

# ID/PW 입력
driver.find_element_by_name('id').send_keys(NAVER_ID)
driver.find_element_by_name('pw').send_keys(NAVER_PW)

# Login 버튼 클릭
driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()
