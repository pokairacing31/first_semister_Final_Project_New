from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
import csv
import requests
from time import sleep
from selenium.webdriver.common.by import By
import pandas as pd


def get_data(url):
    title="NULL"
    price="NULL"
    addr="NULL"
    style="NULL"
    size="NULL"
    floor="NULL"
    Class="NULL"
    lordName="NULL"
    lordPhone="NULL"
    pic="NULL"

    browser = webdriver.Chrome()
    browser.get(url)
    time.sleep(1)
    title_elem = browser.find_elements(by=By.XPATH,value="//section//div[@class='house-title']/h1")
    for t_elem in title_elem:
        title = t_elem.text
    price_elem = browser.find_elements(by=By.XPATH,value="//section//div//span[@class='price']/b")
    for p_elem in price_elem:
        price = p_elem.text
    addr_elem = browser.find_elements(by=By.XPATH,value="//section//div//span[@class='load-map']")
    for a_elem in addr_elem:
        addr = a_elem.text
    style_elem = browser.find_elements(by=By.XPATH,value="//section//div[@class='house-pattern']/span[1]")
    for pt_elem in style_elem:
        style = pt_elem.text    
    size_elem = browser.find_elements(by=By.XPATH,value="//section//div[@class='house-pattern']/span[3]")
    for s_elem in size_elem:
        size = s_elem.text  
    floor_elem = browser.find_elements(by=By.XPATH,value="//section//div[@class='house-pattern']/span[5]")
    for f_elem in floor_elem:
        floor = f_elem.text
    class_elem = browser.find_elements(by=By.XPATH,value="//section//div[@class='house-pattern']/span[7]")
    for c_elem in class_elem:
        Class = c_elem.text  
    ldname_elem = browser.find_elements(by=By.XPATH,value="//div//section//div//p[@class='name']")
    for ld_elem in ldname_elem:
        lordName = ld_elem.text
    ldphone_elem = browser.find_elements(by=By.XPATH,value="//div//div//div//div//span[@class='tel-txt']")
    for phone_elem in ldphone_elem:
        lordPhone = phone_elem.text
    pic_elem = browser.find_elements(by=By.XPATH,value='//*[@id="app"]/div[2]/section/section[1]/div[1]/img')
    for pic in pic_elem:
        pic = pic.get_attribute("src")

    return title,price,addr,style,size,floor,Class,lordName,lordPhone,pic

        




def main(outputfile):
    browser = webdriver.Chrome()
    browser.get("https://rent.591.com.tw/?region=1&section=8")
    with open(outputfile,'w', newline='',encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["標題","租金","地址","格局","大小","樓層","型態","房東","房東電話","圖片","url"])
        pages = 2
        for i in range(pages):
            bs = BeautifulSoup(browser.page_source, 'html.parser')
            get_url_list = []
            get_url = browser.find_elements(by=By.XPATH,value="//section[@class='vue-list-rent-item']/a")
            for elem in get_url:
                get_url_list.append(elem.get_attribute('href'))
            time.sleep(5)
            for url in get_url_list:
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
    
if __name__ == '__main__':
    # -------- configurable parameter -------- #
    output_file_name = 'tpe_rent_output.csv'
    # ---------------------------------------- #
    main(output_file_name)
    print('\nfinish!')