# -*- coding: UTF-8 -*-
"""
@Project ：PythonAutoTest 
@File    ：test01.py
@IDE     ：PyCharm 
@Author  ：胖妞
@Date    ：2022/5/31 0:41
"""
import pytest

from api.api import Api
from tools.common_assert import common_assert
from tools.file_tool import FileTool
from tools.get_log import GetLog

log = GetLog.get_logger()


class Test01:
    # 实例化获取工具类对象
    tool = FileTool('Case01.xlsx')
    # 读取Excel，写入到json文件中
    tool.read_excel()

    @pytest.mark.parametrize('case', tool.read_json())
    def test01(self, case):
        log.info('正在执行调用执行数据：{0}'.format(case))
        try:
            # 调用执行接口方法
            resp = Api(case).run_method()
            print('响应数据为：', resp.text)
            print('响应状态码为：', resp.status_code)
            # 断言
            common_assert(resp, case)
            # 将执行结果写入报告
            Test01.tool.write_excel(case.get('x_y'), '执行通过')
        except Exception as e:
            Test01.tool.write_excel(case.get('x_y'), '执行失败！原因：{0}'.format(e))
            log.error('错误，原因：{0}'.format(e))
            raise

