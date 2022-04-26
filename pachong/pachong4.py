import requests
from urllib.parse import quote
user_input = input("请输入要爬取的贴吧名称")
user_page = input("请输入要爬取的页数")
head = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36'
}
for i in range(int(user_page)):

        url = f'https://tieba.baidu.com/f?kw={quote(user_input)}&ie=utf-8&pn={i*50}'
        response = requests.get(url,headers=head).content.decode()
        with open(f"{user_input}_{i+1}.html",'w',encoding='utf8')as f:
            f.write(response)
        print(f'{user_input}=======第{i+1}页======logging')