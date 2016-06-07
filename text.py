# /usr/bin/env python3
# -*- coding:utf-8 -*-

import urllib.request
import urllib.error
import re


class qiubai:

    def __init__(self):
        print('欢迎进入糗事百科爬取界面')
        self.baseUrl = 'http://www.qiushibaike.com/8hr/page/'
        self.pageNum = 1
        self.user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36'
        self.headers = {"User-Agent": self.user_agent}
        self.enable = True
        self.main()

    def getPage(self):
        try:
            url = self.baseUrl + str(self.pageNum)
            request = urllib.request.Request(url, headers=self.headers)
            response = urllib.request.urlopen(request)
            pageCode = response.read().decode('utf-8')
            return pageCode
        except urllib.error.URLError as e:
            if hasattr(e, 'code'):
                print(e.code)
            if hasattr(e, 'reason'):
                print(e.reason)

    def getConent(self, pageCode):
        pattern = re.compile(
            '<h2>(.*?)</h2>.*?<div class="content">(.*?)</div>', re.S)
        items = re.findall(pattern, pageCode)
        for item in items:
            txt = re.sub('<br.*?>', '\n', item[1])
            print('发布者:' + item[0] + '\n内容:' + txt)

    def loadPage(self):
        while self.enable:
            new_pageCode = self.getPage()
            self.getConent(new_pageCode)
            quit = input('是否加载下一页，退出Q:')
            if quit == 'Q':
                self.enable = False
                print('结束')
                return
            else:
                self.pageNum += 1

    def main(self):
        self.loadPage()

qiubai()
