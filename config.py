# -*- coding: UTF-8 -*-
"""
@Project ：PythonAutoTest 
@File    ：config.py
@IDE     ：PyCharm 
@Author  ：胖妞
@Date    ：2022/5/31 0:01
"""

import os

# 1. 基路径
base_path = os.path.dirname(__file__)
# 2. 主机地址
host = "http://ihrm-test.itheima.net"
# 3. excel数据对应列
cell_config = {
    "path": 5,
    "method": 6,
    "headers": 7,
    "param_type": 8,
    "params": 9,
    "expect": 10,
    "is_run": 11,
    "result": 12,
    "desc": 13
}
