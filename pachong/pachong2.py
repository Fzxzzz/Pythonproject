import requests
from lxml import html
url='https://movie.douban.com/' #需要爬数据的网址
head ={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36'
}
page=requests.Session().get(url,headers=head)
tree=html.fromstring(page.text)
result=tree.xpath('//li[@class="tittle"]//a/text()')
print(result)
