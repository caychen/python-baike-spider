#! /usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Created on 2016年4月12日

@author: Cay
'''
from bs4 import BeautifulSoup
import re
from urllib.parse import urljoin


class HtmlParser(object):
    
    
    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        links = soup.find_all('a', href=re.compile(r'/view/\d+\.htm'))
        for link in links:
            new_url = link['href']
            new_full_url = urljoin(page_url, new_url)
            new_urls.add(new_full_url)
        return new_urls
    
    
    def _get_new_data(self, page_url, soup):
        res_data = {}
        
        # url
        res_data['url'] = page_url
        
        #   <dd class="lemmaWgt-lemmaTitle-title">
        #   <h1>Python</h1>
        #   </dd>
        title_node = soup.find('dd', class_='lemmaWgt-lemmaTitle-title').find('h1')
        res_data['title'] = title_node.get_text()
        
        # <div class="lemma-summary" label-module="lemmaSummary">
        summary_node = soup.find('div', class_='lemma-summary')
        res_data['summary'] = summary_node.get_text()
        
        return res_data
    
    
    def parse(self, page_url, html_context):
        if page_url is None or html_context is None:
            return None
        
        soup = BeautifulSoup(html_context, 'html.parser', from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data
    