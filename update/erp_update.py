#!/usr/bin/python
#coding:utf-8
import os
import re
import urllib
import urllib2
import time

#定时同步更新
while 1:	
	#获取更新版本的网页
	def getHtml(url):
		page = urllib2.urlopen(url)
		html = page.read()
		return html

	#获取最新版本的下载地址
	def file_url(html):
		content = re.search(r'升级日志(.*?)日志结束',html,re.U|re.S)
		html = content.group()
		html = html.split('****************************************')
		fileurl = ''
		#重要！重要！重要！每次生成待更新脚本时必须将当日的日期写入此
		maxver = 20150326	
		for lists in range(len(html)):
			strs = re.findall( r'软件名称：(.*)&#x000A;.*版本号：(.*)&#x000A;.*发布日期：(.*)&#x000A;.*下载地址：(.*)&#x000A;.*更新说明：(.*)&#x000A;',html[lists],re.U|re.S)
	#		print (strs[0][2])
			if int(strs[0][2]) > maxver:
				maxver = int(strs[0][2])
				fileurl = strs[0][3].replace('&amp;','&')
	#			print strs[0][4]
		return fileurl
   
	html = getHtml("https://git.oschina.net/topmy/update/blob/master/fanyierp.lst")
	fileurl = file_url(html)

	#下载文件到临时目录
	def Schedule(a,b,c):
		'''''
		a:已经下载的数据块
		b:数据块的大小
		c:远程文件的大小
	   '''
		per = 100.0 * a * b / c
		if per > 100 :
			per = 100
		print '已下载： %.2f%%' % per
	
	if fileurl != '':
		#print "正在下载：  "+fileurl
		#urllib.urlretrieve(fileurl,'/tmp/test.py',Schedule)
		urllib.urlretrieve(fileurl,'/tmp/list.md')
	

	#移动文件到指定目录并设置好权限加入启动




	#本程序更新需要执行的任务


	time.sleep(1500)



















