import urllib
from urllib.request import urlopen
from urllib.error import HTTPError , URLError
from bs4 import BeautifulSoup

urls = ['http://www.dbmeinv.com']


header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
}

# def get_photo(url):
#     html = requests.url
#
#     print(html.text)
#
#     # pat = '[p|/]>\n*<img src="(.*?)"'
#     #
#     # links = re.findall(pat, html.text, re.M)
#     #
#     # print(links)

def getHtml(url):
    page1 = 'http://www.pythonscraping.com/pages/page1.html'
    html = urlopen(url)
    bsObj = BeautifulSoup(html.read())

    try:
        html = urlopen(url)
    except HTTPError as e:
        print(e)
    else:
        # 继续处理
        print('继续处理')

    print(bsObj.href)


def getTitle(url):
    try:
        html = urlopen(url)
    except (HTTPError , URLError) as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read())
        title = bsObj.body.h1
    except AttributeError as e:
        return None
    return title



def getSubInfo(url):

    request = urllib.request.Request(url)
    request.add_header('User-Agent','Mozilla/5.0')#
    html = urlopen(request)
    bsObj = BeautifulSoup(html.read())

    # print(bsObj)

    # nsmaList =  bsObj.findAll("dt",{"class":"public-title"})
    # for name in nsmaList:
    #     print(name.get_text())


    imgList = bsObj.findAll("img",{"class":"height_min"})
    for name in imgList:
        # print(name)
        # print(name.get('title'))
        # print(name.get('src'))
        print(name.attrs['src']) #获取标签对象全部属性


# title = getTitle('http://www.pythonscraping.com/pages/page1.htm')
# # title = getTitle('http://cuiqingcai.com/1319.html')
# if title == None:
#     print("Title not found")
# else:
#     print(title)


for url in urls:
    getSubInfo(url)
