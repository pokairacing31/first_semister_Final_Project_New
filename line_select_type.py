import csv
from tkinter.ttk import Separator


from linebot.models import FlexSendMessage, BubbleContainer, BoxComponent, TextComponent, ButtonComponent, PostbackAction, BlockStyle, CarouselContainer

class type_selector():
    def select_footer_list(self,code):
        if code == 'area_1':
            menu_list = [['整層住家','z_t_1'],['獨立套房','z_t_2'],['分租套房','z_t_3'],['雅房','z_t_4']]
        else:
            menu_list = [['整層住家','s_t_1'],['獨立套房','s_t_2'],['分租套房','s_t_3'],['雅房','s_t_4']]
        buttom_list=[]
        for menu in menu_list:
            buttom_list.append(
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
        return buttom_list
    def select_type(self,code):
        buttom_list = self.select_footer_list(code)
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
                    contents=buttom_list,
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
    
    def is_type_selector(self,code):
        return True if  code == 'area_1' or code == 'area_2' else False