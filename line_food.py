from linebot.models import FlexSendMessage, BubbleContainer, BoxComponent, TextComponent, ButtonComponent, PostbackAction, BlockStyle, CarouselContainer, IconComponent, ImageComponent, URIAction
import requests
from bs4 import BeautifulSoup
import json
from urllib import response
import pandas as pd
import requests, re, json
from bs4 import BeautifulSoup


class food():

    def food_kind(self):
        food_kind_list = [
            '日式料理', '韓式料理', '美式料理', '義式料理', '中式料理', '泰式料理', '港式料理'
        ]
        return food_kind_list

    def select_food_list(self, code):
        if code == 'zz':
            menu_list = [['日式料理', 'z_jp'], ['韓式料理', 'z_ko'], ['美式料理', 'z_us'],
                         ['義式料理', 'z_it'], ['中式料理', 'z_ch'], ['泰式料理', 'z_th'],
                         ['港式料理', 'z_hk']]
            print('zz')
        else:
            menu_list = [['日式料理', 's_jp'], ['韓式料理', 's_ko'], ['美式料理', 's_us'],
                         ['義式料理', 's_it'], ['中式料理', 's_ch'], ['泰式料理', 's_th'],
                         ['港式料理', 's_hk']]
            print('ss')
        button_list = []
        for menu in menu_list:
            button_list.append(
                ButtonComponent(action=PostbackAction(label=menu[0],
                                                      data=menu[1]),
                                height='md',
                                color='#FFB5B5',
                                style='primary',
                                margin='xs'))
        print(button_list)
        return button_list

    def food_crawler_elem(self, code):
        code_list = code.split('_')
        food_elem_list = []
        if code_list[0] == 'z':
            area = '中正區'
        else:
            area = '士林區'
        food_elem_list.append(area)
        if code_list[1] == 'jp':
            type = '日本料理'
        elif code_list[1] == 'ko':
            type = '韓式料理'
        elif code_list[1] == 'us':
            type = '美式料理'
        elif code_list[1] == 'it':
            type = '義式料理'
        elif code_list[1] == 'ch':
            type = '中式料理'
        elif code_list[1] == 'th':
            type = '泰式料理'
        elif code_list[1] == 'hk':
            type = '港式料理'
        food_elem_list.append(type)

        return food_elem_list

    def food_crawler(self, code):
        food_body_elem = []
        food_elem_list = self.food_crawler_elem(code)
        url = 'https://ifoodie.tw/explore/台北市/' + food_elem_list[
            0] + '/list/' + food_elem_list[1] + '?sortby=rating'
        resp = requests.get(url)
        resp.encoding = 'utf-8'
        print('網頁下載中...')
        resp.raise_for_status()
        print('網頁下載完成')
        soup = BeautifulSoup(resp.text, 'html.parser')
        article = soup.select('script[type="application/json"]')[0].contents[0]
        results = json.loads(article)
        # print(results.keys())
        final1 = results['props']
        # print(final1.keys())
        final2 = final1['initialState']
        # print(final2.keys())
        final3 = final2['search']
        # print(final3.keys())
        final4 = final3['explore']
        # print(final4.keys())
        final5 = final4['data']
        for i in range(10):
            dic = final5[i]
            res_name = str(dic['name']).strip()
            res_phone = str(dic['phone']).strip()
            res_address = str(dic['address']).strip()
            res_rating = str(dic['rating']).strip()
            res_cover = str(dic['coverUrl']).strip()
            food_elem = [
                res_name, res_phone, res_address, res_rating, res_cover
            ]
            food_body_elem.append(food_elem)
        return food_body_elem

    def show_contents(self, code):
        food_body_list = self.food_crawler(code)
        content_list = []
        for food in food_body_list:
            content = BubbleContainer(
                hero=ImageComponent(url=food[4],
                                    size='full',
                                    aspect_ratio="20:13",
                                    aspect_mode='cover'),
                body=BoxComponent(
                    layout='vertical',
                    contents=[
                        TextComponent(text=food[0], weight='bold', size='xl'),
                        BoxComponent(layout='baseline',
                                     spacing='sm',
                                     contents=[
                                         TextComponent(text='評價',
                                                       color='#aaaaaa',
                                                       size='sm',
                                                       flex=1),
                                         TextComponent(text=food[3],
                                                       wrap=True,
                                                       color='#666666',
                                                       size='sm',
                                                       flex=5)
                                     ]),
                        BoxComponent(layout='baseline',
                                     spacing='sm',
                                     contents=[
                                         TextComponent(text='地址',
                                                       color='#aaaaaa',
                                                       size='sm',
                                                       flex=1),
                                         TextComponent(text=food[2],
                                                       wrap=True,
                                                       color='#666666',
                                                       size='sm',
                                                       flex=5)
                                     ]),
                        BoxComponent(layout='baseline',
                                     spacing='sm',
                                     contents=[
                                         TextComponent(text='電話',
                                                       color='#aaaaaa',
                                                       size='sm',
                                                       flex=1),
                                         TextComponent(text=food[1],
                                                       wrap=True,
                                                       color='#666666',
                                                       size='sm',
                                                       flex=5)
                                     ]),
                    ]),
                footer=BoxComponent(layout='vertical',
                                    spacing='sm',
                                    flex=1,
                                    contents=[
                                        ButtonComponent(
                                            style='link',
                                            height='sm',
                                            action=URIAction(
                                                label='前往詳情',
                                                uri='https://ifoodie.tw/'))
                                    ]))
            content_list.append(content)
        print(content_list)
        return content_list

    def show_carousel(self, code):
        content_list = self.show_contents(code)
        return CarouselContainer(contents=content_list)

    def food_type_template(self, code):
        buttom_list = self.select_food_list(code)
        flex_message = BubbleContainer(
            size='kilo',
            body=BoxComponent(layout='vertical',
                              contents=[
                                  TextComponent(text='選擇種類',
                                                size='xl',
                                                weight='bold')
                              ]),
            footer=BoxComponent(layout='vertical',
                                contents=buttom_list,
                                position='relative'),
            styles={
                'header': BlockStyle(separator=False),
                'body': BlockStyle(Separator=True),
                'footer': BlockStyle(Separator=False)
            })
        print(flex_message)
        return flex_message

    def area_template(self, code):
        flex_message = BubbleContainer(
            size='kilo',
            body=BoxComponent(layout='vertical',
                              contents=[
                                  TextComponent(text='選擇校區',
                                                size='xl',
                                                weight='bold')
                              ]),
            footer=BoxComponent(
                layout='vertical',
                contents=[
                    ButtonComponent(action=PostbackAction(label="城中校區",
                                                          data='zz'),
                                    height='md',
                                    color='#FFB5B5',
                                    style='primary',
                                    margin='xs'),
                    ButtonComponent(action=PostbackAction(label="雙溪校區",
                                                          data='ss'),
                                    height='md',
                                    color='#FFB5B5',
                                    style='primary',
                                    margin='xs')
                ],
                position='relative'),
            styles={
                'header': BlockStyle(separator=False),
                'body': BlockStyle(Separator=True),
                'footer': BlockStyle(Separator=False)
            })
        print(flex_message)
        return flex_message

    def is_food_area(self, code):
        return True if code == 'food' else False

    def is_food_type(self, code):
        area_list = ['zz', 'ss']
        print(code)
        return True if code in area_list else False

    def is_show_food(self, code):
        food_code_list = [
            'z_jp', 'z_ko', 'z_us', 'z_it', 'z_ch', 'z_th', 'z_hk', 's_jp',
            's_ko', 's_us', 's_it', 's_ch', 's_th', 's_hk'
        ]
        return True if code in food_code_list else False


reply = food()
reply.show_contents('z_us')