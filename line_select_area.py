import csv
from tkinter.ttk import Separator
from certifi import contents

from linebot.models import FlexSendMessage, BubbleContainer, BoxComponent, TextComponent, ButtonComponent, PostbackAction, BlockStyle, CarouselContainer

class area_selector():
    def area(self):
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
                    data = 'area_1'
                    ),
                    height = 'md',
                    color = '#FFB5B5',
                    style = 'primary',
                    margin = 'xs'),
                    ButtonComponent(
                    action = PostbackAction(
                    label="雙溪校區",
                    data = 'area_2'
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

    def is_area_selector(self,text):
        return True if "找房" in text else False
    
