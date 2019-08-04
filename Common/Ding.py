# -*- coding: utf-8 -*-
'''
@编写者：wjh
@文件名：Ding.py
@文件创建时间：2019-6-30 22:12:03
'''
import xml

import requests
import os
import json
from bs4 import BeautifulSoup
import calendar

HEADERS = {'ua':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
DINGDING_URL = '钉钉机器人'
REPORT_URL_FILE = '/Users/wx/Dev/Env/Jenkins/tomcat_jenkins/jenkinss/workspace/xxptcs_运营平台接口自动化测试报告/allure-report/windows/executors.json'

class Message():

    def __init__(self):
        self.total = 0
        self.passed = 0
        self.failed = 0
        self.skipped = 0
        self.reportUrl = ''

    # 解析文件获取结果数据
    def analyze(self):
        # 打开xml文档
        # dom = xml.dom.minidom.parse(RESULT_FILE)
        # 得到文档元素对象

        # root = dom.documentElement
        # self.total = root.getAttribute('total')
        # self.passed = root.getAttribute('passed')
        # self.failed = root.getAttribute('failed')
        # self.skipped = root.getAttribute('skipped')

        # 构建的次数统计在json文件中
        # file = open(REPORT_URL_FILE, 'r')
        # self.reportUrl = json.load(file)[0]['reportUrl']
        # print(self.reportUrl)

        reportdata = {}

        casesres_1 = []
        cases_1 = []
        cases_result = []
        cases_name = []
        cases_duration = []

        path = os.path.split(os.path.realpath(__file__))[0]
        fp = open('%S/report.html' % path.replace('Common', 'pytestReport'), 'r')
        soup = BeautifulSoup(fp, 'html.parser')     # 根据文件内容新建一个BeautifulSoup对象
        data_p = soup.find_all('p')
        data_a = soup.find_all('span')
        data_body = soup.find_all('tbody')
        data_result = soup.find_all('td', class_ = 'col-result')
        data_name = soup.find_all('td', class_ = 'col-name')
        data_duration = soup.find_all('td', class_ = 'col-duration')

        for p in data_p[0]:
            if 'on' in p:
                if len(str(list(calendar.month_abbr).index(p[p.index('on') + 2:p.index('by')].strip()[3:6]))) == 1:
                    reportdata['casedate'] = '%s-0%d-%s %s' % (p[p.index('on') + 2:p.index('by')].strip()[7:11],
                                                               list(calendar.month_abbr).index(p[p.index('on') + 2:p.index('by')].strip()[3:6]),
                                                               p[p.index('on') + 2:p.index('by')].strip()[0:2],
                                                               p[p.index('on') + 2:p.index('by')].strip()[15:])

                else:
                    reportdata['casedate'] = '%s-%d-%s %s' % (p[p.index('on') + 2:p.index('by')].strip()[7:11],
                                                              list(calendar.month_abbr).index(
                                                                  p[p.index('on') + 2:p.index('by')].strip()[3:6]),
                                                              p[p.index('on') + 2:p.index('by')].strip()[0:2],
                                                              p[p.index('on') + 2:p.index('by')].strip()[15:]
                                                              )

        for i in data_a:
            casesres_d = {}
            casesres_d[i.string[i.string.index(' ') + 1:]] = i.string
            casesres_1.append(casesres_d)

        for result in data_result:
            cases_result.append(result.string)

        for name in data_name:
            cases_name.append(name.string[name.string.index(':test_') + 1:])

        for duration in data_duration:
            cases_duration.append(duration.string)

        for num in range(len(data_body)):
            cases_d = {}
            cases_d['case_name'] = cases_name[num]
            cases_d['case_duration'] = cases_duration[num]
            cases_d['case_result'] = cases_result[num]
            cases_1.append(cases_d)

        reportdata['casetotal'] = data_p[1].string[:(data_p[1].string.index('tests'))].strip()
        reportdata['casestime'] = '{}'.format(data_p[1].string[(data_p[1].string.index('in') + 2):].strip().replace('seconds','s'))
        reportdata['casesres'] = casesres_1
        reportdata['cases'] = cases_1

        # print(reportdata)
        return reportdata

    # markdown测试
    def send2robot(self):
        headers = {
            'Content-Type': 'application/json',
            'charset': 'utf-8'
        }
        oapi_url = DINGDING_URL

        post_data = {
            'actionCard': {
                'title': 'XXQG_运营平台接口自动化测试报告',
                'text': 'XXQG_运营平台接口自动化测试报告\n\n'
                        '报告生成时间：{}\n\n'
                        '测试执行用时：{}\n\n'
                        '测试结果：用例总计：{}，通过：{}，失败：{}，通过率：{:.2%}。\n'
                        .format(Message().analyze()['casesdate'],
                                Message().analyze()['casestime'],
                                Message().analyze()['casestotal'],
                                Message().analyze()['casesres'][0]['passed'].replace('passed',''),
                                Message().analyze()['casesres'][0]['failed'].replace('failed',''),
                                int(Message().analyze()['casesres'][0]['passed'].replace('passed',''))/int(Message().analyze()['casestotal'])),
                'hideAvatar': '0',
                'btnOrientation': '0',
                'singleTitle': '测试详情',
                'singleURL': 'dingtalk://.....&pc_slide=false'
            },
            'msgtype':'actionCard'
        }

        result = requests.post(oapi_url, data=json.dumps(post_data), headers=headers)
        errmsg = result.json().get('errmsg')
        if errmsg != 'ok':
            print('post error:%s' % (errmsg))
        else:
            print('post ok!')

if __name__ == '__main__':
    message = Message()
    message.analyze()
    message.send2robot()


