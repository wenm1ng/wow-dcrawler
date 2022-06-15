# coding: utf-8
import re
import base64
from time import sleep
from App.common.webRequest import WebRequest

'''
 # cn-proxy
 # @author      WenMing    736038880@qq.com
 # @createTime  2021年1月5日 14:01:16
 # @version     0.1.0 版本号
'''


class ppProxyListPlus(object):
    """
    # 抓取结果集
    # @var string
    """
    proxyIpPortList = []

    """
    # 抓取目标连接
    # @var string  
    """
    targetUrls = [
        'https://list.proxylistplus.com/Fresh-HTTP-Proxy-List-1'
    ]

    """
    # 页面
    # @var int  
    """
    page = 2

    """
     # cn-proxy
     # @param self
     # @return string
     # @author     WenMing    736038880@qq.com
     # @createTime 2021年1月5日 14:12:36
    """
    def getProxyResult(self):
        request = WebRequest()
        for url in self.targetUrls:
            r = request.get(url, timeout=10)
            proxies = re.findall(r'<td>(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})</td>[\s\S]*?<td>(\d+)</td>', r.text)
            for proxy in proxies:
                # yield ':'.join(proxy)
                self.proxyIpPortList.append(':'.join(proxy))

    def setPage(self, page=2):
        self.page = page

    def getProxyList(self):
        return self.proxyIpPortList

    def resetClassVar(self):
        self.proxyIpPortList = []

    pass
