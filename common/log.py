#!/usr/bin/env python3.5
# encoding: utf-8
"""
Created on 18-4-26
@title: '日志配置'
@author: Xusl
"""
from Ftplib.settings import log_level
from Ftplib.common.get_conn import get_conn


def get_log_config(log_file):
    """

    :param log_file:
    :return:
    """
    log_config = {
        'version': 1,
        'formatters': {
            'generic': {
                'format': '%(asctime)s %(levelname)-5.5s [%(name)s:%(lineno)s][%(threadName)s] %(message)s',
            },
            'simple': {
                'format': '%(asctime)s %(levelname)-5.5s %(message)s',
            },
        },
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
                'formatter': 'generic',
            },
            'file': {
                'class': 'logging.FileHandler',
                'filename': log_file,
                'encoding': 'utf-8',
                'formatter': 'generic',

            },
        },
        'root': {
            'level': log_level,
            'handlers': ['console', 'file'],
        }
    }
    return log_config


def insert_sys_log(log_content):
    """
    添加系统日志
    :param log_content:
    :return:
    """
    param_val = (log_content['log_type'],
                 log_content['log_level'],
                 log_content['msg'],
                 log_content['create_date'],
                 log_content['create_user'],)
    sql_insert_sys_log = """
    INSERT INTO web.sys_log(id, log_type, log_level, msg, create_date, create_user)
    VALUES(nextval('web.seq_log_id'), %s, %s, %s, %s, %s)
    """
    conn = get_conn()
    try:
        with conn:
            with conn.cursor() as cur:
                cur.execute(sql_insert_sys_log, param_val)
    finally:
        conn.close()
