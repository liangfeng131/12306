# coding:utf-8

import datetime
import locale
import os
import re
import telnetlib
import time
import urllib

# from util.logger import Logger


GMT_FORMAT = '%a %b %d %Y %H:%M:%S GMT+0800 (中国标准时间)'
locale.setlocale(locale.LC_CTYPE, 'chinese')


# log = Logger(__name__)


def get_root_path():
    """获取项目根路径"""
    project_name = "12306"
    current_path = os.path.abspath(os.path.dirname(__file__))
    return current_path[:current_path.find(project_name) + len(project_name)]


def timestamp():
    return int(round(time.time() * 1000))


def current_timestamp():
    return int(round(time.time() * 1000))


def current_hour():
    return datetime.datetime.now().hour


def current_date():
    return datetime.datetime.now().strftime('%y-%m-%d')


def current_date_time():
    return datetime.datetime.now().strftime('%y-%m-%d %H:%M:%S')


def check_date(text):
    match = re.compile(r'^\d{4}-\d{1,2}-\d{1,2}$').match(text)
    if match:
        return match.group() is not None
    else:
        return False


def decode_secret_str(code):
    return urllib.parse.unquote(code).replace('\n', '')


def proxy_test(proxy):
    try:
        telnetlib.Telnet(proxy.get('ip'), proxy.get('port'), timeout=1)
        return True
    except BaseException as e:
        return False


def get_gmt_time(text):
    """
    Fri Oct 025 2019 00:00:00 GMT+0800 (中国标准时间)
    Sun Oct 06 2019 00:00:00 GMT+0800 (中国标准时间)
    :param text:
    :return:
    """
    return datetime.datetime.strptime(text, '%Y-%m-%d').strftime(GMT_FORMAT)


if __name__ == '__main__':
    print(proxy_test({'ip': '129.205.160.138', 'port': 54789}))
