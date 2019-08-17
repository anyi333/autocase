# -*- coding: utf-8 -*-
"""
@编写者: wx
@文件名: params.py
@文件创建时间: 2019-02-21 16:50
"""

"""
定义所有测试数据
​
"""
import os
from Params import tools
from Common import Log

log = Log.MyLog()
path_dir = str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))


def get_parameter(name):
    data = tools.GetPages().get_page_list()
    param = data[name]
    return param


def get_parameters(page, name):
    data = tools.GetPages().get_pages_list(page)
    param = data[name]
    return param


class CommentSearch:
    log.info('解析yaml, Path:' + path_dir + '/Params/Comment/CommentSearch.yaml')
    params = get_parameters('Comment', 'CommentSearch')
    url = []
    data = []
    header = []
    for i in range(0, len(params)):
        url.append(params[i]['url'])
        data.append(params[i]['data'])
        header.append(params[i]['header'])


class CommentFeature:
    log.info('解析yaml, Path:' + path_dir + '/Params/Comment/CommentFeature.yaml')
    params = get_parameters('Comment', 'CommentFeature')
    url = []
    data = []
    header = []
    for i in range(0, len(params)):
        url.append(params[i]['url'])
        data.append(params[i]['data'])
        header.append(params[i]['header'])


class CardSingle:  # 单卡片
    log.info('解析yaml, Path:' + path_dir + '/Params/Card/CardSingleCreate.yaml')
    params = get_parameters('Card', 'CardSingleCreate')
    url = []
    data = []
    header = []
    for i in range(0, len(params)):
        url.append(params[i]['url'])
        data.append(params[i]['data'])
        header.append(params[i]['header'])


class CardCombination:  # 组合卡片
    log.info('解析yaml, Path:' + path_dir + '/Params/Card/CardCombinationCreate.yaml')
    params = get_parameters('Card', 'CardCombinationCreate')
    url = []
    data = []
    header = []
    for i in range(0, len(params)):
        url.append(params[i]['url'])
        data.append(params[i]['data'])
        header.append(params[i]['header'])


class CardNavigation:  # 组合卡片
    log.info('解析yaml, Path:' + path_dir + '/Params/Card/CardNavigationCreate.yaml')
    params = get_parameters('Card', 'CardNavigationCreate')
    url = []
    data = []
    header = []
    for i in range(0, len(params)):
        url.append(params[i]['url'])
        data.append(params[i]['data'])
        header.append(params[i]['header'])


class CardGroup:  # 专题组合卡片
    log.info('解析yaml, Path:' + path_dir + '/Params/Card/CardGroupCreate.yaml')
    params = get_parameters('Card', 'CardGroupCreate')
    url = []
    data = []
    header = []
    for i in range(0, len(params)):
        url.append(params[i]['url'])
        data.append(params[i]['data'])
        header.append(params[i]['header'])


class CardSideBySide:  # 一行二图卡片
    log.info('解析yaml, Path:' + path_dir + '/Params/Card/CardSideBySideCreate.yaml')
    params = get_parameters('Card', 'CardSideBySideCreate')
    url = []
    data = []
    header = []
    for i in range(0, len(params)):
        url.append(params[i]['url'])
        data.append(params[i]['data'])
        header.append(params[i]['header'])


class CardSlide:  # 图文横滑卡片
    log.info('解析yaml, Path:' + path_dir + '/Params/Card/CardSlideCreate.yaml')
    params = get_parameters('Card', 'CardSlideCreate')
    url = []
    data = []
    header = []
    for i in range(0, len(params)):
        url.append(params[i]['url'])
        data.append(params[i]['data'])
        header.append(params[i]['header'])


class Special:  # 专题
    log.info('解析yaml, Path:' + path_dir + '/Params/Special/SpecialCreate.yaml')
    params = get_parameters('Special', 'SpecialCreate')
    url = []
    data = []
    header = []
    for i in range(0, len(params)):
        url.append(params[i]['url'])
        data.append(params[i]['data'])
        header.append(params[i]['header'])


class SpecialAuditSearch:  # 专题送签列表
    log.info('解析yaml, Path:' + path_dir + '/Params/Special/SpecialAuditSearch.yaml')
    params = get_parameters('Special', 'SpecialAuditSearch')
    url = []
    data = []
    header = []
    for i in range(0, len(params)):
        url.append(params[i]['url'])
        data.append(params[i]['data'])
        header.append(params[i]['header'])


