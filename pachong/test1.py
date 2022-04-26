# -*- codeing = utf-8 -*-
# @Time : 2022/4/23 11:17
import requests
url = "https://y.qq.com/"
headers = {
     "cookie": "fqm_pvqid=47004ebb-881e-4960-b3be-c1b788a29ef5; pgv_pvid=5045419744; fqm_sessionid=ed4e44cf-b197-45f7-8b5b-07c1971e42d9; pgv_info=ssid=s9178083252; ts_refer=www.baidu.com/link; ts_uid=227058575; ts_last=y.qq.com/",
     "origin": "https://y.qq.com",
     "referer": "https://y.qq.com/",
     "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36"
}
response = requests.get(url,headers=headers)

print(response)
#for i in response:
    #if
