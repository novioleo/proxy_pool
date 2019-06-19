# -*- coding: utf-8 -*-
# !/usr/bin/env python
"""
-------------------------------------------------
   File Name：     GetPrivateProxy.py
   Description :  获取私有代理
   Author :       Novio
   date：         2019年06月19日
-------------------------------------------------
   Change Activity:
-------------------------------------------------
"""
import re
import sys
import requests

sys.path.append('..')

from Util.WebRequest import WebRequest
from Util.utilFunction import getHtmlTree

# for debug to disable insecureWarning
requests.packages.urllib3.disable_warnings()

"""

"""


class GetPrivateProxy(object):
    """
    proxy getter
    """

    @staticmethod
    def func_1(*args, **kwargs):
        """
        自定义私有代理ip池
        """
        ip_port_list = [
            ('0.0.0.0', 1080),
        ]
        for m_ip_port in ip_port_list:
            yield '%s:%s' % m_ip_port


if __name__ == '__main__':
    from ProxyGetter.CheckProxy import CheckProxy

    functions = [
        GetPrivateProxy.func_1
    ]
    for m_func in functions:
        CheckProxy.checkGetProxyFunc(m_func)

    # or
    # CheckProxy.checkAllGetProxyFunc(GetPrivateProxy)