class SpecialSearch:  # 专题列表
    log.info('解析yaml, Path:' + path_dir + '/Params/Special/ContentLibaraySearch.yaml')
    params = get_parameters('Special', 'SpecialSearch')
    url = []
    data = []
    header = []
    for i in range(0, len(params)):
        url.append(params[i]['url'])
        data.append(params[i]['data'])
        header.append(params[i]['header'])


class ContentLibrarySearch:  # 内容库列表
    log.info('解析yaml, Path:' + path_dir + '/Params/Card/ContentLibrarySearch.yaml')
    params = get_parameters('Card', 'ContentLibrarySearch')
    url = []
    data = []
    header = []
    for i in range(0, len(params)):
        url.append(params[i]['url'])
        data.append(params[i]['data'])
        header.append(params[i]['header'])


class OpNews:  # 图文运营
    log.info('解析yaml, Path:' + path_dir + '/Params/Card/OpNewsCreate.yaml')
    params = get_parameters('Card', 'OpNewsCreate')
    url = []
    data = []
    header = []
    for i in range(0, len(params)):
        url.append(params[i]['url'])
        data.append(params[i]['data'])
        header.append(params[i]['header'])


class KVideoPlaylistCreate:  # 创建播单
    log.info('解析yaml, Path:' + path_dir + '/Params/KVideoPlaylist/KVideoPlaylistCreate.yaml')
    params = get_parameters('KVideoPlaylist', 'KVideoPlaylistCreate')
    url = []
    data = []
    header = []
    for i in range(0, len(params)):
        url.append(params[i]['url'])
        data.append(params[i]['data'])
        header.append(params[i]['header'])


class YesAssert:  #
    log.info('解析yaml, Path:' + path_dir + '/Params/YesAssert.yaml')
    params = get_parameter('YesAssert')
    url = []
    data = []
    header = []
    for i in range(0, len(params)):
        url.append(params[i]['url'])
        data.append(params[i]['data'])
        header.append(params[i]['header'])

class OpVideo:  # 视频栏目运营
    log.info('解析yaml, Path:' + path_dir + '/Params/Card/OpVideoCreate.yaml')
    params = get_parameters('Card', 'OpVideoCreate')
    url = []
    data = []
    header = []
    for i in range(0, len(params)):
        url.append(params[i]['url'])
        data.append(params[i]['data'])
        header.append(params[i]['header'])

class OpSettingSearch:  # 运营列表筛选
    log.info('解析yaml, Path:' + path_dir + '/Params/Card/OpSettingSearch.yaml')
    params = get_parameters('Card', 'OpSettingSearch')
    url = []
    data = []
    header = []
    for i in range(0, len(params)):
        url.append(params[i]['url'])
        data.append(params[i]['data'])
        header.append(params[i]['header'])


# class Personal:
#     log.info('解析yaml, Path:' + path_dir + '/Params/Yaml/CardSingleCreate.yaml')
#     params = get_parameter('')
#     url = []
#     data = []
#     header = []
#     for i in range(0, len(params)):
#         url.append(params[i]['url'])
#         data.append(params[i]['data'])
#         header.append(params[i]['header'])


# class Collections:
#     log.info('解析yaml, Path:' + path_dir + '/Params/Yaml/Collections.yaml')
#     params = get_parameter('Comment','CommentFeature')
#     url = []
#     data = []
#     header = []
#     for i in range(0, len(params)):
#         url.append(params[i]['url'])
#         data.append(params[i]['data'])
#         header.append(params[i]['header'])


# class Personal:
#     log.info('解析yaml, Path:' + path_dir + '/Params/Yaml/Personal.yaml')
#     params = get_parameter('Personal')
#     url = []
#     data = []
#     header = []
#     for i in range(0, len(params)):
#         url.append(params[i]['url'])
#         data.append(params[i]['data'])
#         header.append(params[i]['header'])
#
#
# class Login:
#     log.info
(
'解析yaml, Path:'
 + path_dir +
'/Params/Yaml/Login.yaml'
)
#     params = get_parameter('Login')
#     url = []
#     data = []
#     header = []
#     for i in range(0, len(params)):
#         url.append(params[i]['url'])
#         data.append(params[i]['data'])
#         header.append(params[i]['header'])
