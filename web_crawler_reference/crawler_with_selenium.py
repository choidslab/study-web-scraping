import time
import pyperclip

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

WEB_DRIVER_PATH = 'D:/chromedriver.exe'  # Chrome web driver 파일 경로 설정
URL = 'https://nid.naver.com/nidlogin.login'

NAVER_ID = ''  # Naver ID 입력
NAVER_PW = ''  # Naver PW 입력


def input_account_info(xpath, input):
    pyperclip.copy(input)
    driver.find_element_by_xpath(xpath).click()
    ActionChains(driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()  # 키보드 Ctrl + v 수행
    time.sleep(1)


if __name__ == "__main__":

    driver = webdriver.Chrome(WEB_DRIVER_PATH)
    driver.implicitly_wait(1)
    driver.get(URL)

    # ID/PW 입력
    # driver.find_element_by_name('id').send_keys(NAVER_ID)
    # driver.find_element_by_name('pw').send_keys(NAVER_PW)

    input_account_info('//*[@id="id"]', NAVER_ID)
    input_account_info('//*[@id="pw"]', NAVER_PW)
    driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()
