from flask import Flask, request, abort

from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import (MessageEvent, TextMessage, TextSendMessage,
                            FlexSendMessage, PostbackEvent)

import re
import json
from line_select_area import area_selector
from line_select_type import type_selector
from line_show_house import house_show
from line_translate import trans
from line_food import food
from line_transport import transport
from line_clothes import clothes

app = Flask(__name__)

line_bot_api = LineBotApi(
    'PVhXkRB7hY5R470z02FQFSfUw//UPXQTcunQgGIkWyWSC2H6cYuea+Za982gv+2Y80+ygDI0U9Js73vuKWSOlxYuToAqH9n/UYjWmciA2OA1LrLKQh5Ya9kCPZqJHEOrEzenVAbC6CscBTGOwehGpQdB04t89/1O/w1cDnyilFU='
)
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
        print(
            "Invalid signature. Please check your channel access token/channel secret."
        )
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    reply3 = trans()
    if event.message.text == '1':
        line_bot_api.reply_message(
            event.reply_token,
            FlexSendMessage(alt_text='選擇語言',
                            contents=reply3.select_language()))
    else:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=reply3.translate(event.message.text)))


@handler.add(PostbackEvent)
def handel_message(event):
    reply = area_selector()
    reply1 = type_selector()
    reply2 = house_show()
    reply3 = trans()
    reply_food = food()
    reply_transport = transport()
    reply_clothes = clothes()

    if reply.is_area_selector(event.postback.data):
        line_bot_api.reply_message(
            event.reply_token,
            FlexSendMessage(alt_text='選擇校區',
                            contents=reply.area(event.postback.data)))
    if reply1.is_type_selector(event.postback.data):
        line_bot_api.reply_message(
            event.reply_token,
            FlexSendMessage(alt_text='選擇種類',
                            contents=reply1.select_type(event.postback.data)))
    if reply2.is_show_house(event.postback.data):
        line_bot_api.reply_message(
            event.reply_token,
            FlexSendMessage(alt_text='好租，讓我們一起更好租',
                            contents=reply2.show_house_carousel(
                                event.postback.data)))
    if reply3.is_trans(event.postback.data):
        line_bot_api.reply_message(
            event.reply_token,
            FlexSendMessage(alt_text='選擇語言',
                            contents=reply3.select_language(
                                event.postback.data)))
    if reply3.is_set_lang(event.postback.data):
        reply3.set_language(event.postback.data)
        line_bot_api.reply_message(event.reply_token,
                                   TextSendMessage(text='已為您設定語言，輸入即可開始翻譯'))
    if reply_food.is_food_area(event.postback.data):
        line_bot_api.reply_message(
            event.reply_token,
            FlexSendMessage(alt_text='選擇校區',
                            contents=reply_food.area_template(
                                event.postback.data)))
    if reply_food.is_food_type(event.postback.data):
        line_bot_api.reply_message(
            event.reply_token,
            FlexSendMessage(alt_text='選擇種類',
                            contents=reply_food.food_type_template(
                                event.postback.data)))
    if reply_food.is_show_food(event.postback.data):
        line_bot_api.reply_message(
            event.reply_token,
            FlexSendMessage(alt_text='選擇種類',
                            contents=reply_food.show_carousel(
                                event.postback.data)))
    if reply_transport.is_transport_area(event.postback.data):
        line_bot_api.reply_message(
            event.reply_token,
            FlexSendMessage(alt_text='選擇校區',
                            contents=reply_transport.area_template(
                                event.postback.data)))
    if reply_transport.is_transport_type(event.postback.data):
        line_bot_api.reply_message(
            event.reply_token,
            FlexSendMessage(alt_text='選擇交通工具',
                            contents=reply_transport.type_template(
                                event.postback.data)))
    if reply_transport.is_show_transport(event.postback.data):
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(
                text=reply_transport.transport_data(event.postback.data)))
    if reply_clothes.is_clothes_area(event.postback.data):
        line_bot_api.reply_message(
            event.reply_token,
            FlexSendMessage(alt_text='選擇校區',
                            contents=reply_clothes.area_template(
                                event.postback.data)))
    if reply_clothes.is_show_clothes(event.postback.data):
        line_bot_api.reply_message(
            event.reply_token,
            FlexSendMessage(alt_text='顯示店家',
                            contents=reply_clothes.show_house_carousel(
                                event.postback.data)))



if __name__ == "__main__":
    app.run("0.0.0.0", port=80)
