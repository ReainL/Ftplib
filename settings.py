#!/usr/bin/env python3.5
# encoding: utf-8
"""
Created on 18-4-26
@title: '配置信息'
@author: Xusl
"""
import os.path
import logging.handlers


BASE_DIR = '/home/xsl'

# 临时文件目录
TEMP_HOME = os.path.join(BASE_DIR, 'temp')

# 数据文件目录
local_data_home = os.path.join(BASE_DIR, 'data')
if not os.path.exists(local_data_home):
    os.makedirs(local_data_home, exist_ok=True)

# 文件服务器参数
ftp_param = {
    'host': '10.12.8.22',
    'port': 2121,
    'user': 'user',
    'pwd': 'uesr1234',
    'points_dir': 'comm/cust_point/',
    'xsl': 'xsl/dps'
}

# 数据库服务器
db_param = {
    "DPS": {
            'host': '10.12.8.22',
            'port': 5432,
            'dbname': 'dps_dev',
            'user': 'user',
            'password': 'pwd',
            'DBType': 'PostgreSQL',
            'remark': 'Pg数据库',
        },
    "DPS_2": {
            'host': '10.12.7.16',
            'port': 1521,
            'dbname': 'dps_dev',
            'user': 'user',
            'password': 'pwd',
            'DBType': 'Oracle',
            'remark': 'Oracle数据库',
    }
}

# 系统标识
sys_flag_dps = 'DPS'

# 日志level, 生产使用error级别
log_level = logging.DEBUG
# 日志文件目录
log_home = os.path.join(BASE_DIR, 'log', 'ftp')
if not os.path.exists(log_home):
    os.makedirs(log_home, exist_ok=True)





