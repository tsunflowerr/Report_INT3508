"""Inspect official university image links; no image transformation."""
from html.parser import HTMLParser
import urllib.request,urllib.parse
class Images(HTMLParser):
    def handle_starttag(self,tag,attrs):
        values=dict(attrs)
        if tag=='img':
            print(values.get('src',''), values.get('alt',''), values.get('srcset',''))
for url in ['https://uet.vnu.edu.vn/', 'https://www.fit.uet.vnu.edu.vn/logo-cua-doi-tac/']:
    try:
        data=urllib.request.urlopen(url,timeout=15).read().decode('utf-8')
        print('SOURCE',url)
        Images().feed(data)
    except Exception as exc:print(type(exc).__name__,str(exc))
