# -*- coding: utf-8 -*-
# jwxt的实现部分
import urllib, urllib2
import json
import re
import cookielib
from tools.printTable import printTable
from tools.openUrl import *

import sys
reload(sys)
sys.setdefaultencoding('utf8')

# 定义输出表头
query_headers = [u'课程名称',u'学分', u'最终成绩', u'绩点', u'教学班排名', ]

# 定义学分总览表头
credit_headers = [u'类型', u'绩点', u'学分', ]

# 登录系统
def login(username, password):
    # 处理cookie
    cookie_support = urllib2.HTTPCookieProcessor(cookielib.CookieJar())
    opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)
    urllib2.install_opener(opener)

    # POST数据到登录URL
    response = postData(url_login, {'username': username, 'password': password, })

    # 通过url有没有被重定向来判断登录是否成功
    return response.url == url_home

# 成绩查询
def queryResults(year = '', term = '', pylb = ''):
    # 判断查询总成绩还是学期成绩, 产生GET的URL
    if year == '' and term == '' and pylb == '':
        url_results = url_score
    else:
        url_results = url_score + '?' + urllib.urlencode({'year': year, 'term': term, 'pylb' : '0'+ pylb, })
    # GET数据
    results = getData(url_results)
    # 将字符串转换成字典列表
    results = re.findall(r'\[.*\]', results)[0]
    results = json.loads(results)
    # 打印结果
    contents = []
    for result in results:
        content = [result['kcmc'], result['xf'], result['zzcj'], result['jd'], result['jxbpm'],]
        content[4] = re.sub(r'V', '/', result['jxbpm'])
        contents.append(content)
    printTable(contents, query_headers)

# 学分总览
def creditOverview():
    # 获取已获学分情况
    earned_credit = getData(url_earned_credit)
    # 将字符串转化为字典列表
    earned_credit = re.findall(r'\[.*\]', earned_credit)[0]
    earned_credit = json.loads(earned_credit)

    # 先获取grade和tno两个参数
    results = getData(url_tno)
    tup = re.findall(r'\d+,\d+,\d+', results)[0].split(',')
    grade = tup[1]
    tno = tup[2]

    # 获取总学分情况
    url_request = url_required_credit + '?' + urllib.urlencode({'grade': grade, 'tno': tno, })
    required_credit = getData(url_request)
    # 将字符串转化为字典列表
    required_credit = re.findall(r'\[.*\]', required_credit)[0]
    required_credit = json.loads(required_credit)

    # 获取GBA
    gba = getData(url_gba)
    # 将字符串转化成为
    gba = re.findall(r'\[.*\]', gba)[0]
    gba = json.loads(gba)

    # 打印结果
    contents = [[u'公必', ], [u'专必', ], [u'专选', ], [u'公选', ]]
    for i in range(0, 4):
        contents[i].append(gba[i]['twoColumn'])
        contents[i].append(earned_credit[i]['twoColumn'] + '/' + required_credit[i]['twoColumn'])
    printTable(contents, credit_headers)
