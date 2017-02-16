#coding=utf-8
import urllib
from urllib.request import urlopen
import re
import time
import os

def getHtml(url):
    page = urlopen(url)  #urllib.urlopen()方法用于打开一个URL地址
    html = page.read() #read()方法用于读取URL上的数据
    return html


def downloadImg(html):
    reg = r'src="(.+?\.jpg)" pic_ext'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    # 定义文件夹的名字
    t = time.localtime(time.time())
    foldername = str(t.__getattribute__("tm_year")) + "-" + str(t.__getattribute__("tm_mon")) + "-" + str(
        t.__getattribute__("tm_mday"))
    # / Users / runlin / Desktop /MMM
    picpath = 'Users\\runlin\\Desktop\\MMM\\%s' % (foldername)  # 下载到的本地目录

    if not os.path.exists(picpath):  # 路径不存在时创建一个
        os.makedirs(picpath)
    x = 0
    for imgurl in imglist:
        target = picpath + '\\%s.jpg' % x
        image = urllib.request.urlretrieve(imgurl, target, schedule)
        x += 1
    return image;

def schedule(a,b,c):
	'''''
	a:已经下载的数据块
	b:数据块的大小
	c:远程文件的大小
   '''
	per = 100.0 * a * b / c
	if per > 100 :
		per = 100
	print( '%.2f%%' % per)

html = getHtml("http://tieba.baidu.com/p/2242414435#!/l/p1")
# html = getHtml("http://tieba.baidu.com/p/2242414435")
print(html)
# downloadImg(html.decode('utf-8'))
print("download yes")