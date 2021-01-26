# -*- coding: utf-8 -*-
'''
    @项目配置文件
    @January, 1, 8
    @author: lc
'''

import os
from os.path import dirname, abspath
import uuid
import logging

PARENT_DIR = abspath(dirname(os.getcwd()))
#当前目录
BASE_DIR = dirname(dirname(abspath(__file__)))

# 静态文件路径
STATIC_DIR = os.path.join(BASE_DIR, 'static')
# 模板路径
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')
# 数据路径
DATA_DIR = os.path.join(PARENT_DIR, 'data')

Code_dict = {'电线':'CAB','电容':'CAP','控制器':'CNL','壳体':'COV','单片机':'CPU','端子':'CRT','晶振':'CRY',
             '二极管':'DIO','三极管':'DYN','防静电管':'ESD','保险丝':'FUS','孔座':'HUS','芯片':'ICE','插接件':'LBC',
             '金属支架':'MFC','线路板':'PCB','包装材料':'PKG','继电器':'REL','电阻':'RES','BNC头':'RFC','滤光片':'SEN',
             '壳体总成':'SKT','线路板总成':'SMA','传感器':'SOR','软件':'SFT','金属件':'STD','辅料':'SUP','套管':'TUB',
             '稳压管':'VRT','连接线':'WHS','标签':'LAB','贴片':'MPZ','塑胶材料':'PAS','客供材料':'KGCL','临时物料':'LS'}

sheet_error = ['KGCL','LS','CAP']
KH_name_list = ['八恺电气科技有限公司','滨松电子','北京瑞龙祥','铭威光电（MW-HS-4）','江苏亿东称重系统']
BM_name_list = ['品质部','研发部','生产部','工程部','物料部','市场部','通用临时物料']

column_list_cab = ['序号','零件号','品名','规格参数','客户','备注','日期']

