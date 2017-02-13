import requests
import re

urls = ['http://jandan.net/ooxx/page-{}'.format(str(i)) for i in range(0,200)]

path = '/Desktop/煎蛋网/'

url_list = []

header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
}

def get_photo(url):
    html = requests.get(url)

    # print(html.text)

    pat = '[p|/]>\n*<img src="(.*?)"'

    links = re.findall(pat, html.text, re.M)

    for str in links:
        b = str.find("//ww")
        if(b == 0):
            print(str)
            sp =  str.replace('//','http://')
            url_list.append(sp)


for url in urls:
    get_photo(url)

for url in url_list:
    print(url)
    print("\n")