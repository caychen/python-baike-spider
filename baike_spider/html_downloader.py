#! /usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Created on 2016年4月12日

@author: Cay
'''
from urllib import request


class HtmlDownloader(object):
    
    
    def download(self, url):
        if url is None:
            return None
        response = request.urlopen(url)
        
        if response.getcode() != 200:
            return None
        
        return response.read()
