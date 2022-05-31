# -*- coding: UTF-8 -*-
"""
@Project ：PythonAutoTest 
@File    ：common_assert.py
@IDE     ：PyCharm 
@Author  ：胖妞
@Date    ：2022/5/31 0:20
"""

from tools.get_log import GetLog

log = GetLog.get_logger()


def common_assert(response, case):
    log.info("正在调用断言公共方法")
    # 获取响应数据
    result = response.json()
    # 获取预期数据
    expect = case.get("expect")
    # 断言 响应状态吗
    # assert response.status_code == expect.get("code"), "错误！响应 code：{} 预期code：{}".format(response.status_code,
    #                                                                                     expect.get("code"))
    # 断言 success
    assert result.get("success") == expect.get("success"), "错误！响应 success：{} 预期 success：{}".format(
        result.get("success"), expect.get("success"))
    # 断言 code
    assert result.get("code") == expect.get("code"), "错误！响应 code：{} 预期 code：{}".format(result.get("code"),
                                                                                       expect.get(
                                                                                           "code"))
    # 断言 message
    assert result.get("message") == expect.get("message"), "错误！响应 message：{} 预期 message：{}".format(
        result.get("message"), expect.get("message"))
