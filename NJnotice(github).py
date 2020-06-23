
from fbchat import Client
import pyautogui
import requests
import re
from bs4 import BeautifulSoup
import schedule

import time


njpeople = ['전송할 사람 명단']


id = '계정 아이디'
pw = '비번'

pyautogui.alert(title='남주고 알림이', text='알림이 계정에 접속하는 중입니다 잠시만 기다려주세요.')
try:
	fc = Client(id, pw)
except:
        fc = Client(id, pw)

print('로그인 완료.')
msg = pyautogui.prompt(title='남주고 알림이', text='공지내용을 입력해주세요')


i = 0
while i < len(njpeople):
        try:
                to = fc.searchForUsers(njpeople[i])[0]
                fc.sendMessage('[알림이] 자동공지가 도착했어요!\n\n'+msg, thread_id=to.uid)
                print('\n['+njpeople[i]+']공지전송 완료.')
        except:
                print('    ['+njpeople[i]+']<<수신자 식별 오류로 건너띄어집니다.')
        i+=1
                
