# -*- coding: utf-8 -*-
import scrapy
import re
import json
class MathSpider(scrapy.Spider):
    name = 'math'
    #print('00')
    #start=0
    def start_requests(self):
        #print('0')
        url = 'https://a.jiuyeb.cn/mobile.php/enrollment/getlist'
        for i in range(5):#79
            data={'school_id':'74d304bd-37d0-fcd6-dc73-a831f6bfc757',
                  'size': '12',
                  'page':str(i+1),
                  'keywords':'',
                  'day': '0',
                  'type': '0',
                  'province_id': '0',
                  'login_admin_school_code':'',
                  'login_admin_school_id': '74d304bd-37d0-fcd6-dc73-a831f6bfc757',
                  'login_user_id':'1'
                  }
            heard={'Accept': 'application/json, text/javascript, */*; q=0.01',
                   'auth': 'Baisc MTAyNDY6MTAyNDY=',
                   'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                   'Origin': 'http://wxdonglin.jiuyeb.cn',
                   'Referer': 'http://wxdonglin.jiuyeb.cn/xiaozhao/fairs.html?page=20',
                   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36'}
            yield scrapy.FormRequest(url,method='POST',headers=heard,formdata=data,callback=self.parse,dont_filter=True)
    def parse(self, response):
        urlId=json.loads(response.text)['data']['list']
        for j in range(len(urlId)):
            #url = 'https://a.jiuyeb.cn/mobile.php/enrollment/getlist'
            url0='https://a.jiuyeb.cn/mobile.php/enrollment/detail'
            url2='http://wxdonglin.jiuyeb.cn/xiaozhao/details.html?id='
            data={'id':urlId[j]['id'],
                  'login_admin_school_code':'',
                  'login_admin_school_id': '74d304bd-37d0-fcd6-dc73-a831f6bfc757',
                  'login_user_id':'1'
                  }
            heard={'Accept': 'application/json, text/javascript, */*; q=0.01',
                   'auth': 'Baisc MTAyNDY6MTAyNDY=',
                   'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                   'Origin': 'http://wxdonglin.jiuyeb.cn',
                   'Referer': url2+urlId[j]['id'],
                   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36'
                   }
            val = url2+urlId[j]['id']
            #print(val)
            yield scrapy.FormRequest(url0,formdata=data,headers=heard, callback=lambda response, typeid=val,title=urlId[j]['title']:
                                     self.parse_math(response, typeid,title),dont_filter=True)
            
            #yield scrapy.FormRequest(url0,method='POST',headers=heard,formdata=data,callback=self.parse_math,dont_filter=True)   
        pass
    def parse_math(self, response, typeid,title):
        #print (typeid)
        jobInfo = json.loads(str(response.body.decode('utf-8')))['data']['remarks']
        key='--'
        try:
            match=re.search(r'数学',jobInfo)
            if match:
                key = title #re.search(r'\"title\"\:\".{25}', jobInfo).group()
                val=typeid
                print(key)
                print(val)
                #with open('V:/scrapy/NefuJob/math.txt', 'a', encoding='utf-8') as f:
                    #f.write( key +'\n'+val+ '\n' )
                #yield key +'\n'+val+ '\n'
                yield {key :val}
            #print(key)
            else:
                yield None
            
        except:
            yield None 
           
