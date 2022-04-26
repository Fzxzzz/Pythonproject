import requests
#Request URL: https://image.baidu.com/search/albumsdata?pn=30&rn=30&tn=albumsdetail&word=%E6%B8%90%E5%8F%98%E9%A3%8E%E6%A0%BC%E6%8F%92%E7%94%BB&album_tab=%E8%AE%BE%E8%AE%A1%E7%B4%A0%E6%9D%90&album_id=409&ic=0&curPageNum=1
url = 'https://image.baidu.com/search/albumsdata'
params = {
      'pn': '30',
      'rn': '30',
      'tn': 'albumsdetail',
      'word': '渐变风格插画',
      'album_tab': '设计素材',
      'album_id': '409',
      'ic': '0',
      'curPageNum': '1'
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36'
}
respons = requests.get(url,headers=headers,params=params).json()
data_list = respons['albumdata']['linkData']
num = 1
for dict_data in data_list:
    img_url = dict_data['thumbnailUrl']
    data = requests.get(img_url).content
    with open(r'E:\搜狗高速下载\快速保存图片\{}.jpg'.format(num),'wb') as f:
        f.write(data)
    num += 1
