
from linebot.models import FlexSendMessage, BubbleContainer, BoxComponent, TextComponent, ButtonComponent, PostbackAction, BlockStyle, CarouselContainer, IconComponent, ImageComponent, URIAction
import requests
from bs4 import BeautifulSoup
import json
from urllib import response
import csv
import requests, re, json
from bs4 import BeautifulSoup

import googlemaps
import requests
import json
import pandas as pd


class clothes():

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
                                                          data='z_c'),
                                    height='md',
                                    color='#FFB5B5',
                                    style='primary',
                                    margin='xs'),
                    ButtonComponent(action=PostbackAction(label="雙溪校區",
                                                          data='s_c'),
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

    def csv_reader(self, code):
        shop_list=[]
        if code == 'z_c':
            path = 'Final_Project\clothes_shop_zz.csv'
        elif code == 's_c':
            path = 'Final_Project\clothes_shop_ss.csv'
        with open(path, newline='', encoding='utf-8') as csvfile:
            rows = csv.reader(csvfile)
            datas = list(rows)
        for data in datas[1:]:
            name = data[5]
            open_houers = data[6][13:-1]
            rating = data[10]
            address = data[15]
            users = data[-2]
            data_list = [name,open_houers,rating,address,users]
            shop_list.append(data_list)
        print(shop_list)
        return shop_list
    def show_template(self,code):
        datas = self.csv_reader(code)
        template_list =[]
        for data in datas: 
            content = BubbleContainer(
                body=BoxComponent(
                    layout='vertical',
                    contents=[
                        TextComponent(
                            text=data[0],
                            weight='bold',
                            size='xl',
                            wrap=True
                        ),
                        BoxComponent(
                            layout='baseline',
                            margin='md',
                            contents=[
                                TextComponent(
                                    text='評價',
                                    color='#aaaaaa',
                                    size='sm',
                                    flex=2
                                ),
                                TextComponent(
                                    text=data[2],
                                    wrap=True,
                                    color='#666666',
                                    size='sm',
                                    flex=2
                                )
                            ]
                        ),
                        BoxComponent(
                            layout='baseline',
                            margin='md',
                            contents=[
                                TextComponent(
                                    text='地址',
                                    color='#aaaaaa',
                                    size='sm',
                                    flex=2
                                ),
                                TextComponent(
                                    text=data[3],
                                    wrap=True,
                                    color='#666666',
                                    size='sm',
                                    flex=2
                                )
                            ]
                        ),
                        BoxComponent(
                            layout='baseline',
                            margin='md',
                            contents=[
                                TextComponent(
                                    text='營業中',
                                    color='#aaaaaa',
                                    size='sm',
                                    flex=2
                                ),
                                TextComponent(
                                    text=data[1],
                                    wrap=True,
                                    color='#666666',
                                    size='sm',
                                    flex=2
                                )
                            ]
                        ),
                        BoxComponent(
                            layout='baseline',
                            margin='md',
                            contents=[
                                TextComponent(
                                    text='評論人數',
                                    color='#aaaaaa',
                                    size='sm',
                                    flex=2
                                ),
                                TextComponent(
                                    text=data[-1],
                                    wrap=True,
                                    color='#666666',
                                    size='sm',
                                    flex=2
                                )
                            ]
                        )
                    ]
                ),
                footer=BoxComponent(
                    layout='vertical',
                    contents=[
                        ButtonComponent(
                            action=URIAction(
                                label='前往  google map',
                                uri='https://www.google.com.tw/maps'
                            )
                            
                        )
                    ]
                )
            )
            template_list.append(content)
        print(template_list)
        return template_list

    def show_house_carousel(self,code):
        carousel_list = self.show_template(code)
        return CarouselContainer(contents=carousel_list[0:10])
            

    def is_show_clothes(self,code):
        show_list=['z_c','s_c']
        return True if code in show_list else False
    def is_clothes_area(self, code):
        return True if code == 'clothes' else False


