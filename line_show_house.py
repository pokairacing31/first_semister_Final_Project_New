import csv

from linebot.models import FlexSendMessage, BubbleContainer, BoxComponent, TextComponent, ButtonComponent, PostbackAction, BlockStyle, CarouselContainer,ImageComponent,URIAction

class house_show():
    def csv_reader(self,code):
        if code == 'z_t_1':
            path = 'zhongzheng_flat_output.csv'
        elif code == 'z_t_2':
            path = 'zhongzheng_indep_suite_output.csv'
        elif code == 'z_t_3':
            path = 'zhongzheng_sublet_output.csv'
        elif code == 'z_t_4':
            path = 'zhongzheng_soloroom_output.csv'
        elif code == 's_t_1':
            path = 'shilin_flat_output.csv'
        elif code == 's_t_2':
            path = 'shilin_indep_suite_output.csv'
        elif code == 's_t_3':
            path = 'shilin_sublet_output.csv'
        elif code == 's_t_4':
            path = 'shilin_soloroom_output.csv'
        with open (path, newline='', encoding='utf-8') as csvfile:
            rows = csv.reader(csvfile)
            datas = list(rows)
        return datas
    def get_body_list(self,code):
        datas = self.csv_reader(code)
        body_list = []
        n=1
        for data in datas[1:9]:
            body_obj = BoxComponent(
                                    layout='baseline',
                                    spacing= 'sm',
                                    contents=[
                                        TextComponent(
                                            text=datas[0][n],
                                            color='#aaaaaa',
                                            size='sm',
                                            flex=1
                                        ),
                                        TextComponent(
                                            text=data[n],
                                            wrap=True,
                                            color='#666666',
                                            size='sm',
                                            flex=5
                                        )
                                    ]           
            )
            body_list.append(body_obj)
            n+=1
        return body_list



    def get_carousel_list(self,code):
        datas = self.csv_reader(code)
        body_list = self.get_body_list(code)
        carousel_list = []
        for data in datas[1:10]:
            flex_message_card=BubbleContainer(
                            size='kilo',
                            hero=ImageComponent(
                                url = data[9],
                                size = 'full',
                                aspect_ratio= "20:13",
                                aspect_mode= "cover",
                                ),
                            body=BoxComponent(
                                layout='vertical',
                                contents=[
                                    TextComponent(
                                        text=data[0],
                                        weight='bold',
                                        size = 'xl'
                                    ),
                                    BoxComponent(
                                        layout = 'vertical',
                                        margin='lg',
                                        spacing='sm',
                                        contents=body_list
                                    )
                                ]
                            ),
                            footer = BoxComponent(
                                layout='vertical',
                                spacing='sm',
                                contents=[
                                    ButtonComponent(
                                        style='link',
                                        height='sm',
                                        action=URIAction(
                                            label='前往詳情',
                                            uri=data[10]
                                        )
                                    )
                                ],
                                flex= 0 
                            )
                        )
            carousel_list.append(flex_message_card)
                        
        return carousel_list
        
    def show_house_carousel(self,code):
        carousel_list = self.get_carousel_list(code)
        return CarouselContainer(contents=carousel_list)

    def is_show_house(self,code):
        show_list = ['z_t_1','z_t_2','z_t_3','z_t_4','s_t_1','s_t_2','s_t_3','s_t_4']
        return True if code in show_list else False
