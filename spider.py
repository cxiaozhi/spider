# 读取网页内容
from encodings.utf_8 import encode
from socket import timeout
import urllib3 as lib3
import re

url_http = lib3.PoolManager()

my_html = url_http.request('get','https://shiwens.com/bookv_13498.html',timeout=3.0)
decode_my_html = my_html.data.decode('utf-8')
reg_text = re.findall('<p>[\D]+</p>',decode_my_html)
text_str = reg_text[0]
text_list = text_str.split('</p>')
f =  open('three.txt','w+')

for item in text_list:
  row_text = item.replace('<p>','')
  f.writelines(row_text)

f.close()