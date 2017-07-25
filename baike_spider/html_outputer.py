#! /usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Created on 2016年4月12日

@author: Cay
'''


class HtmlOutputer(object):
    def __init__(self):
        self.datas = []
        
    
    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)
        pass

    
    def output_html(self):
        with open('output.html','w') as f:
            f.write('<html>')
            f.write('<head><meta http-equiv="Content-Type" content="text/html;charset=UTF-8" /></head>')
            f.write('<body>')
            f.write('<table border="1" cellspacing="0" cellpadding="0">')
            
            for data in self.datas:
                f.write('<tr>')
                f.write('<td>%s</td>' % data['url'])
                f.write('<td>%s</td>' % data['title'].encode('utf-8'))
                f.write('<td>%s</td>' % data['summary'].encode('utf-8'))
                
                f.write('</tr>')
            
            f.write('</table>')
            f.write('</body>')
            f.write('</html>')
        pass
