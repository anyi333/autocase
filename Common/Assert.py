# -*- coding: utf-8 -*-
'''
@编写者：wjh
@文件名：Assert.py
@文件创建时间：2019-6-29 17:14:27
'''

'''
封装Assert方法
'''
from Common import Log
from Common import Consts
import json
import time

class Assertions:
    def __init__(self):
        self.log = Log.MyLog()

    def assert_code(self, code, expected_code):
        '''
        验证response状态码
        :param code:
        :param expected_code:
        :return:
        '''
        try:
            assert code == expected_code
            return True
        except:
            self.log.error("statusCode, expected_code is %s, statusCode is %s" % (expected_code, code))
            Consts.RESULT_LIST.append('fail')

            raise

    def assert_status(self, code, excpected_code, error_data):
        '''
        验证response状态码
        :param code:
        :param excpected_code:
        :param error_data:
        :return:
        '''
        try:
            assert code == excpected_code
            return True
        except:
            self.log.error("statusCode error, excpected_code is %s, statusCode is %s error_data is %s" % (excpected_code, code, error_data))
            Consts.RESULT_LIST.append('fail')

            raise

    def assert_body(self, body, body_msg, expected_msg):
        '''
        验证response body中任意属性的值
        :param body:
        :param body_msg:
        :param expected_msg:
        :return:
        '''
        try:
            msg = body[body_msg]
            assert msg == expected_msg
            return True
        except:
            self.log.error("Response body msg != expected_msg, expected_msg is %s, body_msg is %s" % (expected_msg,body_msg))
            Consts.RESULT_LIST.append('fail')

            raise

    def assert_bodylist(self, bodylist):
        '''
        验证response body中列表包含字典的属性值
        :param bodylist:
        :return:
        '''
        if type(bodylist) == list:
            for num in range(len(bodylist)):
                return num

    def assert_in_text(self, body, expected_msg):
        '''
        验证response body 中是否包含预期字符串
        :param body:
        :param expected_msg:
        :return:
        '''
        try:
            text = json.dumps(body, ensure_ascii=False)
            # print(text)
            assert expected_msg in text
            return True

        except:
            self.log.error("Response body Does not contain expected_msg, expected_msg is %s" % expected_msg)
            Consts.RESULT_LIST.append('fail')
            raise

    def assert_text(self, body, expected_msg, error_data):
        '''
        验证response body 中是否等于预期字符串
        :param body:
        :param expected_msg:
        :param error_data:
        :return:
        '''
        try:
            assert body == expected_msg
            return True
        except:
            self.log.error("Response body != expected_msg, expected_msg is %s, body is %s, error_data is %s" % (expected_msg, body, error_data))
            Consts.RESULT_LIST.append('fail')
            raise

    def assert_time(self, time, expected_time):
        '''
        验证response body 响应时间小于预期最大响应时间，单位：毫秒
        :param body:
        :param expected_time:
        :return:
        '''
        try:
            assert time < expected_time
            return True
        except:
            self.log.error("Response time > expected_time, expected_time is %s, time is %s" % (expected_time, time))
            Consts.RESULT_LIST.append('fail')
            raise

    def assert_datetime(self, datetime, expected_start_datetime, expected_end_datetime):
        '''
        验证response body 响应时间小于预期最大相应时间，单位：毫秒
        :param body:
        :param expected_start_datetime:
        :param expected_end_datetime:
        :return:
        '''
        try:
            assert datetime > expected_start_datetime and datetime < expected_end_datetime
            return True
        except:
            self.log.error("Response datetime not in expected_datetime, expected_datetime is %s~%s, datetime is %s" % (time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(expected_start_datetime)), time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(expected_start_datetime)),datetime))
            Consts.RESULT_LIST.append('fail')
            raise