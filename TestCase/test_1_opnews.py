# -*- coding: utf-8 -*-
"""
@编写者: wjh
@文件名: test_9_opnews.py
@文件创建时间: 2019-5-5 19:23:11
"""

import sys
from os import path

import allure
import pytest
import time
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from Params.params import OpNews
from Conf.Config import Config
from Common import Request
from Common import Consts
from Common import Assert
from Common import Log

resdic = {}
log = Log.MyLog()

class TestOpNews:

    @pytest.allure.feature('OpNewsTest')
    @allure.severity('normal')
    @allure.story('图文栏目运营PDF测试-OpNewsTest')
    @pytest.mark.parametrize("action",  # 用例参数
                             [("action"),  # 用例参数的参数化数据
                              ],
                             ids=["图文栏目运营-PDF-大图-无角标",  # 对应用例参数化数据的用例名
                                  ])
    def test_op_news_53(self, action):
        """
            用例描述：图文栏目运营-PDF-大图-无角标
        """
        conf = Config()
        data = OpNews()
        test = Assert.Assertions()
        request = Request.Request(action)
​
        host = conf.host_release
        req_url = 'https://' + host
        urls = data.url
        params = data.data
        headers = data.header
        for key, value in params[52][0].items():
            if key == 'display_setting':
                params[52][0][key]['title'] = 'testdata-运营PDF-大图-无角标%s' % time.strftime("%Y%m%d%H%M",
                                                                                         time.localtime())
        resdic['title'] = params[52][0]['display_setting']['title']
        api_url = req_url + urls[52]
        response = request.post_request(api_url, params[52][0], headers[52])
        resdic['itemid'] = response['body']['data']
        resdic['isbanner'] = params[52][0]['is_banner']
        resdic['channelid'] = params[52][0]['channel_id']
        log.debug("opnews:%s" % resdic)
        assert test.assert_code(response['code'], 200)
        assert test.assert_body(response['body'], 'message', u'操作成功')
        assert test.assert_body(response['body'], 'status', 0)
        Consts.RESULT_LIST.append('True')