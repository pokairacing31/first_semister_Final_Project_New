from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
import csv
from time import sleep
from selenium.webdriver.common.by import By
import pandas as pd
import threading



def cleaner(url_list):
    for obj in url_list:
        df = pd.read_csv(obj[0],sep=',')
        new_df = df.dropna()
        new_df.to_csv(obj[0],index=None,index_label=None)

def get_data(url):
    title_e="NULL"
    price_e="NULL"
    addr_e="NULL"
    style_e="NULL"
    size_e="NULL"
    floor_e="NULL"
    Class_e="NULL"
    lordName_e="NULL"
    lordPhone_e="NULL"
    pic_e="NULL"

    browser = webdriver.Chrome("C:\python\Final_Project\chromedriver.exe")
    browser.get(url)
    time.sleep(1)
    title_elem = browser.find_elements(by=By.XPATH,value="//section//div[@class='house-title']/h1")
    for t_elem in title_elem:
        title_e = t_elem.text
    price_elem = browser.find_elements(by=By.XPATH,value="//section//div//span[@class='price']/b")
    for p_elem in price_elem:
        price_e = p_elem.text
    addr_elem = browser.find_elements(by=By.XPATH,value="//section//div//span[@class='load-map']")
    for a_elem in addr_elem:
        addr_e = a_elem.text
    style_elem = browser.find_elements(by=By.XPATH,value="//section//div[@class='house-pattern']/span[1]")
    for pt_elem in style_elem:
        style_e = pt_elem.text    
    size_elem = browser.find_elements(by=By.XPATH,value="//section//div[@class='house-pattern']/span[3]")
    for s_elem in size_elem:
        size_e = s_elem.text  
    floor_elem = browser.find_elements(by=By.XPATH,value="//section//div[@class='house-pattern']/span[5]")
    for f_elem in floor_elem:
        floor_e = f_elem.text
    class_elem = browser.find_elements(by=By.XPATH,value="//section//div[@class='house-pattern']/span[7]")
    for c_elem in class_elem:
        Class_e = c_elem.text  
    ldname_elem = browser.find_elements(by=By.XPATH,value="//div//section//div//p[@class='name']")
    for ld_elem in ldname_elem:
        lordName_e = ld_elem.text
    ldphone_elem = browser.find_elements(by=By.XPATH,value="//div//div//div//div//span[@class='tel-txt']")
    for phone_elem in ldphone_elem:
        lordPhone_e = phone_elem.text
    pic_elem = browser.find_elements(by=By.XPATH,value='//*[@id="app"]/div[2]/section/section[1]/div[1]/img')
    for p_elem in pic_elem:
        pic_e = p_elem.get_attribute("src")


    return title_e,price_e,addr_e,style_e,size_e,floor_e,Class_e,lordName_e,lordPhone_e,pic_e

        




def main(outputfile,main_url):
    browser = webdriver.Chrome("C:\python\Final_Project\chromedriver.exe")
    browser.get(main_url)
    with open(outputfile,'w', newline='',encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["標題","租金","地址","格局","大小","樓層","型態","房東","電話","圖片url","url"])
        pages = 2
        for i in range(pages):
            bs = BeautifulSoup(browser.page_source, 'html.parser')
            get_url_list = []
            get_url = browser.find_elements(by=By.XPATH,value="//section[@class='vue-list-rent-item']/a")
            for elem in get_url:
                get_url_list.append(elem.get_attribute('href'))
            time.sleep(5)
            for url in get_url_list[0:20]:
                title,price,addr,style,size,floor,Class,lordName,lordPhone,pic = get_data(url)
                
                writer.writerow([title,price,addr,style,size,floor,Class,lordName,lordPhone,pic,url])

            print(i/pages*100, '%',end='\r')
            if bs.find('a',{'class':'last'}):
                pass
            else:
                #撈取完資料後點選下一頁，並等待 3 秒載入新頁面
                browser.find_element_by_class_name('pageNext').send_keys(Keys.ESCAPE)
                browser.find_element_by_class_name('pageNext').click()
                time.sleep(3)
    
def run():
    # -------- configurable parameter -------- #
    output_file_list=[['shilin_indep_suite_output.csv',"https://rent.591.com.tw/?section=8&searchtype=1&kind=2"],
                        ['shilin_sublet_output.csv',"https://rent.591.com.tw/?section=8&searchtype=1&kind=3"],
                        ['shilin_soloroom_output.csv',"https://rent.591.com.tw/?section=8&searchtype=1&kind=4"],
                        ['shilin_flat_output.csv',"https://rent.591.com.tw/?section=8&searchtype=1&kind=1"],
                        ['zhongzheng_flat_output.csv',"https://rent.591.com.tw/?section=1&searchtype=1&kind=1"],
                        ['zhongzheng_indep_suite_output.csv',"https://rent.591.com.tw/?section=1&searchtype=1&kind=2"],
                        ['zhongzheng_sublet_output.csv',"https://rent.591.com.tw/?section=1&searchtype=1&kind=3"],
                        ['zhongzheng_soloroom_output.csv',"https://rent.591.com.tw/?section=1&searchtype=1&kind=4"]]
    
    # ---------------------------------------- #
    for output in output_file_list:
        output_file_name= output[0]
        url = output[1]
        main(output_file_name,url)

    cleaner(output_file_list)
    print('\nfinish!')

while True:
    timer = threading.Timer(0,run)
    timer.start()
    time.sleep(3600)