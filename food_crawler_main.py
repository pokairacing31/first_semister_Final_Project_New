from urllib import response

import requests,re,json
from bs4 import BeautifulSoup


url='https://ifoodie.tw/explore/台北市/士林區/list?sortby=rating'
resp=requests.get(url)
resp.encoding='utf-8'
print('網頁下載中...')
resp.raise_for_status()
print('網頁下載完成')
soup= BeautifulSoup(resp.text, 'html.parser')

# article=soup.select('script[type="application/json"]')
article = soup.select('script[type="application/json"]')[0].contents[0]
results = json.loads(article)
print(results.keys())
final1=results['props']
# print(final1.keys())
final2=final1['initialState']
# print(final2.keys())
final3=final2['search']
# print(final3.keys())
final4=final3['explore']
# print(final4.keys())
final5=final4['data']
#print(final5[0])
'''
for i in range(10):
    dic=final5[i]
    res_name=dic['name']
    print(res_name)
    res_phone=dic['phone']
    print(res_phone)
    res_address=dic['address']
    print(res_address)
    res_rating=dic['rating']
    print(res_rating)
    res_cover=dic['coverUrl']
    print(res_cover)
    print()
    '''