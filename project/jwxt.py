# -*- coding: utf-8 -*-
# jwxt的UI部分
import getpass
import urllib2
from kernel.jwxtApp import *
from kernel.tools.printTable import printTable
import socket
is_login = False
is_quit = False

if __name__ == '__main__':
    print '欢迎使用jwxt,请先登录'
    while not is_quit:
        while not is_login:
            try:
                username = raw_input('请输入学号： ')
                password = getpass.getpass('请输入密码： ')
            except EOFError:
                print '输入终止！'
                is_quit = True
                break
            except KeyboardInterrupt:
                print '输入终止！'
                is_quit = True
                break
            else:
                try:
                    is_login = login(username, password)
                except urllib2.URLError:
                    print '链接失败！'
                except socket.timeout:
                    print '链接超时！'
                else:
                    if is_login:
                        print '登录成功！请选择操作，输入回车结束： '
                        printTable([[u'1', u'查询特定学期成绩',], [u'2', u'查看所有成绩', ], \
                            [u'3', u'查看学分总览',], [u'4', u'退出',]],[u'选择', u'操作', ])
                    else:
                        print '登录失败！'

        if is_quit:
            break

        try:
            oper = raw_input('您选择的操作是： ')
        except EOFError:
            oper = '4'
            print '输入终止！'
        except KeyboardInterrupt:
            oper = '4'
            print '输入终止！'
        if oper == '1':
            try:
                year = raw_input('请输入学年(yyyy-yyyy)： ')
                term = raw_input('请输入学期(1.第一学期, 2.第二学期, 3.第三学期)： ')
                pylb = raw_input('请选择类型(1.主修, 2.辅修, 3.双学位, 4.双专业)： ')
            except EOFError:
                is_quit = True
                print '输入终止！'
            except KeyboardInterrupt:
                is_quit = True
                print '输入终止！'
            else:
                if pylb == '':
                    pylb = '1'
                queryResults(year, term, pylb)
        elif oper == '2':
            queryResults()
        elif oper == '3':
            creditOverview()
        elif oper == '4':
            is_quit = True
        else:
            print '输入有误，请重新输入！'

    print '登出成功！'
