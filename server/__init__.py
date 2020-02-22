
import sqlite3
import requests
from bs4 import BeautifulSoup

import model.Sql as sql


class DataGet():
    def __init__(self):
        pass
    def getBlogsData(self):
        '''Get the blogs.html data'''
        data = []
        data.extend([
            {'links': '/showi',
             'content': 'Showi小冰:一切都有迹可循(狗头护体)'},
            {'links': 'https://mp.weixin.qq.com/s/L0dlAT6NK5tHeSDtI-7DOg', 'content': '小姬姬:减3000还是减5000，在线砍价攻略，带你上戴尔砍价买电脑'},
            {'links': 'https://mp.weixin.qq.com/s/m36OZ3TDVLJaNigY1xGAsw', 'content': '小姬姬:这是个装机必备的神器，不信？那你来看看'},
            {'links': 'https://mp.weixin.qq.com/s/bF_8lvOA9seUDH_rJ5QXsQ', 'content': '小姬姬:快来白嫖免费的云电脑'},
            {'links': 'https://mp.weixin.qq.com/s/L0KG0VVJ56eokglKqrby0w', 'content': '小姬姬:小机机又来用爱发电了'},
            {'links': 'https://mp.weixin.qq.com/s/wm9OqT7G3xcvhIwLuSShvg', 'content': '小姬姬:又一款超级音乐神器，请收下'},
            {'links': 'https://mp.weixin.qq.com/s/dMSpymfz2GgIY8iOeAmqkw', 'content': '小姬姬:知网研学平台免费使用攻略'},{'links': 'https://mp.weixin.qq.com/s/L0dlAT6NK5tHeSDtI-7DOg', 'content': '小姬姬:减3000还是减5000，在线砍价攻略，带你上戴尔砍价买电脑'},
            {'links': 'https://mp.weixin.qq.com/s/m36OZ3TDVLJaNigY1xGAsw', 'content': '小姬姬:这是个装机必备的神器，不信？那你来看看'},
            {'links': 'https://mp.weixin.qq.com/s/bF_8lvOA9seUDH_rJ5QXsQ', 'content': '小姬姬:快来白嫖免费的云电脑'},
            {'links': 'https://mp.weixin.qq.com/s/L0KG0VVJ56eokglKqrby0w', 'content': '小姬姬:小机机又来用爱发电了'},
            {'links': 'https://mp.weixin.qq.com/s/wm9OqT7G3xcvhIwLuSShvg', 'content': '小姬姬:又一款超级音乐神器，请收下'},
            {'links': 'https://mp.weixin.qq.com/s/dMSpymfz2GgIY8iOeAmqkw', 'content': '小姬姬:知网研学平台免费使用攻略'}
        ])
        return str(data)


    def getAppdata(self):
        '''
        get app data
        :return: a json data,can be parse to a list,caontain obj consisting of img,href,name
        '''
        url = 'https://m.wandoujia.com/top/app'
        html = requests.get(url).text#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1.获取网页所有的html

        soup = BeautifulSoup(html,"html.parser")#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!2.使用bs4将html解析
        i = 0
        imgs = []
        href = []
        names = []
        for tag in soup.find_all('div', class_='icon-wrap'):#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!3.找到其中的类名为icon-wrap的div的内容
            if i > 30:
                break
            href.append(tag.find('a').get_attribute_list('href'))#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!4.获取网页中的标签为a的属性:href
            imgs.append(tag.find('img').get_attribute_list('src'))#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            names.append(tag.find('img').get_attribute_list('alt'))#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

            i = i+1
        data = []
        for img,hr,name in zip(imgs,href,names):
            obj = {}
            obj['img'] = img
            obj['href'] = hr
            if len(name[0]) > 5:
                nameShort = name[0][:4]+'...'
                obj['name'] = nameShort
                # print('a')
            else:
                obj['name'] = name
            data.append(obj)
        return str(data)

    def getNewsData(self):
        '''

        :return:
        '''

        url = 'http://tech.123.com.cn/ai/'
        html = requests.get(url).text

        soup = BeautifulSoup(html, "html.parser")
        i = 0
        html = []
        for tag in soup.find_all('li', class_='hasimg'):
            if i > 5:
                break
            html.append(i)

            i = i + 1
        return str(html)

    def getData(self, data_name):
        '''get data by the request'''
        if(data_name == 'homeBlogData'):
            # print('#server.init.getData:','yo')
            return self.getBlogsData()
        elif(data_name=='app'):
            return self.getAppdata()
        elif(data_name=='news'):
            return self.getNewsData()

#
# a = DataGet()
# obj = eval(a.getData('news'))
# print(obj)



