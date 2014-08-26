# -*- coding: utf-8
# 该函数打开url并且处理GET和POST

import urllib, urllib2
import sys
reload(sys)
sys.setdefaultencoding('utf8')

# 伪装成浏览器访问
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 \
        Safari/537.36',
}
# 教务系统URL
url_jwxt = 'http://jwxt.sysucs.org/'

# 登录的URL
url_login = url_jwxt + 'sign_in'

# 登录成功后的首页
url_home =  url_jwxt + 'score'

# 获取成绩的URL头
url_score =  url_jwxt + 'api/score'

# 获取年级和编号URL
url_tno = url_jwxt + 'api/tno'

# 获取GPA的URL
url_gba = url_jwxt + 'api/gpa'

# 获取已获取学分URL
url_earned_credit = url_jwxt + 'api/earned_credit'

# 获取总学分的URL
url_required_credit = url_jwxt + 'api/required_credit'

# 设置链接等待时间
time_out = 10#sec

# 获取URL的内容返回字符串
def getData(url):
    # GET数据
        # 先形成一个request
    request = urllib2.Request(url = url, headers = headers)
        # 访问后获得一个response
    response = urllib2.urlopen(request, timeout = time_out)
    results = response.read()
    return results

#  将post_data POST到url，返回response
def postData(url, data):
    # POST数据
        # POST的数据转码
    post_data = urllib.urlencode(data)
        # 先形成一个request
    request = urllib2.Request(
        url = url_login,
        data = post_data,
        headers = headers,
    )
        # 获取response
    response = urllib2.urlopen(request, timeout = time_out)
    return response
