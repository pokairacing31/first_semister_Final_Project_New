import requests, json
'''
headers = {'Authorization':'Bearer PVhXkRB7hY5R470z02FQFSfUw//UPXQTcunQgGIkWyWSC2H6cYuea+Za982gv+2Y80+ygDI0U9Js73vuKWSOlxYuToAqH9n/UYjWmciA2OA1LrLKQh5Ya9kCPZqJHEOrEzenVAbC6CscBTGOwehGpQdB04t89/1O/w1cDnyilFU=','Content-Type':'application/json'}

body = {
    'size': {'width': 2500, 'height': 1600},   # 設定尺寸
    'selected': 'true',                        # 預設是否顯示
    'name': 'find_house',                             # 選單名稱 ( 別名 Alias Id )
    'chatBarText': '貼身助理',                    # 選單在 LINE 顯示的標題
    'areas':[                                  # 選單內容
        {
          'bounds': {'x': 0, 'y':0, 'width': 830, 'height': 790},
          'action': {'type': 'postback', 'data':'food'}          # 按鈕 A 使用 postback
        },
        {
          'bounds': {'x': 833, 'y':0, 'width': 830, 'height': 790},
          'action': {'type': 'postback', 'data':'clothes'}          # 按鈕 A 使用 postback
        },
        {
          'bounds': {'x': 1666, 'y':0, 'width': 830, 'height': 790},
          'action': {'type': 'postback', 'data':'house'}          # 按鈕 A 使用 postback
        },
        {
          'bounds': {'x': 0, 'y':800, 'width': 830, 'height': 790},
          'action': {'type': 'postback', 'data':'transport'}          # 按鈕 A 使用 postback
        },
        {
          'bounds': {'x': 833, 'y':800, 'width': 830, 'height': 790},
          'action': {'type': 'postback', 'data':'trans'}          # 按鈕 A 使用 postback
        },
        {
          'bounds': {'x': 1666, 'y': 800, 'width': 830, 'height': 790},
          'action': {'type': 'postback', 'data':'unset'}          # 按鈕 A 使用 postback
        }
        
    ]
  }
req = requests.request('POST', 'https://api.line.me/v2/bot/richmenu',
                      headers=headers,data=json.dumps(body).encode('utf-8'))
print(req.text)

from linebot import LineBotApi, WebhookHandler
line_bot_api = LineBotApi('PVhXkRB7hY5R470z02FQFSfUw//UPXQTcunQgGIkWyWSC2H6cYuea+Za982gv+2Y80+ygDI0U9Js73vuKWSOlxYuToAqH9n/UYjWmciA2OA1LrLKQh5Ya9kCPZqJHEOrEzenVAbC6CscBTGOwehGpQdB04t89/1O/w1cDnyilFU=')
with open("C:/python/Final_Project/richmenu_1654671468094.jpg", 'rb') as f:
    line_bot_api.set_rich_menu_image("richmenu-6c1aa48f7f5e464344b40b3e97f256e4", "image/jpeg", f)


import requests
import json
headers = {'Authorization':'Bearer PVhXkRB7hY5R470z02FQFSfUw//UPXQTcunQgGIkWyWSC2H6cYuea+Za982gv+2Y80+ygDI0U9Js73vuKWSOlxYuToAqH9n/UYjWmciA2OA1LrLKQh5Ya9kCPZqJHEOrEzenVAbC6CscBTGOwehGpQdB04t89/1O/w1cDnyilFU=','Content-Type':'application/json'}
body = {
    "richMenuAliasId":"welcome_ma",
    "richMenuId":"richmenu-6c1aa48f7f5e464344b40b3e97f256e4"
}
req = requests.request('POST', 'https://api.line.me/v2/bot/richmenu/alias',
                      headers=headers,data=json.dumps(body).encode('utf-8'))
print(req.text)

'''
import requests
headers = {"Authorization":"Bearer PVhXkRB7hY5R470z02FQFSfUw//UPXQTcunQgGIkWyWSC2H6cYuea+Za982gv+2Y80+ygDI0U9Js73vuKWSOlxYuToAqH9n/UYjWmciA2OA1LrLKQh5Ya9kCPZqJHEOrEzenVAbC6CscBTGOwehGpQdB04t89/1O/w1cDnyilFU=","Content-Type":"application/json"}
req = requests.request('POST', 'https://api.line.me/v2/bot/user/all/richmenu/richmenu-6c1aa48f7f5e464344b40b3e97f256e4', headers=headers)
print(req.text)

'''
from linebot import LineBotApi, WebhookHandler
line_bot_api = LineBotApi('PVhXkRB7hY5R470z02FQFSfUw//UPXQTcunQgGIkWyWSC2H6cYuea+Za982gv+2Y80+ygDI0U9Js73vuKWSOlxYuToAqH9n/UYjWmciA2OA1LrLKQh5Ya9kCPZqJHEOrEzenVAbC6CscBTGOwehGpQdB04t89/1O/w1cDnyilFU=')
line_bot_api.delete_rich_menu('richmenu-150170f2caa39496099b29389873f4a3')

rich_menu_list = line_bot_api.get_rich_menu_list()
print(rich_menu_list)
'''