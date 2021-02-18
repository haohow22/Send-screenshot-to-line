'''
可以直接截圖，用Line Notify發訊息
可以用路徑 P:/Python/screenshots/P_
新增Timer
'''

import time
import os
import requests
import schedule

from PIL import ImageGrab
from dotenv import load_dotenv

load_dotenv()
LINE_TOKEN = os.getenv("LINE_NOTIFY_TOKEN")
MESSAGE_CONTENT = os.getenv("MESSAGE_CONTENT_ENV")
SHORTCUT_SAVEPATH = os.getenv("SAVEPATH")
# PICTUREQuality = os.getenv("PICTURE_Quality")
# 截圖
def grab(timeString):
    img = ImageGrab.grab()
    img.save(SHORTCUT_SAVEPATH + timeString + ".jpg", quality=50)

# 發送 Line Notify 訊息
def sendLineNotify(msg, picURI):
    url = "https://notify-api.line.me/api/notify"
    headers = {
        "Authorization": "Bearer " + LINE_TOKEN
    }

    payload = { 'message': msg }
    files = { 'imageFile': open(picURI, 'rb') }
    #執行傳送
    requests.post(url, headers = headers, params = payload, files = files)

# 當開啟程式，送訊息及圖片
def grabAndSendNotify1st():
    # print("Token: " + LINE_TOKEN)
    print("裝置名稱: " + MESSAGE_CONTENT)
    print("存檔位置: " + SHORTCUT_SAVEPATH)
    print("請縮小視窗，5秒後自動截圖並傳送") 
    i=0
    while i <= 5 :
        print(5-i)
        i=i+1
        time.sleep(1)
    
    time_string = time.strftime("%Y-%m-%d_%H-%M-%S")
    grab(time_string)
    msg =  " ***截圖已啟動*** "  + time_string
    pic_url = (SHORTCUT_SAVEPATH + time_string + ".jpg")
    sendLineNotify(msg, pic_url)
    print(MESSAGE_CONTENT + " ***截圖已啟動*** ") 
    print("傳送時間: " + time_string ) 

def grabAndSendNotify():
    time_string = time.strftime("%Y-%m-%d_%H-%M-%S")
    grab(time_string)

    msg = MESSAGE_CONTENT + " " + time_string
    pic_url = (SHORTCUT_SAVEPATH + time_string + ".jpg")
    sendLineNotify(msg, pic_url)
    print("傳送時間: " + time_string ) 


schedule.every(20).seconds.do(grabAndSendNotify)    #測試20秒送訊息
'''
# Monday
schedule.every().monday.at('08:45').do(grabAndSendNotify)
schedule.every().monday.at('13:46').do(grabAndSendNotify)
# Tuesday
schedule.every().tuesday.at('05:01').do(grabAndSendNotify)
schedule.every().tuesday.at('08:45').do(grabAndSendNotify)
schedule.every().tuesday.at('13:46').do(grabAndSendNotify)
# Wednesday
schedule.every().wednesday.at('05:01').do(grabAndSendNotify)
schedule.every().wednesday.at('08:45').do(grabAndSendNotify)
schedule.every().wednesday.at('13:46').do(grabAndSendNotify)
# Thursday
schedule.every().thursday.at('05:01').do(grabAndSendNotify)
schedule.every().thursday.at('08:45').do(grabAndSendNotify)
schedule.every().thursday.at('13:46').do(grabAndSendNotify)
# Friday
schedule.every().friday.at('05:01').do(grabAndSendNotify)
schedule.every().friday.at('08:45').do(grabAndSendNotify)
schedule.every().friday.at('13:46').do(grabAndSendNotify)
# Saturday
schedule.every().saturday.at('05:01').do(grabAndSendNotify)
'''
def main_loop():
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == '__main__':
    grabAndSendNotify1st()
    main_loop()
