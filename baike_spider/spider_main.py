#! /usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Created on 2016年4月12日

@author: Cay
'''
from baike_spider import url_manager, html_downloader, html_parser,\
    html_outputer


class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()
    
    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print('craw %d : %s' % (count, new_url))
                html_context = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_context)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)
                
                if count == 10:
                    break
                count += 1
                
            except:
                print('craw failed')
    
        self.outputer.output_html()


if __name__ == '__main__':
    root_url = 'http://baike.baidu.com/link?url=Lc3Pc5b-F48CTThhaJdO1LX_Xb9pPMP6Yq1_hEwnNUNeO0JuZTDYXOCCXuikkGr77oqXJFTDV1ji-6EjjbCRGK'
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)