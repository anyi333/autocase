# -*- coding: utf-8 -*-
"""
@编写者: wx
@文件名: Shells.py
@文件创建时间: 2019-02-21 16:37
"""


"""
封装执行shell语句方法
​
"""

import subprocess


class Shell:
    @staticmethod
    def invoke(cmd):
        output, errors = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
        o = output.decode("utf-8")
        return o