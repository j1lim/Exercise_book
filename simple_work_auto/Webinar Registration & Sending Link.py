#!/usr/bin/env python
# coding: utf-8

# In[1]:

import time
import gspread
import win32com.client
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds",
         "https://www.googleapis.com/auth/drive",]

# JSON Key File Path
json_key_path = "C:/Users/limjw/OneDrive/바탕 화면/j1lim/HRU/google_api/massive-oasis-357803-325743f36cb3.json"

credential = ServiceAccountCredentials.from_json_keyfile_name(json_key_path, scope)
gc = gspread.authorize(credential)

# URL로 열기
spreadsheet_url = "https://docs.google.com/spreadsheets/d/1QjtdghWeypM-vGUkQADaDkJUEljV44IPViFeR43zvvM/edit#gid=1134538840"
doc = gc.open_by_url(spreadsheet_url)

# Sheet 선택 (이름)
sheet = doc.worksheet("설문지 응답 시트1")

#새로운 열 추가
#sheet.update_acell('K1', "링크 발송 여부")


# In[2]:

while True:
    # 모든 값을 dict로 가져오기
    list_of_dicts = sheet.get_all_records()
    #print(len(list_of_dicts))
    
    dic_to_send = {}
    for x in range(len(list_of_dicts)):
        tmp_dic = list_of_dicts[x]
        #print(tmp_dic)
        
        if tmp_dic["링크 발송 여부"] != "YES":
            dic_to_send[tmp_dic["이름"]] = tmp_dic["이메일"]
            tmp_cell = 'K%s' % (x + 2)
            sheet.update_acell(tmp_cell, "YES")
            time.sleep(2)
        else:
            continue
            
    print(len(dic_to_send))
    #print(dic_to_send)
    
    
    
    #메일 제목
    mail_subject = "BC Platforms 웨비나 녹화 비디오"
    #메일 본문
    mail_body = """
    <a href="https://info.bcplatforms.com/lp-cmp-precision-medicine-and-data-science-seminar-singapore-2022-recordings-all" target="_blank">
      <img src="C:/Users/limjw/Downloads/asd.png">
    </a>
    <br><br>
    <span style=" font-size: x-small; color: #333333;">
    HELiXⓇUS, Inc.
    </span>
    <br><br>
    <span style=" font-size: x-small; color: #333333;">
    B1714 Jong-ro 19, Jongno-gu, Seoul, Korea 03157
    </span>
    <br><br>
    <span style=" font-size: x-small; color: #333333;">
    Phone: +82-2-730-8850
    </span>
    <br>
    <span style=" font-size: x-small; color: #333333;">
    Fax: +82-2-730-8851
    </span>
    <br>
    <span style=" font-size: x-small; color: #333333;">
    Email: info@helixrus.com
    </span>
    """

    for k, v in dic_to_send.items():
        #수신자 정보
        mail_To = v

        obj = win32com.client.Dispatch("Outlook.Application")
        newMail = obj.CreateItem(0)

        #메일 제목
        newMail.Subject = mail_subject
        #메일 HTML 본문
        newMail.HTMLBody = mail_body
        #수신자
        newMail.To = mail_To
        #참조자
        newMail.CC = mail_CC
        
        #메일 내용 확인하기
        newMail.Display(True)
        #메일 보내기
        #newMail.Send()
        
        break
    
    break
    #1시간에 한번 체크
    time.sleep(3600)
