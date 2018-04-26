#!/usr/bin/env python3.5
# encoding: utf-8
"""
Created on 18-4-26
@title: '连接数据库'
@author: Xusl
"""
import os
import psycopg2
import cx_Oracle
import pymssql

from Ftplib.settings import db_param


def get_conn(sys_code='DPS'):
    """
    数据库连接获取
    :return:
    """
    params = db_param[sys_code]
    host = params['host']
    port = params['port']
    database = params['dbname']
    user = params['user']
    password = params['password']
    db_type = params['DBType'].upper()
    # 如果是pg数据库使用第一种连接方式,如果是Oracle数据库使用第二种方式,如果是SQL Server数据库则使用第三种连接方式
    if db_type == "PostgreSQL".upper():
        return psycopg2.connect(database=database, user=user, password=password, host=host, port=port)
    elif db_type == "Oracle".upper():
        os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
        dsn = cx_Oracle.makedsn(host, port, service_name=database)
        conn = cx_Oracle.connect(user, password, dsn=dsn)
        return conn
    elif db_type == 'SQLServer'.upper():
        return pymssql.connect(host=host, user=user, password=password, database=database, charset="utf8")
    else:
        raise Exception("源系统%s数据库连接失败. " % sys_code)

