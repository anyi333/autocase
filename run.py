# -*- coding: utf-8 -*-
"""
@编写者: wx
@文件名: run.py
@文件创建时间: 2019-02-21 16:52
"""

"""
运行用例集：
    python3 run.py
​
# '--allure_severities=critical, blocker'
# '--allure_stories=测试模块_demo1, 测试模块_demo2'
# '--allure_features=测试features'
​
"""
import sys

import pytest

from Common import Log
from Common import Shell
from Conf import Config

if __name__ == '__main__':
    conf = Config.Config()
    log = Log.MyLog()
    log.info('初始化配置文件, path=' + conf.conf_path)

    shell = Shell.Shell()
    xml_report_path = conf.xml_report_path
    html_report_path = conf.html_report_path
    pytest_html_report_path = conf.pytest_html_report_path

    # 定义测试集
    #allure_list = '--allure_features=ContentLibrarySearch'

    allure_list = '--allure_features=SpecialTest,评论筛选项操作CommentFeature,CommentSearch,CommentFeature,' \
                  'CardSingleTest,CardCombinationTest,CardGroupTest,CardNavigationTest,CardSideBySideTest,' \
                  'CardSlideTest,SpecialAuditSearch,SpecialSearch,OpNewsTest,KvideoplaylistTest,OpVideoTest,ContentLibrarySearch,' \
                  'OpSettingSearch'
    #allure_list = '--allure_features=评论筛选项操作CommentFeature'  # Comment,Personal
    #allure_list = '--allure_features=CardSlideTest'
    #allure_list = '--allure_features=SpecialTest'
    args = ['--html', pytest_html_report_path, '-s', '-q', '--alluredir', xml_report_path, allure_list]
    log.info('执行用例集为：%s' % allure_list)
    self_args = sys.argv[1:]
    pytest.main(args + self_args)
    cmd = 'allure generate %s -o %s' % (xml_report_path, html_report_path)

    try:
        shell.invoke(cmd)
    except Exception:
        log.error('执行用例失败，请检查环境配置')
        raise

    # from Common import Email
    # try:
    #     mail = Email.SendMail()
    #     mail.sendMail()
    #
    # except:
    #     log.error('发送邮件失败，请检查邮件配置')
    #     raise

    from Common import Ding

    try:
        sendreport = Ding.Message()
        sendreport.send2robot()

    except:
        log.error('钉钉发送测试报告失败，请检查配置')
        raise
