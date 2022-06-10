from tkinter import Button
import googletrans
from googletrans import Translator
from linebot.models import FlexSendMessage, BubbleContainer, BoxComponent, TextComponent, ButtonComponent, PostbackAction, BlockStyle, CarouselContainer

class trans():
    lang_list = [['英文','en'],['日文','ja'],['韓文','ko'],['西文','es'],['德文','de'],['法文','fr'],['印尼文','id']]
    lang_data_list=['en','ja','ko','es','de','fr','id']
    language = ''
    def language_footer(self,code):
        lang_list = self.lang_list
        button_list = []
        for button in lang_list:
            button_list.append(
                ButtonComponent(
                action=PostbackAction(
                label = button[0],
                data = button[1]
                ),
                height='md',
                color='#FFB5B5',
                style='primary',
                margin = 'xs'
            ))
        return button_list

    def select_language(self,code):
        button_list = self.language_footer(code)
        flex_message = BubbleContainer(
            size='kilo',
            body=BoxComponent(
                layout = 'vertical',
                contents = [
                    TextComponent(
                        text = '選擇語言',
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
        
        
        return flex_message

    def set_language(self,code):
        setattr(trans,'language',code)
        print(getattr(trans,'language'))
        
    def translate(self,text):
        language = self.language
        print(language)
        translater = googletrans.Translator()
        reply = translater.translate(text,dest=language).text
        print(reply)
        return reply
        


    def is_set_lang(self,code):
        lang_data_list = self.lang_data_list
        print('true')
        return True if code in lang_data_list else False


        
        

    def is_trans(self,code):
        return True if code == 'trans' else False

