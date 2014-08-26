# -*- coding: utf-8 -*-
import sys
import unicodedata
reload(sys)
sys.setdefaultencoding('utf8')

# 判断字符串是否含有汉字，返回长度，如果有长度为其他字符的两倍
def string_len(text):
    text_len = 0
    for char in text:
        if isinstance(char, unicode):
            if unicodedata.east_asian_width(char) != 'Na' and char != u'Ⅰ':
                text_len += 2
            else:
                text_len += 1
    return text_len

# 打印水平分割线，deli为分割符，cols_len为每列的长度
def print_line(deli, cols_len):
    for i in range(0, len(cols_len)):
        sys.stdout.write('+')
        for j in range(0, cols_len[i]):
            sys.stdout.write(deli)
    sys.stdout.write('+\n')

# 给定表格的内容和表头，将其打印成表格
def printTable(contents, headers):
    # 获取每列最大长度，汉字的长度比字母长两倍
    num_cols = len(headers)
    max_len = []
    for i in range(0, num_cols):
        max_len.append(string_len(headers[i]))
    contents_len = []
    for content in contents:
        content_len = []
        for i in range(0, num_cols):
            content_len.append(string_len(content[i]))
            if content_len[i] > max_len[i]:
                max_len[i] = content_len[i]
        contents_len.append(content_len)

    # 打印表头
    print_line('-', max_len)
    for i in range(0, num_cols):
        sys.stdout.write('|')
        sys.stdout.write(headers[i])
        # 打印空格，进行表格格式调整
        for j in range(0, max_len[i] - string_len(headers[i])):
            sys.stdout.write(' ')
    print '|'
    print_line('=', max_len)
    # 打印表格内容
    for i in range(0, len(contents)):
        for j in range(0, num_cols):
            sys.stdout.write('|')
            sys.stdout.write(contents[i][j])
            # 打印空格，进行表格格式调整
            for j in range(0, max_len[j]-contents_len[i][j]):
                sys.stdout.write(' ')
        print '|'
    print_line('-', max_len)
