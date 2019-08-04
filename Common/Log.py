# -*- coding: utf-8 -*-
"""
@编写者: wx
@文件名: Logs.py
@文件创建时间: 2019-02-21 16:35
"""

"""
封装log方法
​
"""

import logging
import os
import time
import json
import requests

LEVELS = {
    'debug': logging.DEBUG,
    'info': logging.INFO,
    'warning': logging.WARNING,
    'error': logging.ERROR,
    'critical': logging.CRITICAL,
}

logger = logging.getLogger()
level = 'default'

def create_file(filename):
    path = filename[0:filename.rfind('/')]
    if not os.path.isdir(path):
        os.makedirs(path)
    if not os.path.isfile(filename):
        fd = open(filename, mode='w', encoding='utf-8')
        fd.close()
    else:
        pass

def set_handler(levels):
    if levels == 'error':
        logger.addHandler(MyLog.err_handler)
    elif levels == 'debug':
        logger.addHandler(MyLog.debug_handler)
    logger.addHandler(MyLog.handler)

def remove_handler(levels):
    if levels == 'error':
        logger.removeHandler(MyLog.err_handler)
    elif levels == 'debug':
        logger.removeHandler(MyLog.debug_handler)
    logger.removeHandler(MyLog.handler)

def get_current_time():
    return time.strftime(MyLog.date, time.localtime(time.time()))

# def get_current_filetime():
#     return time.strftime(MyLog.datefile, time.localtime(time.time()))
    #     ​
class MyLog:
    date = '%Y-%m-%d %H:%M:%S'
    datefile = '%Y-%m-%d'

    path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    log_file = path+'/Log/log.log'
    err_file = path+'/Log/err.log'
    log_debug_file = path + '/Log/' + 'Debug.%s.log' % (time.strftime(datefile, time.localtime(time.time())))

    logger.setLevel(LEVELS.get(level, logging.NOTSET))
    create_file(log_file)
    create_file(err_file)
    create_file(log_debug_file)

    handler = logging.FileHandler(log_file, encoding='utf-8')
    debug_handler = logging.FileHandler(log_debug_file, encoding='utf-8')
    err_handler = logging.FileHandler(err_file, encoding='utf-8')

    @staticmethod
    def debug(log_meg):
        set_handler('debug')
        logger.debug(get_current_time() + " [Debug]:" + "".join(log_meg))
        ColorLog.show_debug(get_current_time() + " [Debug]:" + "".join(log_meg))
        remove_handler('debug')

    @staticmethod
    def info(log_meg):
        set_handler('info')
        logger.info(get_current_time() + " [Info]:" + "".join(log_meg))
        ColorLog.show_info(get_current_time() + " [Info]:" + "".join(log_meg))
        remove_handler('info')

    @staticmethod
    def warning(log_meg):
        set_handler('warning')
        logger.warning(get_current_time() + " [Warn]:" + "".join(log_meg))
        ColorLog.show_warn(get_current_time() + " [Warn]:" + "".join(log_meg))
        remove_handler('warning')

    @staticmethod
    def error(log_meg):
        set_handler('error')
        logger.error(get_current_time() + " [Error]:" + "".join(log_meg))
        ColorLog.show_error(get_current_time() + " [Error]:" + "".join(log_meg))
        remove_handler('error')

    @staticmethod
    def critical(log_meg):
        set_handler('critical')
        logger.error(get_current_time() + " [Critical]:" + "".join(log_meg))
        ColorLog.show_error(get_current_time() + " [Critical]:" + "".join(log_meg))
        remove_handler('ritical')

    @staticmethod
    def read(log_type):
        reslist = []
        path_txt = str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))) + '/Log'
        #with open('%s/Debug.%s.log' % (path_txt, time.strftime('%Y-%m-%d', time.localtime(time.time()))), 'r+', encoding='utf-8') as f:
        f = open('%s/Debug.%s.log' % (path_txt, time.strftime('%Y-%m-%d', time.localtime(time.time()))), 'r+',
             encoding='utf-8')
            #flist = f.readlines()
        for i in f.readlines():
            if log_type in i:
                #print(log_type)
                res = json.loads(i[i.index('{'):].replace("'", '"'))
                reslist.append(res)
        return reslist



class ColorLog:
    @staticmethod
    def c(msg, colour):
        try:
            from termcolor import colored, cprint
            p = lambda x: cprint(x, '%s' % colour)
            return p(msg)
        except:
            print(msg)

    @staticmethod
    def show_verbose(msg):
        ColorLog.c(msg, 'white')

    @staticmethod
    def show_debug(msg):
        ColorLog.c(msg, 'blue')

    @staticmethod
    def show_info(msg):
        ColorLog.c(msg, 'green')

    @staticmethod
    def show_warn(msg):
        ColorLog.c(msg, 'yellow')

    @staticmethod
    def show_error(msg):
        ColorLog.c(msg, 'red')


if __name__ == "__main__":
        # MyLog.debug("This is debug message")
        # MyLog.info("This is info message")
        # MyLog.warning("This is warning message")
        # MyLog.error("This is error")
        # MyLog.critical("This is critical message")
        print(MyLog.read('special'))