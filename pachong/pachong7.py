# -*- codeing = utf-8 -*-
# @Time : 2022/4/22 17:09
from bs4 import BeautifulSoup
import re
import urllib.request,urllib.error
import xlwt
import sqlite3


def main():
    baseurl = "https://movie.douban.com/top250?start="
    datalist = getData(baseurl)
    savepath = ".\\豆瓣电影Top250.xls"

    saveData(savepath)



def getData(baseurl):
    datalist = []
    return datalist

def askURL(url):
    head = {
        "User-Agent": "Mozilla / 5.0(Windows NT 10.0; Win64; x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 80.0.3987.122  Safari / 537.36"
    }
    request = urllib.request.Request(url,headers=head)
    html= ""
    try:

    except urllib.error.URLError as e:

def saveData(savepath):

 pass


if __name__ =="__main__":
    main()