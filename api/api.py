# -*- coding: UTF-8 -*-
"""
@Project ：PythonAutoTest 
@File    ：api.py
@IDE     ：PyCharm 
@Author  ：胖妞
@Date    ：2022/5/31 0:23
"""

from config import host
import requests

from tools.get_log import GetLog

log = GetLog.get_logger()


class Api:

    def __init__(self, case):
        # 提取url = host+path
        self.url = host + case.get('path')
        # 请求方法
        self.method = case.get('method')
        # 请求参数类型
        self.param_type = case.get('param_type')
        # 请求信息头
        self.headers = case.get('headers')
        # 请求参数
        self.params = case.get('params')

    # get方法
    def _get(self):
        log.info('正在调用get请求方法')
        return requests.get(url=self.url, params=self.params, headers=self.headers)

    # post方法
    def _post(self):
        log.info('正在调用post请求方法')
        if self.param_type == 'json':
            return requests.post(url=self.url, json=self.params, headers=self.headers)
        elif self.param_type == 'data':
            return requests.post(url=self.url, data=self.params, headers=self.headers)

    # put方法
    def _put(self):
        log.info('正在调用put请求方法')
        return requests.put(url=self.url, json=self.params, headers=self.headers)

    # delete方法
    def _delete(self):
        log.info('正在调用delete请求方法')
        return requests.delete(url=self.url, params=self.params, headers=self.headers)

    # 调用运行方法
    def run_method(self):
        log.info('正在调用运行接口方法')
        if self.method == 'get':
            return self._get()
        elif self.method == 'post':
            return self._post()
        elif self.method == "put":
            return self._put()
        elif self.method == "delete":
            return self._delete()
