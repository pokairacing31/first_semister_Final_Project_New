from linebot.models import FlexSendMessage, BubbleContainer, BoxComponent, TextComponent, ButtonComponent, PostbackAction, BlockStyle, CarouselContainer,IconComponent,ImageComponent,URIAction
import requests
from bs4 import BeautifulSoup
import json
from urllib import response

import requests,re,json
from bs4 import BeautifulSoup

class transport():
    def area_template(self,code):
        flex_message = BubbleContainer(
            size='kilo',
            body=BoxComponent(
                layout = 'vertical',
                contents = [
                    TextComponent(
                        text = '選擇校區',
                        size = 'xl',
                        weight = 'bold'
                    )
                ]
            ),
            footer=BoxComponent(
                layout = 'vertical',
                contents = [
                    ButtonComponent(
                    action = PostbackAction(
                    label="城中校區",
                    data = 'z'
                    ),
                    height = 'md',
                    color = '#FFB5B5',
                    style = 'primary',
                    margin = 'xs'),
                    ButtonComponent(
                    action = PostbackAction(
                    label="雙溪校區",
                    data = 's'
                    ),
                    height = 'md',
                    color = '#FFB5B5',
                    style = 'primary',
                    margin = 'xs')
                    ],
                position = 'relative'
            ),
            styles={
                'header': BlockStyle(separator=False),
                'body':BlockStyle(Separator = True),
                'footer':BlockStyle(Separator = False)
            }
        )
        print(flex_message)
        return flex_message
    def select_type_list(self,code):
        if code == 'z':
            menu_list = [['公車','z_bus'],['捷運','z_mrt'],['鐵路','z_train'],['開車','z_car']]
        else:
            menu_list = [['公車','s_bus'],['捷運','s_mrt'],['鐵路','s_train'],['開車','s_car']]
        button_list=[]
        for menu in menu_list:
            button_list.append(
                ButtonComponent(
                action=PostbackAction(
                label = menu[0],
                data = menu[1]
                ),
                height='md',
                color='#FFB5B5',
                style='primary',
                margin = 'xs'
            ))
        print(button_list)
        return button_list

    def type_template(self,code):
        button_list = self.select_type_list(code)
        flex_message = BubbleContainer(
            size='kilo',
            body=BoxComponent(
                layout = 'vertical',
                contents = [
                    TextComponent(
                        text = '選擇種類',
                        size = 'xl',
                        weight = 'bold'
                    )
                ]
            ),
            footer=BoxComponent(
                    layout='vertical',
                    contents=button_list,
                    position='relative'
            ),
            styles={
                'header': BlockStyle(separator=False),
                'body':BlockStyle(Separator = True),
                'footer':BlockStyle(Separator = False)
            }
        )
        print(flex_message)
        return flex_message

    def transport_data(self,code):
        code_list = code.split('_')
        if code_list[0]=='s':
            if code_list[1] == 'bus':
                data = '557（東吳大學）\n\n、255、268、300、304、620、645、680、681、683、957、小18、小19、市民小巴1、紅30（東吳大學_錢穆故居）\n\n、棕13、棕20(外雙溪_故宮)'
            elif code_list[1] == 'mrt':
                data = '捷運淡水線至士林站，往中正路出口，再轉搭公車255、300、304、620、683、957、小18、小19、市民小巴1、紅30至東吳大學_錢穆故居站下車；或557至東吳大學站下車\n\n捷運文湖線至大直站，往北安路出口再轉搭公車680至東吳大學_錢穆故居站下車；或棕13至外雙溪_故宮站下車\n\n捷運文湖線至劍南路站，往北安路出口再轉搭公車681至東吳大學_錢穆故居站下車；或棕20至外雙溪_故宮站下車'
            elif code_list[1] == 'train':
                data = '至台北車站下車，轉乘捷運至士林站，往中正路出口，再轉搭公車255、300、304、620、683、957、小18、小19、市民小巴1、紅30至東吳大學_錢穆故居站下車；或557至東吳大學站下車'
            else:
                data='中山高速公路-->重慶北路交流道（往士林方向）-->重慶北路四段-->百齡橋-->中正路-->至善路-->外雙溪校區\n\n北二高-->堤頂交流道-->往左至內湖路（內湖大直方向）-->自強隧道-->至善路-->外雙溪校區'
        else:
            if code_list[1] == 'bus':
                data='1503、235、270、38、662、663（東吳大學城中校區站）\n\n12、20、202、205、212、218、223、234、246、250、253、260、265、302、307、310、604、651、9、956、仁愛幹線、藍29、重慶幹線（小南門）\n\n252、262、262區、304、38、604、660（捷運小南門站）'
            elif code_list[1] == 'mrt':
                data = '至小南門（1號出口）或西門站（2號出口）下車，步行即至'
            elif code_list[1] == 'train':
                data = '至台北車站下車，搭乘捷運至小南門（1號出口）或西門站（2號出口）下車，步行即至'
            else:
                data = '中山高速公路-->重慶北路交流道（往台北市區方向）-->重慶北路三段-->重慶南路-->貴陽街-->城中校區\n\n北二高-->木柵交流道-->辛亥路-->羅斯福路-->中山南路-->凱達格蘭大道-->重慶南路-->貴陽街-->城中校區'
        return data
    def is_transport_area(self,code):
        return True if code =='transport'else False 
    def is_transport_type(self,code):
        area = ['z','s']
        return True if code in area else False
    def is_show_transport(self,code):
        type = ['z_bus','z_mrt','z_train','z_car','s_bus','s_mrt','s_train','s_car']
        return True if code in type else False

reply = transport()
reply.transport_data('z_bus')