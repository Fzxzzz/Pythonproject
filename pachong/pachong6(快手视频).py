import requests
import os
url = 'https://www.kuaishou.com/graphql'
os_path = os.getcwd() + '/视频/'
if not os.path.exists(os_path):
    os.mkdir(os_path)
headers = {
    'content-type': 'application/json',
    'Cookie': 'did=web_0e72852770472c4525104bd3bdbb8a40; didv=1649766476768; kpf=PC_WEB; kpn=KUAISHOU_VISION; clientid=3',
    'Host': 'www.kuaishou.com',
    'Origin': 'https://www.kuaishou.com',
    'Referer': 'https://www.kuaishou.com/brilliant',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36'
}
data = {"operationName":"brilliantTypeDataQuery","variables":{"hotChannelId":"00","page":"brilliant","pcursor":"1"},"query":"fragment feedContent on Feed {\n  type\n  author {\n    id\n    name\n    headerUrl\n    following\n    headerUrls {\n      url\n      __typename\n    }\n    __typename\n  }\n  photo {\n    id\n    duration\n    caption\n    likeCount\n    realLikeCount\n    coverUrl\n    photoUrl\n    coverUrls {\n      url\n      __typename\n    }\n    timestamp\n    expTag\n    animatedCoverUrl\n    distance\n    videoRatio\n    liked\n    stereoType\n    __typename\n  }\n  canAddComment\n  llsid\n  status\n  currentPcursor\n  __typename\n}\n\nfragment photoResult on PhotoResult {\n  result\n  llsid\n  expTag\n  serverExpTag\n  pcursor\n  feeds {\n    ...feedContent\n    __typename\n  }\n  webPageArea\n  __typename\n}\n\nquery brilliantTypeDataQuery($pcursor: String, $hotChannelId: String, $page: String, $webPageArea: String) {\n  brilliantTypeData(pcursor: $pcursor, hotChannelId: $hotChannelId, page: $page, webPageArea: $webPageArea) {\n    ...photoResult\n    __typename\n  }\n}\n"}
for page in range(2):
    response = requests.post(url,headers=headers,json=data)
    json_data = response.json()
    data_list = json_data['data']['brilliantTypeData']['feeds']
    for data_dict in data_list:
        tittle = data_dict['photo']['caption']
        name = tittle.replace('\\','').replace('\n','').replace('@','')
        mp4_url = data_dict['photo']['photoUrl']
        base = requests.get(mp4_url).content
        with open(os_path + name + '.mp4', 'wb') as f:
            f.write(base)
        print(f"{name}===========下载完毕！！！")