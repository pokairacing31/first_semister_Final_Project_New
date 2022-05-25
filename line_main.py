from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,FlexSendMessage,PostbackEvent
)

import re
import json
from line_select_area import area_selector
from line_select_type import type_selector
from line_show_house import house_show


app = Flask(__name__)

line_bot_api = LineBotApi('PVhXkRB7hY5R470z02FQFSfUw//UPXQTcunQgGIkWyWSC2H6cYuea+Za982gv+2Y80+ygDI0U9Js73vuKWSOlxYuToAqH9n/UYjWmciA2OA1LrLKQh5Ya9kCPZqJHEOrEzenVAbC6CscBTGOwehGpQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('269a7c0ab431de6b327b6ffca0d51f75')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    reply = area_selector()
    if reply.is_area_selector(event.message.text):
        line_bot_api.reply_message(
            event.reply_token,
            FlexSendMessage(alt_text='選擇校區',contents=reply.area())
        )
@handler.add(PostbackEvent)
def handel_message(event):
    reply = type_selector()
    reply2 = house_show()
    if reply.is_type_selector(event.postback.data):
        line_bot_api.reply_message(
            event.reply_token,
            FlexSendMessage(alt_text='選擇種類',contents=reply.select_type(event.postback.data))
        )
    if reply2.is_show_house(event.postback.data):
        line_bot_api.reply_message(
            event.reply_token,
            FlexSendMessage(alt_text='好租，讓我們一起更好租',contents=reply2.show_house_carousel(event.postback.data))
        )
    

    


if __name__ == "__main__":
    app.run("0.0.0.0",port=80)